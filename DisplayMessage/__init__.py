#based on Quick 'n Dirty Messenger App rev. 4 (by bear)

import ugfx
import network
import badge
import time
import socket

badge.init()
badge.vibrator_init()

TCP_PORT = 23
FONT = "DejaVuSans20"
FONT_IP = "Roboto_Black22"

sta_if = network.WLAN(network.STA_IF); sta_if.active(True) 
while not sta_if.isconnected():  
    sta_if.connect("SHA2017-insecure") 
    time.sleep(1)

BADGE_IP = sta_if.ifconfig()[0]
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((BADGE_IP, TCP_PORT))
s.listen(1)

MSG = "** Hi, send me a message at: " 
MSG2 = BADGE_IP + ":" + str(TCP_PORT)

while True:
    while not sta_if.isconnected():  
        sta_if.connect("SHA2017-insecure") 
        time.sleep(0.5)
    ugfx.clear(ugfx.WHITE)
    ugfx.string(0,0, MSG, FONT, ugfx.BLACK)
    ugfx.string(50,50, MSG2, FONT_IP, ugfx.BLACK)
    ugfx.flush()
    client_socket = s.accept()
    # vibrate when someone has connected
    badge.vibrator_activate(6)
    ugfx.clear(ugfx.WHITE)
    client_msg = "** " + str(client_socket[1][0]) + " is"
    client_msg2 = "** connected.."
    ugfx.string(0,0,client_msg, FONT, ugfx.BLACK)
    ugfx.string(0,20,client_msg2, FONT, ugfx.BLACK)
    ugfx.flush()
    client_socket[0].send('-----------------------------------------\n')
    client_socket[0].send('Leave your message ' + str(client_socket[1][0]) + ' :-)\n')
    try:
        output = client_socket[0].readline()
        ugfx.clear(ugfx.WHITE)
        ugfx.string(0,0,output,FONT,ugfx.BLACK)
        ugfx.flush()
        client_socket[0].send('Thanks! Bye!\n')
        client_socket[0].send('-----------------------------------------\n')
        client_socket[0].close()
        time.sleep(5)
    except:
        client_socket[0].close()
