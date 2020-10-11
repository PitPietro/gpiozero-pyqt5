from picamera import PiCamera
from time import sleep


def take_photo(sec):
    pi_cam = PiCamera()
    pi_cam.start_preview()
    sleep(sec)
    pi_cam.capture('./test.jpg')
    pi_cam.stop_preview()


take_photo(5)