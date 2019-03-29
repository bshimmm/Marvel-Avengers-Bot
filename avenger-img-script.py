import tweepy
import time
import os

consumer_key = 'AhvCZn4meETltBcQsYNrFk4nw'
consumer_secret = 'goGUdUb3Z8VgUE8cygqTEAdflQ5TZVe9R8pBuZzy7bg6XdsMoy'
access_token = '1110252920770043908-LaqSnBj6qJ2SqSQLbEMEqRYbjVEj8l'
access_token_secret = 'Md2HdObyXGUe33LIhPfVCm22edx68Wnj7ElZRmCLbewL3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)

"""
iterates over images in get-avengers folder
"""
os.chdir('avengers')
for avenger_img in os.listdir('.'):
	api.update_with_media(avenger_img)
	time.sleep(15*60)