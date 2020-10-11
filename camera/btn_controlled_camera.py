from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause


def capture():
    prev_btn = Button(2)
    photo_btn = Button(3)
    my_cam = PiCamera()
    
    timestamp = datetime.now().isoformat()
    my_cam.capture('./%s.jpg' % timestamp)
    
    prev_btn.when_pressed = my_cam.start_preview
    prev_btn.when_released = my_cam.stop_preview
    photo_btn.when_pressed = capture

    pause()


capture()
