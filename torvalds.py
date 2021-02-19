#!/usr/bin/env python3
# import libraries
from guizero import App, PushButton, Text
from picamera import PiCamera
from gpiozero import LED, CamJamKitRobot
from datetime import datetime

#setup the camera, LED and Robot
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25
devastator_eye = LED(25)
devastator_robot = CamJamKitRobot()

# Define the functions
def capture_camera():
    devastator_eye.on()
    moment = datetime.now()
    camera.start_recording("/home/pi/video_%02d_%02d_%02d.mjpg" % (moment.hour, moment.minute, moment.second))

def stop_record():
    devastator_eye.off()
    camera.stop_recording()

def direction_one():
    devastator_robot.forward()

def direction_two():
    devastator_robot.backward()


def direction_three():
    devastator_robot.left()

def direction_four():
    devastator_robot.right()

def stop():
    devastator_robot.stop()



# Define the app
app = App("PiCamera Recording")
app.bg = (45, 232, 225)
camera_text = Text(app, text="Camera recording", size = 20)
# Button to make the robot move forward
forward_button = PushButton(app, text = "forward", width=10)
forward_button.when_left_button_pressed = direction_one
forward_button.when_left_button_released = stop
forward_button.bg = "blue"
forward_button.text_size = 20
# Button to make the robot move backward
backward_button = PushButton(app, text = "backward", width=10, align="bottom")
backward_button.when_left_button_pressed = direction_two
backward_button.when_left_button_released = stop
backward_button.bg = "blue"
backward_button.text_size = 20
# Button to make the robot move left
left_button = PushButton(app, text = "left", width=10, align="left")
left_button.when_left_button_pressed = direction_three
left_button.when_left_button_released = stop
left_button.bg = "blue"
left_button.text_size = 20
# Button to make the robot move right
right_button = PushButton(app, text = "right", width=10, align ="right")
right_button.when_left_button_pressed = direction_four
right_button.when_left_button_released = stop
right_button.bg = "blue"
right_button.text_size = 20
# Create the buttons to record and stop recording
record = PushButton(app, command=capture_camera, text = "Record")
record.bg = "green"
record.text_size = 20
stop_button = PushButton(app, command=stop_record, text = "Stop")
stop.bg = "red"
stop.text_size = 20
# Display the app
app.display()

