import os
import csv
import sys
import pkgutil
import subprocess
import re
from datetime import datetime,date,time, timedelta
import logging
import time


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer, SimpleClient
from values import access_token, access_token_secret, consumer_key, consumer_secret

access_token = access_token
access_token_secret = access_token_secret
consumer_key = consumer_key
consumer_secret = consumer_secret


kafka_client = SimpleClient("127.0.0.1:9092")
#kafka = KafkaClient("PLAINTEXT://localhost:9092")
#producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092')
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10))
# producer = KafkaProducer()


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        producer.send("modi", data.encode('utf-8'))
        return True

    def on_error(self, status):
        print(status)


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['Kaala'])





