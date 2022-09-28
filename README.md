# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Ultrasonic Sensor](#CircuitPython_Ultrasonic)
---



## CircuitPython_Servo

### Description & Code

Code credit goes to [this adafruit link](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/circuitpython-servo)

```
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin D2.
pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=250)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.0)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.0)
```
First, you will need to import the necessary libraries:
Next, you will need to create a PWMOut object on the specified pin. In this case, I used pin D1:
To move the servo, you will need to set the duty cycle of the PWM signal. A value of 2000 corresponds to a fully clockwise rotation, while a value of 1000 corresponds to a fully counter-clockwise rotation. Values in between will result in proportional movement.
For example, to rotate the servo clockwise by 90 degrees:
servo.duty_cycle = 2000 time.sleep(0.5)

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## CircuitPython_Ultrasonic

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
