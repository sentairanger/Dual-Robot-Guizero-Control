# Dual-Robot-Guizero-Control

## Introduction

This project was conceived of after I learned about guizero from the `Create Graphical User Interfaces with Python` by Martin O'Hanlon and Laura Sach. I tried out the examples in the book and then did some of my own GUIs to control LEDs and servo motors. After that I scaled up to my robots and here I will show you the full process of everything I did. 

## Getting Started

To begin with first I will explain the hardware and software I used for the project. 

### Hardware

Here is the list of supplies I used:

* My robot Torvalds (I used this robot from previous projects in my other GitHub Repos). Materials list found on `torvalds_materials.txt` file.
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
* For the final test, I ran `dual_robot_pwm.py` and then ran `camera_guizero.py` on Torvalds using VNC Viewer.
* `torvalds.py`: This was the initial test code I used for Torvalds locally to make sure the motors and the camera was working.
* `linus_movement.py`: This was the initial test code I also used for Linus to test the motors and the servos before upscaling to the next phase.
* `dual_movement_gui.py`: This is similar to `dual_improved_movement.py` only this time PWM is only on Linus and this code can be run on any platform.
## Pictures
* `dual_robot_mobile.py`: This is similar to `dual_improved_movement.py` but can be run on any machine using VNC Viewer.

* `dual_improved_movement.py`
* ![dual](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-12-140715_1920x1080_scrot.png)
* `dual_robot_pwm.py`
* ![pwm](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-17-163125_1920x1080_scrot.png)
* `camera_guizero_.py` plus `dual_robot_pwm.py`
* ![camera](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/2021-02-17-163135_1920x1080_scrot.png)
* ![robots](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/IMG_20210213_120338052.jpg)
* `dual_movement_gui`![platform](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/Screenshot%20from%202021-03-31%2016-47-45.png)
* `gui-robot-update.py`
* ![update](https://github.com/sentairanger/Dual-Robot-Guizero-Control/blob/main/new-gui.png)

## Note on Duplicating the Project on Your Own

To duplicate this project you can use any robot you wish as long as it uses a Raspberry Pi. Pi OS or Pi OS Lite is recommended for each robot. Also, to ensure `pigpio` is enabled, you must use the `sudo pigpiod` command. When controlling the robots, if you are not using a raspberry pi to control them use the following [link](https://gpiozero.readthedocs.io/en/stable/installing.html) to follow the instructions depending on your machine. Also make sure `guizero` is installed by using the `pip3 install guizero` or `pip install guizero` commands. 

To run this on your own:
* Copy the link from the code button and then go to your terminal and clone the repo by running the command `git clone https://github.com/sentairanger/Dual-Robot-Guizero-Control.git`
* Take the `camera_guizero.py` code and copy it to the other robot that uses a Pi Camera. If both robots use a Camera you would still do the same thing. The easiest way to do so is to insert the SD card into an SD card reader and copy it to the root partition of the card, specifically the `/home/pi` directory. You can choose any sub directory you want for the file to be copied to. 
* You cannot run the code from the terminal on the Pi so you can use an IDE like Mu or Geany. I recommend Mu as it's more straightforward.

To run this on other platforms (Linux, Windows and Mac) use the `dual_movement_gui.py` code and it should work. Just make sure that you have python 3 installed as well as `guizero`, `gpiozero` and `pigpio`. Also note that the motor and robot modules for `gpiozero` do not work on Linux, Windows or Mac due to a bug so please use the OutputDevice and PWMOutputDevice modules instead as they work on all platforms. 

* Windows: In order to run the code on Windows, first you will need a program like PUTTY to SSH into both robots as SSH is not included in Windows. Make sure to install Python from the official site and install the modules in the command prompt using pip3. Then install an IDE such as Mu or IDLE to run the code.
* Mac OS: You can either install Python using the main site or `brew install python`. Use an IDE like Mu or IDLE to run the code. Make sure to install the needed modules and SSH into each robot.
* Linux: Make sure pip3 is installed and install the needed modules. Use an IDE such as Mu or IDLE and make sure to SSH into both robots.


## Update

I added the `gui-robot-update.py` code to reflect the use of picamera2. The rest of the files will be updated to reflect the use of picamera2 as picamera no longer works on Bullseye or Bookworm. The image is also added to show the changes. The new code must run on a Raspberry Pi with Bullseye or newer. Picamera will be depreciated in the future so it's important to use this code instead. This can be extended to add more cameras, including the Raspberry Pi 5.

## Dedication

This project is dedicated to Mr. Cain who has always supported my goals and sadly passed away in 2018. To my dad who died from covid in November and hoping he is still proud of my progress. To my abuelita who died in March 2020 from anemia. To my neighbor Vicente who I always took care of and sadly passed away from alzheimers in 2018. To all those in my family and my friends who passed away. To my friends who have been very supportive. And to the Perseverance team for inspiring me to do better. 
