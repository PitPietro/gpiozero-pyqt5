from gpiozero import LED, Button
from signal import pause

def blink_led():
    led_1 = LED(17)
    led_2 = LED(18)
    
    btn_1 = Button(2)
    btn_2 = Button(3)

    btn_1.when_pressed = led_1.on
    btn_1.when_released = led_1.off

    led_2.source = button
    
    pause()

    
blink_led():
