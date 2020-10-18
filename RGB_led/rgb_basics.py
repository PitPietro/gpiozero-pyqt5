from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

def rainbow(s_time):
    
    led.color = (0, 0, 0)
    print('Slowly increase intensity')
    prec = 10
    for i in range(prec):
        tmp_color = i/prec
        led.green = tmp_color
        print('value', tmp_color)
        sleep(0.2)
    
    led.color = (0, 0, 0)
    
    led.red = 0.5
    print('HALF Red: 7F0000')
    sleep(s_time / 2)
    
    print('Red: #FF0000')
    led.red = 1
    sleep(s_time)
    
    print('Orange: #ffa500')
    led.color = (1, 0.95, 0)
    sleep(s_time)
    
    print('Yellow: #fafa37')
    led.color = (0.9842, 0.9842, 0.2165)
    sleep(s_time)
    
    print('Green: #00ff00')
    led.color = (0, 1, 0)
    sleep(s_time)
    
    print('Blue: #0000ff')
    led.color = (0, 0, 1)
    sleep(s_time)
    
    print('Indigo: #4b0082')
    led.color = (0.2953, 0, 0.5118)
    sleep(s_time)
    
    print('Violet: #8f00ff')
    led.color = (0.5630, 0, 1)
    sleep(s_time)
    
    print('OFF: #000000')
    led.color = (0, 0, 0)
    sleep(s_time)
    
    led.color = (0, 0, 0)


rainbow(5)
