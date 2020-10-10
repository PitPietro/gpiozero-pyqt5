from gpiozero import LED
from signal import pause

def led_blink_2():
    my_led = LED(5)
    my_led.blink()
    pause()


led_blink_2()