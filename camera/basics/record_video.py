from picamera import PiCamera
from time import sleep


def record_video(sec):
    pi_cam = PiCamera()
    pi_cam.start_preview()
    pi_cam.start_recording('./video.mp4')
    sleep(sec)
    pi_cam.stop_recording()
    pi_cam.stop_preview()


record_video(5)
