# sha2017badges

Namebadge.py = a simple logo, name, company badge example

twitter/reader.py = a twitter reader for on your badge (display's newest tweet only for now) <- UNTESTED

Needs the following code:

ugfx.input_init() #Needs badge.init() and ugfx.init()

ugfx.input_attach(button, callback) #The callback has one boolean argument, pressed.

ugfx.input_attach(ugfx.JOY_UP, lambda pressed: print(pressed)) #This example attaches a simple print function to the UP button, showing True for press and False for release.



https://wiki.sha2017.org/w/Projects:Badge/MicroPython
