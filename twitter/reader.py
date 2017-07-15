mport ugfx
import sys
import badge
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
    sleep(0.1)
    pass
   
def get_tweets(pushed):
    if(pushed):
        print("Downloading JSON...")
        gc.collect()
        try:
            data = requests.get("https://example/twitter.php")
        except:
            print("Could not download JSON!")
            sleep(1)
            return
        try:
            global tweets
            tweets = data.json()
        except:
            data.close()
            print("Could not decode JSON!")
            sleep(1)
            return
        data.close()

    print("Rendering list...")
    ugfx.clear(ugfx.WHITE)
    ugfx.flush()
    
    #get 1 tweet only, but possible to convert to scroll/something
    x=1 
    tweet_text = str(tweets['statuses'][x]['text'])
    ugfx.string(45,85,tweet_text,"Roboto_Black22",ugfx.BLACK)
    ugfx.flush()

def main()
    get_tweets(1)

def go_home(pushed):
    if(pushed):
        import machine
        machine.deepsleep(1)

ugfx.input_attach(ugfx.BTN_A, load_tickets)
ugfx.input_attach(ugfx.BTN_B,

main()
