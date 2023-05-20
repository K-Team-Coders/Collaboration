import os
from datetime import datetime
from random import randrange

import psycopg2
from loguru import logger
from dotenv import load_dotenv
from geopy.geocoders import Nominatim, Yandex

from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Внесение конфига для подключения к БД (не важно где она)
load_dotenv('../DB.ENV', override=True)
SOURCE = os.environ.get('SOURCE')
GEOCODER = Nominatim(user_agent="POSTAMAT PROJECT")

# # Геокодер для отобраджения на карте полученных отзывов
# try:
#     e = 1 / 0
#     logger.debug('Using API-Yandex GEOCODER')
#     # GEOCODER = Yandex(api_key="06856716-badb-42a6-9815-4c8e630af04b", user_agent="POSTAMAT PROJECT")
# except Exception as e:
#     logger.error(e)
#     logger.error('Using default GEOCODER -- OpenStreetMap')
#     GEOCODER = Nominatim(user_agent="POSTAMAT PROJECT")

# Инициализация переменных
conn = 0
cur = 0

# Попытка подключения к БД в Докере, На удаленной машине, На локальном компе
try:  
    # Получение конфига 
    IP=os.environ.get("HOST_IP")
    PORT=os.environ.get("PORT")
    DBNAME=os.environ.get("POSTGRES_DB")
    USER=os.environ.get("POSTGRES_USER")
    PASSWORD=os.environ.get("POSTGRES_PASSWORD")

    logger.debug((f'{SOURCE} connection started \n', IP, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))
    
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
    try:
        location = GEOCODER.geocode(adress, language='ru')
        return location.latitude, location.longitude
    except Exception as e:
        logger.error(f'Wrong adress! \n {adress}')
        logger.error(e)
        return 0.0, 0.0
    
# Функция - анализ кластера 
def String2Cluster(usertext):
    # В разработке
    return randrange(0, 7, 1)

# Заглушка чистой воды, если пользователь обращается не по приложению обратной связи
def SomeArticleFromYourSources():
    return randrange(0, 9999999, 1)

# Бэк
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Тест на подключение
@app.get("/")
def dronescnas():
    cur.execute(f"SELECT * FROM test")
    data = cur.fetchall()
    logger.debug(data)

    return JSONResponse(status_code=200, content={'hello': 'kisel'})

# Сбор инфы по карте - адреса, отзывы, их количество и т.д
@app.get("/getAdminPageData/")
def receive():
    cur.execute(f"SELECT * FROM reviews")
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
                "longitude": longitude
            })

    return JSONResponse(status_code=200, content=result)


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
    # Входной контроль
    logger.debug('User text -- ' + item.usertext)
    logger.debug('Mark -- ' + str(item.mark))
    logger.debug('Adress -- ' + str(item.adress))
    logger.debug('Review date -- ' + item.reviewdate)
    logger.debug('Cluster number (Optional) -- ' + str(item.clusternumber))
    logger.debug('Article (Optianal) -- ' + str(item.article))
    logger.debug('Seller (Optional) -- ' + str(item.seller))
    logger.debug('Longitude (Optional) -- ' + str(item.longitude))
    logger.debug('Latitude (Optional) -- ' + str(item.latitude))
    
    # Логика обработки адресов, кластеров +чего-нибудь ещё
    latitude, longitude = String2Coords(item.adress)
    clusternumber = String2Cluster(item.usertext)
    article = SomeArticleFromYourSources()

    try:
        reviewdate = datetime.fromisoformat(item.reviewdate.replace('T', ' ').split('.')[0])
    except Exception as e:
        logger.error(f'Datetime error! \n {e}')

    # Если данные верны - оправляем на БД
    if latitude != 0.0:
        cur.execute("""
        INSERT INTO reviews 
            (usertext, mark, adress, reviewdate, clusternumber, article, seller, longitude, latitude) 
        VALUES 
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
        (item.usertext, item.mark, item.adress, reviewdate, clusternumber, article, item.seller, longitude, latitude))    
        conn.commit()
        return Response(status_code=201)
    else:
        return Response(status_code=422)