from gpiozero import LED
from time import sleep

def led_blink_1():
    my_led = LED(17)

    while True:
        my_led.on()
        print('ON')
        sleep(1)
        my_led.off()
        print('OFF')
        sleep(1)


led_blink_1()