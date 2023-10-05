from guizero import App, PushButton, Box, Window, Text, Slider
from gpiozero import Robot, LED, PWMOutputDevice, AngularServo
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from datetime import datetime
from gpiozero.pins.pigpio import PiGPIOFactory

#set variable for robots, servos, factory and eyes
devastator_robot = Robot(left=(13, 21), right=(17, 27))
eye = LED(25)

factory = PiGPIOFactory(host='192.168.0.28')

linus = Robot(left=(13, 21), right=(17, 27), pin_factory=factory)
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
eye_2 = LED(16, pin_factory=factory)
servo = AngularServo(22, min_angle = -90, max_angle = 90, pin_factory=factory)
servo_two = AngularServo(23, min_angle = -90, max_angle = 90, pin_factory=factory)

# Define the new camera and the configurations
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
moment = datetime.now()

# Define the movements, speed control and servo control
def forward():
    devastator_robot.forward()

def backward():
    devastator_robot.backward()

def left():
    devastator_robot.left()

def right():
    devastator_robot.right()
    
def stop():
    devastator_robot.stop()

def north():
    linus.forward()

def south():
    linus.backward()

def west():
    linus.left()

def east():
    linus.right()

def stop_2():
    linus.stop()
    
def speed_control(slider_value):
    en_1.value = int(slider_value) / 10
    en_2.value = int(slider_value) / 10

def servo_movement(slider_value):
    servo.angle = int(slider_value)
    
def servo_movement_2(slider_value):
    servo_two.angle = int(slider_value)
    

def eye_on():
    eye.on()

def eye_off():
    eye.off()

def linus_on():
    eye_2.on()

def linus_off():
    eye_2.off()

#Define the record and stop_record functions
def record():
    print("recording!")
    eye.on()
    picam2.start_recording(encoder, '/home/torvalds/Videos/robot_gui_video2_%02d_%02d_%02d.h264' % (moment.hour, moment.minute, moment.second))

def stop_record():
    eye.off()
    print("stop recording!")
    picam2.stop_recording()

# Define the app
app = App(title='Updated Robot Control', layout='grid')
app.bg = (51, 246, 255)
# Add a camera window
camera_window = Window(app, "Updated Camera Control")
camera_window.bg = (51, 246, 255)
# Add the boxes for placing the widgets
center_box = Box(app, layout="grid", grid=[2,0])
center_box_2 = Box(app, layout="grid", grid=[3,0])
center_box_3 = Box(app, layout="grid", grid=[2,1])
center_box_4 = Box(app, layout="grid", grid=[3,1])
#Define the buttons
forward_button = PushButton(center_box, text='^', grid=[1,0])
left_button = PushButton(center_box, text='<', grid=[0,1])
blink_button = PushButton(center_box, text='O', grid=[1,1])
right_button = PushButton(center_box, text='>', grid=[2,1])
backward_button = PushButton(center_box, text='v', grid=[1,2])
forward_button_2 = PushButton(center_box_2, text='^', grid=[1,0])
left_button_2 = PushButton(center_box_2, text='<', grid=[0,1])
blink_button_2 = PushButton(center_box_2, text='O', grid=[1,1])
right_button_2 = PushButton(center_box_2, text='>', grid=[2,1])
backward_button_2 = PushButton(center_box_2, text='v', grid=[1,2])
camera_text = Text(camera_window, text="Camera Controls")
record_button = PushButton(camera_window, text="record", command=record)
stop_button = PushButton(camera_window, text="stop", command=stop_record)
# Sliders
speed_slider = Slider(center_box_3, start=0, end=10, grid=[0,0], command=speed_control)
servo_slider = Slider(center_box_4, start=-90, end=90, grid=[0,0], command=servo_movement)
servo_slider_2 = Slider(center_box_4, start=-90, end=90, grid=[0,1], command=servo_movement_2)
# Torvalds buttons
forward_button.text_size = 20
forward_button.bg = "red"
backward_button.text_size = 20
backward_button.bg = "red"
left_button.text_size = 20
left_button.bg = "red"
right_button.text_size = 20
right_button.bg = "red"
blink_button.text_size = 20
blink_button.bg = "red"
record_button.text_size = 20
record_button.bg = "green"
stop_button.text_size = 20
stop_button.bg = "red"
camera_text.text_size = 20
#Linus Buttons
forward_button_2.text_size = 20
forward_button_2.bg = "green"
backward_button_2.text_size = 20
backward_button_2.bg = "green"
left_button_2.text_size = 20
left_button_2.bg = "green"
right_button_2.text_size = 20
right_button_2.bg = "green"
blink_button_2.text_size = 20
blink_button_2.bg = "green"
# camera buttons
record_button.text_size = 20
record_button.bg = "green"
stop_button.text_size = 20
stop_button.bg = "red"
camera_text.text_size = 20
# sliders
speed_slider.bg = "magenta"
servo_slider.bg = "yellow"
servo_slider_2.bg = "yellow"
# Torvalds Commands
forward_button.when_left_button_pressed = forward
forward_button.when_left_button_released = stop
backward_button.when_left_button_pressed = backward
backward_button.when_left_button_released = stop
left_button.when_left_button_pressed = left
left_button.when_left_button_released = stop
right_button.when_left_button_pressed = right
right_button.when_left_button_released = stop
blink_button.when_left_button_pressed = eye_on
blink_button.when_left_button_released = eye_off
# Linus Commands
forward_button_2.when_left_button_pressed = north
forward_button_2.when_left_button_released = stop_2
backward_button_2.when_left_button_pressed = south
backward_button_2.when_left_button_released = stop_2
left_button_2.when_left_button_pressed = west
left_button_2.when_left_button_released = stop_2
right_button_2.when_left_button_pressed = east
right_button_2.when_left_button_released = stop_2
blink_button_2.when_left_button_pressed = linus_on
blink_button_2.when_left_button_released = linus_off

app.display()
