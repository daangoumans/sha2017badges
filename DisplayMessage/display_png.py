import urequests, appglue, ugfx, badge, easydraw, wifi, time

easydraw.msg('', 'waiting for wifi')

wifi.init()
while not wifi.sta_if.isconnected():
    time.sleep(0.1)

req = urequests.get('')
ugfx.clear()
badge.eink_png(0,0,req.content)
ugfx.flush()
req.close()

while True:
	ugfx.input_attach(ugfx.BTN_SELECT, lambda x: appglue.home() if x else '')
