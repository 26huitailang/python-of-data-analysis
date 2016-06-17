#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo
from pandas import DataFrame

con = pymongo.MongoClient('localost', port=27017) # pymongo has no attribution Connection but MongoClient

tweets = con.db.tweets

import requests, json
url = 'http://search.twitter.com/search.json?q=python%20pandas'
data = json.loads(requests.get(url).text)

for tweet in data['results']:
    tweets.save(tweet)

cursor = tweet.find({'from_user': 'wesmckinn'})
tweet_fields = ['created_at', 'from_user', 'id', 'text']
result = DataFrame(list(cursor), columns=tweet_fields)