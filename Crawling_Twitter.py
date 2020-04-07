#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import json


# In[8]:


access_token = "xxx"
access_token_secret = "xxxxx"
consumer_key = "xxxxxxxxxxxxx"
consumer_secret = "Xxxxxx"


# In[9]:


class StdoutListener(StreamListener):
    def on_data(self,data):
        try:
            data = json.loads(data)
            tweet = data['text']
            with open('tweet.csv', 'a', encoding='utf-8') as f:
                saveFile = open('gabung.csv','a')
                f.write(tweet)
                f.write('\n')
                f.close()
            return True
        except BaseException as e:
            print('Failed'(e))
        
        def on_error(self_status):
            print(status)


# In[10]:


#streaming
l = StdoutListener()
auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
stream = Stream(auth,l)
stream.filter(track=['nonton'])


# In[ ]:





# In[ ]:




