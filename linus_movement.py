# import the libraries
from guizero import App, Text, PushButton, Slider, Window
from gpiozero import Robot, LED, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

# Define the app
robot_movement = App("Linus Movement")
servo_window = Window(app, "Servo Control")
# Background color
robot_movement.bg = (88, 255, 51)
# Define the factory
# Insert IP address here
factory = PiGPIOFactory(host='')
# Define the robot
linus = Robot(left=(13, 21), right=(17,27), pin_factory = factory)
# Define the LED that will be used for the eye
eye = LED(16, pin_factory=factory)
#Define the servos
servo = AngularServo(22, min_angle = -90, max_angle = 90, pin_factory=factory)
servo_two = AngularServo(23, min_angle = -90, max_angle = 90, pin_factory=factory)

# Define the directions and the eye

def direction_one():
    linus.forward()

def direction_two():
    linus.backward()


def direction_three():
    linus.left()

def direction_four():
    linus.right()

def stop():
    linus.stop()


def linus_eye():
    eye.on()

def linus_off():
    eye.off()

def servo_movement(slider_value):
    servo.angle = int(slider_value)

def servo_two_movement(slider_value):
    servo_two.angle = int(slider_value)


# This is the title text
robot_text = Text(robot_movement, text="Linus Movement", size=20)
# Button to make the robot move forward
forward_button = PushButton(robot_movement, text = "forward", width=10)
forward_button.when_left_button_pressed = direction_one
forward_button.when_left_button_released = stop
forward_button.bg = "blue"
forward_button.text_size = 20
#Define the servo sliders
servo_text = Text(servo_window, text = "Servo Angular Movement", size=20)
slider_one_text = Text(servo_window, text = "servo one")
slider = Slider(servo_window, start = -90, end = 90, command=servo_movement)
slider.bg = "aqua"
slider_two_text = Text(servo_window, text = "servo two")
slider_two = Slider(servo_window, start = -90, end = 90, command=servo_two_movement)
slider_two.bg = "aqua"
# Button to make the robot move backward
backward_button = PushButton(robot_movement, text = "backward", width=10, align="bottom")
backward_button.when_left_button_pressed = direction_two
backward_button.when_left_button_released = stop
backward_button.bg = "blue"
backward_button.text_size = 20
# Button to make the robot move left
left_button = PushButton(robot_movement, text = "left", width=10, align="left")
left_button.when_left_button_pressed = direction_three
left_button.when_left_button_released = stop
left_button.bg = "blue"
left_button.text_size = 20
# Button to make the robot move right
right_button = PushButton(robot_movement, text = "right", width=10, align ="right")
right_button.when_left_button_pressed = direction_four
right_button.when_left_button_released = stop
right_button.bg = "blue"
right_button.text_size = 20
# Turns the LED on and off when released
linus_button = PushButton(robot_movement, linus_eye, text = 'eye on', width = 10)
linus_button.when_left_button_pressed = linus_eye
linus_button.when_left_button_released = linus_off
linus_button.bg = "green"
linus_button.text_size = 20

# Displays the app
robot_movement.display()
