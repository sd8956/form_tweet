# Celery
from celery import Celery

# Local
from bot.bot import make_tweet 

app = Celery('tweet',broker='amqp://admin:mypass@rabbitmq:5672')

@app.task
def publish(tweet):
    print('Publicando')
    make_tweet(tweet)
