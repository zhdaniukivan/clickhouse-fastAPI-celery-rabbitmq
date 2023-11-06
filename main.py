from fastapi import FastAPI
from fastapi.responses import JSONResponse
from clickhouse_driver import Client
from clickhouse_driver import connect
import clickhouse_connect
import json
import requests
from ujson import loads
from celery import Celery

app_celery('main', broker=)

app = FastAPI()

clickhouse_client = clickhouse_connect.get_client(port=8123, host='localhost', username='default', password='000000')




@app.get('/getWords', response_model=dict)
async def get_top_words():
    print('1')
    query_ = """
        SELECT word, count() AS word_count
        FROM
        (
            SELECT arrayJoin(splitByChar(' ', text)) AS word
            FROM news_articles.a22rticles
        )
        GROUP BY word
        ORDER BY word_count DESC
        LIMIT 100
        FORMAT JSON
    """
    data = clickhouse_client.command(query_)
    print(data)





    # for i in results:
    #     print(i)
    #     print('--------------')
    # count = len(results) - 1
    # dict_word = {}
    # for i in range(0, count, 2):
    #     dict_word[results[i]] = results[i + 1]
    #
    # print(dict_word)
    # top_word = [{'word': result[0], 'count': result[1]} for result in results]
    # print(dict_word)
    # return JSONResponse(content={'top_word': top_word})
    return {'data':'data'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='127.0.0.3', port=9090)
