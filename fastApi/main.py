import os
import re
import pickle
import numpy as np
import pandas as pd
import collections
from pathlib import Path
from random import randrange
from datetime import datetime

import psycopg2
import qrcode
from loguru import logger
from dotenv import load_dotenv
from geopy.geocoders import Nominatim, Yandex

from typing import Union
from pydantic import BaseModel
from fastapi import  APIRouter
from fastapi.responses import  FileResponse
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

import gensim
from clasterisation.miniBatch import MiniBatch

# Загрузка предобученных моделей обработки текста.
path = Path().cwd().joinpath('clasterisation')
minibatchkmeans = 0
router = APIRouter()
word2vec = gensim.models.Word2Vec.load(str(path.joinpath('word2vec.model')))
with open(str(path.joinpath('model.pkl')), 'rb') as f:
    minibatchkmeans = pickle.load(f)
logger.success('Model loading succesful!')

# Внесение конфига для подключения к БД (не важно где она)
load_dotenv('../DB.ENV', override=True)
SOURCE = os.environ.get('SOURCE')
GEOCODER = os.environ.get('GEOCODER')

# Геокодер для отобраджения на карте полученных отзывов
if GEOCODER == 'YANDEX':
    try:
        GEOCODER = Yandex(api_key=os.environ.get('YANDEX_API'), user_agent="POSTAMAT PROJECT")
        logger.success('Using API-Yandex GEOCODER')
    except Exception as e:
        logger.error(e)
elif GEOCODER == 'DEFAULT':
    try:
        GEOCODER = Nominatim(user_agent="POSTAMAT PROJECT")
        logger.success('Using default OpenStreetMap GEOCODER ')
    except Exception as e:
        logger.error(e)

# Инициализация переменных
conn = 0
cur = 0
old_stats = 0

CLASSIFICATOR_CLASSES = {
    '0': 'good',
    '1': 'article',
    '2': 'delivery',
    '3': 'post',
    '4': 'times'
}

CLASSIFICATOR_RUS_CLASSES = {
    '0': 'Все хорошо',
    '1': 'Проблема с товаром',
    '2': 'Проблема с доставкой',
    '3': 'Проблема с постаматом (ПВЗ)',
    '4': 'Проблема со сроками'
}

MONTH_NAMES = {
    '1': 'january',
    '2': 'february',
    '3': 'march',
    '4': 'april',
    '5': 'may',
    '6': 'june',
    '7': 'july',
    '8': 'august',
    '9': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december'
}

# Попытка подключения к БД в Докере, На удаленной машине, На локальном компе
try:
    # Получение конфига
    IP = os.environ.get("HOST_IP")
    PORT = os.environ.get("PORT")
    DBNAME = os.environ.get("POSTGRES_DB")
    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")

    logger.debug(f'{SOURCE} connection started, {IP}, {PORT}, {DBNAME}, {USER}, {PASSWORD},  - env variables!')

    conn = psycopg2.connect(
        dbname=DBNAME,
        host=IP,
        user=USER,
        password=PASSWORD,
        port=PORT)

    cur = conn.cursor()

    logger.success(f'{SOURCE} connected!')

except Exception as e:
    logger.error(f'{SOURCE} connect failed \n {e}!')


# Функции-обертки
def String2Coords(adress):
    adress = re.sub(' к. [0-9999],', '', adress)
    adress = adress.replace('б-р. ', 'бульвар ')
    adress = adress.replace('ш. ', 'шоссе ')
    try:
        location = GEOCODER.geocode(adress, language='ru')
        data = location.latitude, location.longitude
        return True, location.latitude, location.longitude
    except Exception as e:
        logger.error(f'Wrong adress! \n {adress}')
        logger.error(e)
        return False, 0.0, 0.0


# Функция - предсказание
def String2Classs(usertext):
    pass


# Функция - анализ кластера
def String2Cluster(usertext, word2vec, minibatch):
    result = MiniBatch(usertext, word2vec, minibatch)
    return result


# Заглушка чистой воды, если пользователь обращается не по приложению обратной связи
# ЗАГЛУШКА под номера заказов! ---------------
def SomeArticleFromYourSources():
    return randrange(0, 9999999, 1)


# Конец заглушки -----------------------------

# Функция-поддержка для вывода обозначений классов
def Number2Class(code):
    return CLASSIFICATOR_CLASSES[f'{str(code)}']


# Функция-поддержка для вывода обозначений классов
def Number2RusClass(code):
    return CLASSIFICATOR_RUS_CLASSES[f'{str(code)}']


# Функция-поддержка для вывода обозначений классов
def Number2Month(code):
    return MONTH_NAMES[f'{str(code)}']


# Статистика адресов во входном запросе
def getAdressStats(result):
    stats = []
    adresses = collections.Counter([x['adress'] for x in result])
    unique_adresses = list(set(adresses.elements()))
    for adress in unique_adresses:
        substats = {
            'adress': adress,
            'stars': np.mean([float(subresult['mark']) for subresult in result if subresult['adress'] == adress]),
            'textnumbers': len([subresult['usertext'] for subresult in result if subresult['adress'] == adress]),
            'problem': Number2RusClass(collections.Counter(
                [int(subresult['classnumber']) for subresult in result if subresult['adress'] == adress]).most_common(
                1)[0][0])
        }
        stats.append(substats)
    logger.debug(stats)
    return stats


# Статистика для макретплейсов
def getMarketStats(result):
    stats = []
    markets = collections.Counter([x['seller'] for x in result])
    unique_markets = list(set(markets.elements()))
    for adress in unique_markets:
        substats = {
            'market': adress,
        }
        substats.update(collections.Counter([Number2Class(x['classnumber']) for x in result]))
        stats.append(substats)

    # ЗАГЛУШКА ПОД ДОПОЛНИТЕЛЬНЫЕ МАРКЕТПЛЕЙСЫ -------------
    # В ПРОДЕ - УДАЛЯЙ
    datapatch = collections.Counter([Number2Class(x['classnumber']) for x in result[:len(result) // 2]])
    substats = {
        'market': 'Главпиво'
    }
    substats.update(datapatch)
    stats.append(substats)
    # КОНЕЦ ЗАГЛУШКИ ---------------------------------------
    logger.debug(stats)
    return stats


# Статистика для макретплейсов
def getTotalStats(result):
    posts = collections.Counter([x['adress'] for x in result])
    markets = collections.Counter([x['seller'] for x in result])
    unique_posts = len(list(set(posts.elements())))
    unique_markets = len(list(set(markets.elements())))
    total_reviews = len(result)
    stats = {
        'postamats': unique_posts,
        'partners': unique_markets,
        'reviews': total_reviews
    }
    logger.debug(stats)
    return stats


# Статистика по классам
def getClassesStats(result):
    stats = {}
    stats.update(collections.Counter([Number2Class(x['classnumber']) for x in result]))
    logger.debug(stats)
    return stats


# Статистика по месяцам
def getTimeStats(result):
    stats = []
    data = collections.Counter([int(datetime.fromisoformat(x['reviewdate']).timestamp()) for x in result])
    keys = list(data.keys())
    values = list(data.values())

    for index in range(len(keys)):
        substats = []
        substats.append(keys[index])
        substats.append(values[index])

        stats.append(substats)

    logger.debug(stats)
    return stats

# Бэк
app = FastAPI()

origins = "*"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Access-Control-Allow-Origin", "Access-Control-Allow-Headers"],
)

# Тест на подключение
@app.get("/")
def dronescnas():
    cur.execute(f"SELECT * FROM test")
    data = cur.fetchall()
    logger.debug(data)

# Классы для работы с POST-запросами
# Получение отзыва с универсальныго источника (generic для всех остальных)
class ReviewFromAnySource(BaseModel):
    usertext: str
    mark: float
    reviewdate: str
    adress: Union[str, None] = None
    clusternumber: Union[int, None] = None
    article: Union[str, None] = None
    seller: Union[str, None] = None
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None


# Получение отзыва с телеграм-бота в котором пользователь укажет проблему и свои ПнД
class ReviewFromTelegramBot(ReviewFromAnySource):
    username: str
    chatid: str
    classnumber: int


# Фича с разметкой данных для улучшения работы Bert
class ReviewFromDatasetFormer(ReviewFromAnySource):
    classnumber: int
    id_: int


class AdminFilter(BaseModel):
    stars: Union[str, list, None] = None


# Сбор инфы по карте - адреса, отзывы, их количество и т.д


@app.get("/getAdminPageData/")
def adminPage():
    # if item.stars == None:
    # cur.execute(f"SELECT * FROM xdataset")
    # elif type(item.stars) == type([1,2,3]):
    #     cur.execute(f"SELECT * FROM xdataset WHERE mark IN (%s)", item.stars)
    # else:
    #     cur.execute(f"SELECT * FROM xdataset WHERE mark IN (%s)", item.stars)

    cur.execute(f"SELECT * FROM xdataset")
    data = cur.fetchall()
    result = []
    for index, subdata in enumerate(data):
        usertext = subdata[0]
        mark = subdata[1]
        adress = subdata[2]
        reviewdate = subdata[3]
        clusternumber = subdata[4]
        article = subdata[5]
        seller = subdata[6]
        latitude = subdata[7]
        longitude = subdata[8]
        classnumber = subdata[9]

        result.append({
            "id": index,
            "usertext": usertext,
            "mark": mark,
            "adress": adress,
            "reviewdate": str(reviewdate),
            "clusternumber": clusternumber,
            "article": article,
            "seller": seller,
            "latitude": latitude,
            "longitude": longitude,
            "classnumber": classnumber,
            "longitude": longitude

        })

    adressStats = getAdressStats(result)
    marketStats = getMarketStats(result)
    totalStats = getTotalStats(result)
    classStats = getClassesStats(result)
    timeStats = getTimeStats(result)

    total_data = {
        "data": result,
        'adressStats': adressStats,
        'marketStats': marketStats,
        'totalStats': totalStats,
        'classStats': classStats,
        'timeStats': timeStats
    }

    return JSONResponse(status_code=200, content=total_data)

# API для добавления универсального отзыва с обработкой ГЕОЛОКАЦИИ + КЛАСТЕРИЗАЦИИ + ВАШ ИСТОЧНИК НОМЕРА ЗАКАЗА

class ReviewFromAnySource(BaseModel):
    usertext: str
    mark: float
    adress: str
    reviewdate: str
    clusternumber: Union[int, None] = None
    article: Union[str, None] = None
    seller: Union[str, None] = None
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None

@app.post("/addReview/")
def intellegenceReviewProceduring(item: ReviewFromAnySource):
    # Логика обработки адресов, кластеров +чего-нибудь ещё
    # coordsChecker = False
    coordsChecker, latitude, longitude = String2Coords(item.adress)

    if item.usertext:
        clusternumber = int(String2Cluster(item.usertext, word2vec, minibatchkmeans)[0])
    article = SomeArticleFromYourSources()

    try:
        reviewdate = datetime.fromisoformat(item.reviewdate.replace('T', ' ').split('.')[0])
    except Exception as e:
        logger.error(f'Datetime error! \n {e}')

    # Если данные верны - оправляем на БД
    if coordsChecker and item.usertext and clusternumber != 999:
        # Контроль
        logger.success('User text -- ' + item.usertext)
        logger.success('Mark -- ' + str(item.mark))
        logger.success('Adress -- ' + str(item.adress))
        logger.success('Review date -- ' + str(reviewdate))
        logger.success('Cluster number (Optional) -- ' + str(clusternumber))
        logger.success('Article (Optianal) -- ' + str(article))
        logger.success('Seller (Optional) -- ' + str(item.seller))
        logger.success('Longitude (Optional) -- ' + str(longitude))
        logger.success('Latitude (Optional) -- ' + str(latitude))

        cur.execute("""
        INSERT INTO reviews 
            (usertext, mark, adress, reviewdate, clusternumber, article, seller, longitude, latitude) 
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (item.usertext, item.mark, item.adress, reviewdate, clusternumber, article, item.seller, longitude,
                     latitude))
        conn.commit()
        return Response(status_code=201)
    else:
        return Response(status_code=422)


# API для добавления отзыва из Телеграм-бота
@app.post("/addTelegramReview/")
def intellegenceTelegramReviewProceduring(item: ReviewFromTelegramBot):
    # Логика обработки адресов, кластеров +чего-нибудь ещё
    article = SomeArticleFromYourSources()

    try:
        reviewdate = datetime.fromtimestamp(item.reviewdate)
    except Exception as e:
        logger.error(f'Datetime error! \n {e}')

        # Если данные верны - оправляем на БД
        # if item.usertext:
        #     # Контроль
        #     logger.success('User text -- ' + item.usertext)
        #     logger.success('Mark -- ' + str(item.mark))
        #     logger.success('Adress -- ' + str(item.adress))
        #     logger.success('Review date -- ' + str(reviewdate))
        #     logger.success('Telegram User Name -- ' + str(item.username))
        #     logger.success('Telegram User Chat ID (for bot) -- ' + str(item.chatid))
        #     logger.success('Telegram Class number -- ' + str(item.classnumber))
        #     logger.success('Article (Optional) -- ' + str(article))
        #     logger.success('Seller (Optional) -- ' + str(item.seller))

        # В РАЗРАБОТКУ
        # cur.execute("""
        # INSERT INTO reviews
        #     (usertext, mark, adress, reviewdate, clusternumber, article, seller, longitude, latitude)
        # VALUES
        #     (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        # (item.usertext, item.mark, item.adress, reviewdate, clusternumber, article, item.seller, longitude, latitude))
        # conn.commit()

        return Response(status_code=201)
    else:
        return Response(status_code=422)


# API для датасета (получение случайной строчки из БД)
@app.get("/getFormDatasetElement/")
def getDatasetFormerElement():
    # Подсчитываем сколько строк в таблице
    cur.execute("""SELECT COUNT(*) FROM rawdataset;""")
    result = cur.fetchall()
    for index, data in enumerate(result):
        result = data[0]

    # Выбираем случайную строку
    try:
        randomRow = randrange(1, result, 1)
        cur.execute(f"""SELECT * FROM rawdataset WHERE id = {randomRow};""")
        row = cur.fetchall()
        for index, subdata in enumerate(row):
            usertext = subdata[0]
            mark = subdata[1]
            adress = subdata[2]
            reviewdate = subdata[3]
            clusternumber = subdata[4]
            article = subdata[5]
            seller = subdata[6]
            latitude = subdata[7]
            longitude = subdata[8]
            id_ = subdata[9]

    except UnboundLocalError as e:
        logger.error(e)
        randomRow = randrange(1, result, 1)
        cur.execute(f"""SELECT * FROM rawdataset WHERE id = {randomRow};""")
        row = cur.fetchall()
        for index, subdata in enumerate(row):
            usertext = subdata[0]
            mark = subdata[1]
            adress = subdata[2]
            reviewdate = subdata[3]
            clusternumber = subdata[4]
            article = subdata[5]
            seller = subdata[6]
            latitude = subdata[7]
            longitude = subdata[8]
            id_ = subdata[9]

    try:
        # Удаляем строчку с такими данными
        cur.execute(f"""DELETE FROM rawdataset WHERE id = {id_};""")
        conn.commit()
    except Exception as e:
        logger.error(e)
        conn.rollback()

    # Для статистики и отслеживания сколько экземпляров для классов есть.
    # Поможет когда будете создавать свой датасет на своих отзывах
    try:
        results = []
        for classIndex in range(0, 5, 1):
            cur.execute(f"""SELECT COUNT(*) FROM xdataset WHERE classnumber = {classIndex};""")
            result = cur.fetchall()
            subresult = result[0][0]
            results.append(subresult)
        old_stats = results
    except psycopg2.ProgrammingError as e:
        logger.error(e)
        results = old_stats

    logger.debug("Dataset balance -- " + str(results))

    jsoned = {
        "usertext": usertext,
        "mark": mark,
        "adress": adress,
        "reviewdate": str(reviewdate),
        "clusternumber": clusternumber,
        "article": article,
        "seller": seller,
        "latitude": latitude,
        "longitude": longitude,
        "id_": id_,
        "stats": results
    }

    return JSONResponse(content=jsoned, status_code=200)


# API для датасета (добавление в таблицу с выборкой + удаление из сырых данных)
@app.post("/addFormDatasetElement/")
def addDatasetFormerElement(item: ReviewFromDatasetFormer):
    # Если данные верны - оправляем на БД
    if item.usertext:
        # Контроль
        logger.success('User text -- ' + item.usertext)
        logger.success('ID -- ' + str(item.id_))
        logger.success('Mark -- ' + str(item.mark))
        logger.success('Adress -- ' + str(item.adress))
        logger.success('Review date -- ' + str(item.reviewdate))
        logger.success('Cluster number (Optional) -- ' + str(item.clusternumber))
        logger.success('Article (Optianal) -- ' + str(item.article))
        logger.success('Seller (Optional) -- ' + str(item.seller))
        logger.success('Longitude (Optional) -- ' + str(item.longitude))
        logger.success('Latitude (Optional) -- ' + str(item.latitude))
        logger.success('Marked class -- ' + str(item.classnumber))

    try:
        cur.execute("""
            INSERT INTO xdataset 
                (usertext, mark, adress, reviewdate, clusternumber, article, seller, longitude, latitude, classnumber) 
            VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (item.usertext, str(item.mark), item.adress, item.reviewdate, item.clusternumber, item.article,
                     item.seller, item.longitude, item.latitude, item.classnumber))
    except Exception as e:
        logger.error(e)
        conn.rollback()
        return Response(status_code=304)

    return Response(status_code=201)


@app.get('/getAdminPageStatsFile/')
def adminPageStatsFile():
    cur.execute(f"SELECT * FROM xdataset")
    data = cur.fetchall()
    result = []
    for index, subdata in enumerate(data):
        usertext = subdata[0]
        mark = subdata[1]
        adress = subdata[2]
        reviewdate = subdata[3]
        clusternumber = subdata[4]
        article = subdata[5]
        seller = subdata[6]
        latitude = subdata[7]
        longitude = subdata[8]
        classnumber = subdata[9]

        result.append({
            "id": index,
            "usertext": usertext,
            "mark": mark,
            "adress": adress,
            "reviewdate": str(reviewdate),
            "clusternumber": clusternumber,
            "article": article,
            "seller": seller,
            "latitude": latitude,
            "longitude": longitude,
            "classnumber": classnumber
        })

    adressStats = getAdressStats(result)
    df = pd.DataFrame(columns=['adress', 'stars', 'textnumbers', 'problem'])
    for index_, dictionary in enumerate(adressStats):
        extended = pd.DataFrame(dictionary, index=[index_])
        df = pd.concat([df, extended], ignore_index=True)

    path = "report.xlsx"
    df.to_excel("report.xlsx")
    FileResponse(path, status_code=201)


@app.get("/postamatQR/")
async def QRCodeGeneratiFromArticle(article: str, response: Response):
    cur.execute(f"SELECT article FROM reviews ORDER BY RANDOM() LIMIT 1")
    data = cur.fetchall()
    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()

    # Set the content type and send the image in the response body
    response.headers['Content-Type'] = 'image/png'
    img_bytes = img.getvalue()
    response.body = img_bytes

    # Redirect to another URL
    response.status_code = 307
    response.headers['Location'] = "/postamatQR/{article}"

