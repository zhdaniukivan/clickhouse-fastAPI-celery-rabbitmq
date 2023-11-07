from celery import Celery

from main import get_top_words

app = Celery('main', backend='rpc://', broker='pyamqp://')


@app.task
def start(x, y):
    get_top_words()





