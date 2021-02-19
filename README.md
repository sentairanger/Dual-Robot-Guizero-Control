# Dual-Robot-Guizero-Control

## Introduction

This project was conceived of after I learned about guizero from the `Create Graphical User Interfaces with Python` by Martin O'Hanlon and Laura Sach. I tried out the examples in the book and then did some of my own GUIs to control LEDs and servo motors. After that I scaled up to my robots and here I will show you the full process of everything I did. 

## Getting Started

To begin with first I will explain the hardware and software I used for the project. 

### Hardware

Here is the list of supplies I used:

* My robot Torvalds (I used this robot from previous projects in my other GitHub Repos)
* My robot Linus: The list of materials can be found on the `linus_materials.txt`file
* A PC to control both robots (In my initial tests I used my Acer Aspire One 725 but moved to my Raspberry Pi 4)

### Software

Here is the software I used. Python modules are mentioned here:

* Raspberry Pi OS (Raspberry Pi 4)
* Raspberry Pi OS Lite (Linus)
* Raspbian Buster (Torvalds)
* Manjaro Linux (Acer Aspire One 725 for initial tests)
* Python modules `guizero`, `pigpio`, and `gpiozero`. For `gpiozero` I had to run this command to get the motors working since the current version does not work for motors: `sudo pip3 install https://bennuttall.com/files/gpiozero-1.5.2b1-py2.py3-none-any.whl`. 
* On Torvalds I had to enable the Pi Camera for the final step of the project. I also enabled VNC since `guizero` code cannot run in the terminal. 
* VNC Viewer (Raspberry Pi 4)

## Code Explanation

* `dual_improved_movement.py`: Here, the robots move using `guizero` and `gpiozero`. In order to connect to each robot remotely I had to use `gpiozero.pins.pigpio` to allow remote connections to the GPIO pins. The `guizero` windows are used to not just control the motors but also the servo arm. This code can run on any PC as long as the python modules are installed. Also to enable `pigpio` on both robots I had to run `sudo pigpiod` to enable the `pigpio` daemon. 
* `dual_robot_pwm.py`: This is exactly like the previous code but this time speed control is introduced. In the text box I input a number between 1 and 10 to control the speed of both robots because in gpiozero the speed of a robot is between zero and 1 and in the slider I made sure to divide 10 since sliders cannot use float numbers.
* `camera_guizero.py`: To control the pi camera remotely while Torvalds moves I had to run this code from Torvalds using VNC viewer since this code cannot run on an ssh session. The `dual_robot.mp4` video shows the final result of all the tests.

## Pictures

* `dual_improve(https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-12-140715_1920x1080_scrot.pngd_movement.py`
* ![dual](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-12-140715_1920x1080_scrot.png)
* `dual_robot_pwm.py`
* ![pwm](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-17-163125_1920x1080_scrot.png)
* `camera_guizero_.py` plus `dual_robot_pwm.py`
* ![camera](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-17-163135_1920x1080_scrot.png)
* ![robots](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/IMG_20210213_120338052.jpg)
