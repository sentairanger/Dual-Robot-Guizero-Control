# import libraries
from guizero import App, PushButton, Text
from picamera import PiCamera
from gpiozero import LED
# This is imported to create a timestamp for the video
from datetime import datetime

#setup the camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
devastator_eye = LED(25)

# Define the functions
def capture_camera():
    devastator_eye.on()
    moment = datetime.now()
    camera.start_recording("/home/pi/video_%02d_%02d_%02d.mjpg" % (moment.hour, moment.minute, moment.second))

def stop_record():
    devastator_eye.off()
    camera.stop_recording()

# Define the app
app = App("PiCamera Recording")
app.bg = (45, 232, 225)
camera_text = Text(app, text="Camera recording", size = 20)
# Create the buttons to record and stop recording
record = PushButton(app, command=capture_camera, text = "Record")
record.bg = "green"
record.text_size = 20
stop = PushButton(app, command=stop_record, text = "Stop")
stop.bg = "red"
stop.text_size = 20
# Display the app
app.display()
