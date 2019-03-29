import tweepy
import time
import os
from tkinter import *

consumer_key = 'AhvCZn4meETltBcQsYNrFk4nw'
consumer_secret = 'goGUdUb3Z8VgUE8cygqTEAdflQ5TZVe9R8pBuZzy7bg6XdsMoy'
access_token = '1110252920770043908-LaqSnBj6qJ2SqSQLbEMEqRYbjVEj8l'
access_token_secret = 'Md2HdObyXGUe33LIhPfVCm22edx68Wnj7ElZRmCLbewL3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

"""
Looping through the account's followers and following each one back
"""
for follower in tweepy.Cursor(api.followers).items():
	follower.follow()
	
print("Followed everyone that is following " + user.name)

"""
Creating a GUI application that will take our inputs of the keyword we would like to search for and favorite the tweet
"""

root = Tk()
label_1 = Label(root, text="Search")
#label_1.grid(row=0)
e1 = Entry(root, bd = 4)

label_2 = Label(root, text="# of Tweets")
#label_2.grid(row=1)
e2 = Entry(root, bd = 4)

label_3 = Label(root, text="Response")
#label_3.grid(row=2)
e3 = Entry(root, bd = 4)

label_4 = Label(root, text="Reply")
#label_4.grid(row=3)
e4 = Entry(root, bd = 4)

label_5 = Label(root, text="Retweet")
#label_5.grid(row=4)
e5 = Entry(root, bd = 4)

label_6 = Label(root, text="Favorite")
#label_6.grid(row=5)
e6 = Entry(root, bd = 4)

label_7 = Label(root, text="Follow")
#label_7.grid(row=6)
e7 = Entry(root, bd = 4)


def get_e1():
	return e1.get()

def get_e2():
	return e2.get()

def get_e3():
	return e3.get()

def get_e4():
	return e4.get()

def get_e5():
	return e5.get()

def get_e6():
	return e6.get()

def get_e7():
	return e7.get()





"""
This program is a twitter bot to favorite and reply to tweets that mention certain keywords
Tweepy docs: http://docs.tweepy.org/en/3.7.0/
"""

def main():
	get_e1()
	search = get_e1()

	get_e2()
	numOfTweets = get_e2()
	numOfTweets = int(numOfTweets)

	get_e3()
	response = get_e3()

	get_e4()
	reply = get_e4()

	get_e5()
	retweet = get_e5()

	get_e6()
	favorite = get_e6()

	get_e7()
	follow = get_e7()

	if reply == "yes":
		for tweet in tweepy.Cursor(api.search, search).items(numOfTweets):
			try:
				print('\nTweet by: @' + tweet.user.screen_name)
				print('Twitter ID: @' + str(tweet.user.id))
				tweetId = tweet.user.id
				username = tweet.user.screen_name
				api.update_status("@" + username + " " + response, in_reply_to_status_id = tweetId)
				print("Replied with " + response)

			except tweepy.TweepError as e:
				print(e.reason)

			except StopIteration:
				break

	if retweet == "yes":
		for tweet in tweepy.Cursor(api.search, search).items(numOfTweets):
			try:
				tweet.retweet()
				print('Retweeted the tweet')

			except tweepy.TweepError as e:
				print(e.reason)

			except StopIteration:
				break

	if favorite == "yes":
		for tweet in tweepy.Cursor(api.search, search).items(numOfTweets):
			try:
				tweet.favorite()
				print('Favorited the tweet')

			except tweepy.TweepError as e:
				print(e.reason)

			except StopIteration:
				break

	if follow == "yes":
		for tweet in tweepy.Cursor(api.search, search).items(numOfTweets):
			try:
				tweet.user.follow()
				print('Followed the twitter user')

			except tweepy.TweepError as e:
				print(e.reason)

			except StopIteration:
				break

submit = Button(root, text = "Submit", command = main)

label_1.pack()
e1.pack()

label_2.pack()
e2.pack()

label_3.pack()
e3.pack()

label_4.pack()
e4.pack()

label_5.pack()
e5.pack()

label_6.pack()
e6.pack()

label_7.pack()
e7.pack()

submit.pack(side=BOTTOM)

root.mainloop()

