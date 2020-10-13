from gpiozero import LED, Button
from signal import pause

def blink_led_1():
    led = LED(17)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

    pause()

def blink_led_2():
    led = LED(18)
    button = Button(3)

    led.source = button

    pause()
    
blink_led_1():
blink_led_2():
