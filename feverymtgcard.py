import tweepy
import datetime
from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

file = open("acting_card_list.txt","r")

cards = file.read().splitlines()

card = cards.pop(0)

tweet_content = "Fuck " + card

tweet = api.update_status(tweet_content)

new_file = open("acting_card_list.txt","w")
for line in cards:
	new_file.write(line + "\n")

log = open("log_tweets.txt","a")
log.write(str(datetime.datetime.now()) + ": " + card)