import os
from dotenv import load_dotenv

from loguru import logger
import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

conn = 0
cur = 0

load_dotenv('../DB.ENV', override=True)
SOURCE = os.environ.get('SOURCE')

try:     
    IP=os.environ.get("HOST_IP")
    PORT=os.environ.get("PORT")
    DBNAME=os.environ.get("POSTGRES_DB")
    USER=os.environ.get("POSTGRES_USER")
    PASSWORD=os.environ.get("POSTGRES_PASSWORD")

    if SOURCE == 'Local':
        logger.debug(('Local connection started \n', IP, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))
    if SOURCE == 'Docker':
        logger.success(('Docker DB connection started \n', IP, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))
    if SOURCE == 'Host':
        logger.success(('Host connection started \n', IP, PORT, DBNAME, USER, PASSWORD, ' - env variables!'))
    
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


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def dronescnas():
    cur.execute(f"SELECT * FROM test")
    data = cur.fetchall()
    logger.debug(data)

    return JSONResponse(status_code=200, content={'hello': 'kisel'})


@app.get("/getDronesCnas/")
def dronescnas():
    cur.execute(f"SELECT * FROM dronescnas")
    data = cur.fetchall()
    result = []
    for index, subdata in enumerate(data):
        name = subdata[0]
        country = subdata[1]
        range_ = subdata[2] * 1000
        params = subdata[3]
        
        result_subdict = {
            'id': index,
            'name': name,
            'country': country,
            'range_': range_
        }
        result_subdict.update(params)

        result.append(result_subdict)

    return result

@app.get('/getSpidersData/')
def spider():
    cur.execute("SELECT * FROM spiders")
    data = cur.fetchall()
    jsoned = []
    for index, subdata in enumerate(data):
        jsoned.append({
                'spider': subdata[0],
                'url': subdata[1],
                "data": subdata[2] 
            })
        
    return jsoned


