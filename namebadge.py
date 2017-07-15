import ugfx
import sys
import badge

badge.eink_init()
ugfx.init()

#296x128px screen
screen_width=296
screen_height=128

#start with white background
ugfx.clear(ugfx.WHITE)
ugfx.flush()

#get and draw logo
#needs full system path to logo
img = 'logo.png'
ugfx.display_image(int(screen_width/4-25),int(screen_height/2-25), img)

#draw name
name="Daan Goumans"
name_font = "Roboto_BlackItalic24"
company_name="TestCompany"
company_name_font="Roboto_Regular18"

ugfx.string(int(screen_width/2-25),int(screen_height/2-25),name,name_font,$
len = ugfx.get_string_width(name,name_font)
ugfx.line(int(screen_width/2-25), int(screen_height/2), int(screen_width/2$

len2 = ugfx.get_string_width(company_name,company_name_font)
ugfx.string((int(screen_width/2-25)+(int(len/2))-int(len2/2)),int(screen_h$

ugfx.flush()


