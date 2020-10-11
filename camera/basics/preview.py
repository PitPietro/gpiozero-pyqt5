from picamera import PiCamera
from time import sleep


def preview_photo(sec):
    pi_cam = PiCamera()
    pi_cam.start_preview()
    sleep(sec)
    pi_cam.stop_preview()


preview_photo(20)