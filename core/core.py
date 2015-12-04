#!/usr/bin/env python

import tweepy
import random
import config

# Use: get_api()
def get_api():
	auth = tweepy.OAuthHandler(config.cfg['consumer_key'], config.cfg['consumer_secret'])
	auth.set_access_token(config.cfg['access_token'], config.cfg['access_token_secret'])
	return tweepy.API(auth)

# Use: get_current_tweet()
def get_current_tweet(api, user):
	current_status = api.user_timeline(user)
	return current_status[0].text

# Use: get_current_tweet_id()
def get_current_tweet_id(api, user):
	current_status = api.user_timeline(user)
	return current_status[0].id_str

# Use: reply(user, answer)
# Replies to a certain status
def reply(api, user, answer):
	api.update_status('@'+user+' '+answer, in_reply_to_status_id=get_current_tweet_id(user))

# Use: reply_from_file(user_,file)
# Replies to a certain status with a random line of a file. File must exist.
def reply_from_file(api, user, file):
	with open(file) as f:
		lines = f.readlines()
	api.update_status('@'+user+' '+random.choice(lines), in_reply_to_status_id=get_current_tweet_id(user))

# Use: get_mentions(user, since)
# Gets mentions from a certain ID
def get_mentions(api, user, since):
	try:
		mentions = api.mentions_timeline(since_id=since)
		return mentions

	except tweepy.TweepError as api_error:
        	# quit on rate limit errors
                if "rate limit" in str(api_error).lower():
                    print 'You have been rate limited. Wait a while before running the bot again'
                    return

# Use: get_last_mention(user)
# Return the entire object. (Tweet = mentions.text)
def get_last_mention(api, user):
	mentions = api.mentions_timeline(count=1)
	return mentions[0]

