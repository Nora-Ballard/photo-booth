from guizero import App, Text, TextBox, PushButton, Picture
from picamera import PiCamera
import time 

def shutter_press():
    camera.start_preview()
    start_countdown(5)
    camera.capture(photo_path, format="png")
    photo_display.value = photo_path
    photo_display.show()
    camera.stop_preview()

def start_countdown(seconds):
    photo_display.hide()
    countdown.value = "{0}".format(seconds)
    countdown.show()

    starting_time = time.time()

    while (time.time() - starting_time) < seconds:
        print(countdown.value)
        countdown.value = "{0}".format((time.time() - starting_time))
        time.sleep(1)

    countdown.hide()

def show_preview():
    camera.start_preview()
    time.sleep(480)
    camera.stop_preview()


camera = PiCamera()
photo_path = '/home/pi/Desktop/PhotoBooth/image.png'

app = App(title="Pride Camera")

shutter = PushButton(app, command=shutter_press, text="Take Picture")
preview_mode = PushButton(app, command=show_preview, text="Preview Mode")

countdown = Text(app)
countdown.hide()

photo_display = Picture(app)
photo_display.hide()

app.display()

