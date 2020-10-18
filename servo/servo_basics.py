from gpiozero import Servo
from time import sleep

servo = Servo(17)

def min_mid_max(times = 10):
    for i in range(times):
        print('MIN')
        servo.min()
        sleep(2)
        
        print('MID')
        servo.mid()
        sleep(2)
        
        print('MAX')
        servo.max()
        sleep(2)


min_mid_max(2)