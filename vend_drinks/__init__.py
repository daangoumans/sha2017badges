import urequests as requests
import deepsleep
import wifi
import time
import badge
import ugfx

badge.init()
ugfx.init()
wifi.init()
badge.leds_init()
badge.vibrator_init()

ugfx.clear(ugfx.BLACK)
ugfx.flush()
ugfx.clear(ugfx.WHITE)
ugfx.flush()



def set_message(text):
  ugfx.clear(ugfx.BLACK)
  ugfx.clear(ugfx.WHITE)
  ugfx.string(10,60,text,"Roboto_Regular12", 0)
  ugfx.flush()
  badge.eink_busy_wait()
    
def home(pressed):
  if pressed:
    deepsleep.reboot()

def vendmate(pressed):
  if pressed:
    try:
      led_array = bytes([255, 0, 0, 100, 255, 0, 0, 100, 255, 0, 0, 100, 255, 0, 0, 100, 255, 0, 0, 100, 255, 0, 0, 100])
      badge.leds_enable()
      badge.leds_send_data(led_array,24)
      time.sleep(1)
      badge.leds_disable()
      badge.vibrator_activate(0xFF)
      set_message("U WOT MATE?!?!")
      url = "https://vendingmachineurl.url/api"
      h = {"Authorization":"Basic <base64 login string>"}
      data = requests.get(url, headers=h)
      data.close()
      set_message("Look at the vending machine")
    except Exception as e:
      set_message("Unexpected error: "+str(e))
      deepsleep.reboot()

def main():
    ugfx.clear(ugfx.WHITE)
    ugfx.string(5,50,"Free Mate @ Torvalds","Roboto_Regular12",ugfx.BLACK)
    ugfx.string(5,70,"When u get there, press A!","Roboto_Regular12",ugfx.BLACK)
    ugfx.flush()


set_message("Waiting for wifi")
while not wifi.sta_if.isconnected():
    time.sleep(0.1)
    pass
    
ugfx.input_init()
ugfx.input_attach(ugfx.BTN_A, vendmate)
ugfx.input_attach(ugfx.BTN_SELECT, home)
main()
