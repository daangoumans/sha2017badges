import ugfx
import badge
import dialogs
import json
import wifi
import gc
import deepsleep
import network
import urequest as request
from time import *

badge.eink_init()
ugfx.init()
wifi.init()

ugfx.clear(ugfx.WHITE);
ugfx.string(10,10,"Waiting for wifi...","Roboto_Regular12", 0)
ugfx.flush()

# Wait for WiFi connection
while not wifi.sta_if.isconnected():
    time.sleep(0.1)
    pass

ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()

input_string = badge.nvs_get_str("Hashtag", "hashtag", "")
hashtag = dialogs.prompt_text("What hashtag should we display?", input_string)
if hashtag:
  badge.nvs_set_str("Hashtag", "hashtag", hashtag)

tweets = []
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

tweets = get_tweets(hashtag)

x=0
def display_next(tweets,pressed):
    if (pressed):
        ugfx.clear(ugfx.WHITE)
        tweet_text = str(tweets[x])
        ugfx.string(45,85,tweet_text,"Roboto_Black22",ugfx.BLACK)
        ugfx.flush()
        x=x+1

def passout():
    exit()

display_next(tweets,0)
ugfx.input_init()
ugfx.input_attach(ugfx.BTN_A, lambda pressed: display_next(tweets,pressed))
ugfx.input_attach(ugfx.BTN_SELECT, lambda pressed: passout())

while True:
    pass
