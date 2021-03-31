# import libraries
from guizero import App, PushButton, Slider, Text, Window
from gpiozero import OutputDevice, PWMOutputDevice, AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

#Define the app and window for the servo sliders
app = App("Dual Robot Control", layout='grid')
servo_window = Window(app, "Servo Movement and PWM")
servo_window.bg = (51, 165, 255)
app.bg = (51, 246, 255)

#Define the factories
factory = PiGPIOFactory(host='')
factory2 = PiGPIOFactory(host='')

# Define both robots
en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)


# Define the servos
servo = AngularServo(22, min_angle = -90, max_angle = 90, pin_factory=factory)
servo_two = AngularServo(23, min_angle = -90, max_angle = 90, pin_factory=factory)

# Define the functions
# Forwards
def direction_one():
    motor_in1.on()
    motor_in2.off()
    motor_in3.on()
    motor_in4.off()

# backwards
def direction_two():
    motor_in1.off()
    motor_in2.on()
    motor_in3.off()
    motor_in4.on()

#right
def direction_three():
    motor_in1.on()
    motor_in2.off()
    motor_in3.off()
    motor_in4.on()

#left
def direction_four():
    motor_in1.off()
    motor_in2.on()
    motor_in3.on()
    motor_in4.off()

def stop():
    motor_in1.off()
    motor_in2.off()
    motor_in3.off()
    motor_in4.off()


# Forwards
def north():
    pin1.on()
    pin2.off()
    pin3.on()
    pin4.off()

# backwards
def south():
    pin1.off()
    pin2.on()
    pin3.off()
    pin4.on()

#right
def east():
    pin1.on()
    pin2.off()
    pin3.off()
    pin4.on()

#left
def west():
    pin1.off()
    pin2.on()
    pin3.on()
    pin4.off()

def stop_two():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()

def servo_movement(slider_value):
    servo.angle = int(slider_value)

def servo_two_movement(slider_value):
    servo_two.angle = int(slider_value)

def pwm_one(slider_value):
    en_1.value = int(slider_value) / 10

def pwm_two(slider_value):
    en_2.value = int(slider_value) / 10

# Define the buttons for movement
# Forward button for Linus
button1 = PushButton(app, text="f", grid=[0,0])
button1.text_size = 20
button1.bg = "green"
button1.when_left_button_pressed = direction_one
button1.when_left_button_released = stop
#Backward Button for Linus
button2 = PushButton(app, text="b", grid=[1,0])
button2.text_size = 20
button2.bg = "green"
button2.when_left_button_pressed = direction_two
button2.when_left_button_released = stop
# Forward button for Torvalds
button3 = PushButton(app, text="n", grid=[2,0])
button3.text_size = 20
button3.bg = "red"
button3.when_left_button_pressed = north
button3.when_left_button_released = stop_two
# Backward button for Torvalds
button4 = PushButton(app, text="s", grid=[3,0])
button4.text_size = 20
button4.bg = "red"
button4.when_left_button_pressed = south
button4.when_left_button_released = stop_two
# left button for Linus
button5 = PushButton(app, text="l", grid=[0,1])
button5.text_size = 20
button5.bg = "green"
button5.when_left_button_pressed = direction_three
button5.when_left_button_released = stop
# Right button for Linus
button6 = PushButton(app, text="r", grid=[1,1])
button6.text_size = 20
button6.bg = "green"
button6.when_left_button_pressed = direction_four
button6.when_left_button_released = stop
# Right button for torvalds
button7 = PushButton(app, text="e", grid=[2,1])
button7.text_size = 20
button7.bg = "red"
button7.when_left_button_pressed = east
button7.when_left_button_released = stop_two
# Left button for torvalds
button8 = PushButton(app, text="w", grid=[3,1])
button8.text_size = 20
button8.bg = "red"
button8.when_left_button_pressed = west
button8.when_left_button_released = stop_two
# Sliders to control the servos and pwm
servo_slider1 = Slider(servo_window, start=-90, end=90, command=servo_movement)
servo_slider1.bg = "magenta"
servo_slider2 = Slider(servo_window, start=-90, end=90, command=servo_two_movement)
servo_slider2.bg = "magenta"
slider_three = Slider(servo_window, start=0, end=10, command=pwm_one)
slider_three.bg = "aqua"
slider_four = Slider(servo_window, start=0, end=10, command=pwm_two)
slider_four.bg = "aqua"
# display the App
app.display()