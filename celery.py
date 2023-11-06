from celery import Celery

app = Celery('clickhouse_count',
             broker='amqp://',
             backend='rpc://',
             include=['clickhouse.task'])

app.conf.update(
    result_expires=3600,
)
if __name__=='__main__':
    app.start()

