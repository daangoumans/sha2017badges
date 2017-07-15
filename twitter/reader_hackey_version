import sys
import json
import gc
import time
import requests

def get_tweets(pushed,number):
    if(pushed):
        gc.collect()
        try:
            data = requests.get("https://example.com/sha2017/index.php")
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
    for x in range(0, 20):
        tweet_user = "@" + str(tweets['statuses'][x]['user']['screen_name'].encode("utf-8"))
        tweet_text = str(tweets['statuses'][x]['text'].encode("utf-8"))
        tweet_array.append(str(tweet_user+"\r\n"+tweet_text))
    return tweet_array[number]

def main(number):
    if(number.isdigit()):
        tweet_number = int(number)
        if 0 <= tweet_number <= 19:
            print(get_tweets(1,tweet_number))
        else:
            print "Please insert a number between 0 and 19"

if len(sys.argv) < 2:
    print "Usage: python reader.py #0-19"
else:
    number = sys.argv[1]
    main(number)
