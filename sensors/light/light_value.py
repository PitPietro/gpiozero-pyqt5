from gpiozero import LightSensor, PWMLED
from signal import pause
from time import sleep


def main():
    sensor = LightSensor(18)
    while True:
        print('sensor: ', sensor)
        sleep(0.5)
        pause()

main()