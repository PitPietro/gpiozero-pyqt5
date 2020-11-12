import os
# from signal import pause
from gpiozero import Button
from datetime import datetime

def take_screen():
    screen_btn = Button(2)
    
    while True:
        if screen_btn.is_pressed:
            timestamp = datetime.now()
            cmd = "scrot -u d 5 $n {}.png".format('screen_' + str(timestamp))
            os.system(cmd)
    
    #screen_btn.when_pressed=os.system(cmd)
    #pause()
    

take_screen()    
    