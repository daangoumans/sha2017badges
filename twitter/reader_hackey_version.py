import sys
import json
import gc
import time
import requests

def get_tweets(hashtag):
	gc.collect()
	try:
		data = requests.get("http://server/html/twitter/get.php?hashtag="+hashtag)
	except:
		print("Could not download JSON!")
		time.sleep(1)
		return
	try:
		global tweets
		tweets = data.json()
	except:
		data.close()
		print("Could not decode JSON!")
		time.sleep(1)
		return
	
	data.close()
	x=0
	tweet_array = []
	amount =  len(tweets['statuses'])
	if amount >= 1:
		for x in range(0,amount):
			tweet_user = "@" + str(tweets['statuses'][x]['user']['screen_name'].encode("utf-8"))
			tweet_text = str(tweets['statuses'][x]['text'].encode("utf-8"))
			tweet_array.append(str(tweet_user+"\r\n"+tweet_text))
		return tweet_array
	else:
		tweet_array.append("try another hashtag")
		return tweet_array

def loop_through_tweets(array_of_tweets):
	for index, tweet in enumerate(array_of_tweets):
		#print "-----------------"
		#print index
		#print "-----"
		print tweet
		time.sleep(0.1)

def main(hashtag):
	tweets = get_tweets(hashtag)
	loop_through_tweets(tweets)

if len(sys.argv) > 1:
	hashtag = sys.argv[1]
	main(hashtag)
else:
	main('')
