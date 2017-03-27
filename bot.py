#!/usr/bin/env python

import tweepy

# from our keys module (keys.py), import the keys dictionary
from keys import keys


CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# SIMPLE #

query = '"radhika"'

tweet_list = api.search(
	q=query,
	count=5,
	lang="en"
)

for tweet in tweet_list:
	screen_name = tweet.user.screen_name

	message = ".@{username} {message}".format(
		username=screen_name,
		message='Hi I''m a Twitter Bot!'
	)

	try:
		api.update_status(
			status=message,
			in_reply_to_status_id=tweet.id
		)
		print message

	except tweepy.TweepError as e:
		print e.message


# ADVANCED #

# ALOT_HERD = [
# 	# ['"exact string to search"', 'tweet response']
# 	['"alot of bacon"', 'You just summoned Alot of bacon!'],
# 	['"alot of beer"', 'You just summoned Alot of beer!'],
# 	['"alot of fire"', 'You just summoned Alot of fire!'],
# 	['"alot of mist"', 'You just summoned Alot of mist!'],
# 	['"alot of money"', 'You just summoned Alot of money!'],
# ]

# for alot in ALOT_HERD:

# 	query = alot[0]

# 	tweet_list = api.search(q=query, count=5, lang="en")

# 	for tweet in tweet_list:

# 		screen_name = tweet.user.screen_name

# 		message = ".@{username} {message}".format(
# 			username=screen_name,
# 			message=alot[1]
# 			)
# 		try:
# 			api.update_status(
# 				status=message,
# 				in_reply_to_status_id=tweet.id
# 				)
# 			print message

# 		except tweepy.TweepError as e:
# 			print e.message[0]['code']
# 			print e.args[0][0]['code']
