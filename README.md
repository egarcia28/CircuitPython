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
First, I imported the necessary libraries:
Next, you will need to create a PWMOut object on the specified pin. In this case, I used pin D1:
To move the servo, you will need to set the duty cycle of the PWM signal. A value of 2000 corresponds to a fully clockwise rotation, while a value of 1000 corresponds to a fully counter-clockwise rotation. Values in between will result in proportional movement.
For example, to rotate the servo clockwise by 90 degrees:
servo.duty_cycle = 2000 time.sleep(0.5)

### Evidence



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

Code credit goes to my classmates [Graham Gilbert-Schroeer](https://github.com/VeganPorkChop/CircutPython) and [Jack Helmke](https://github.com/jhelmke45/CircuitPython)

```
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = .3 
red = 0
green = 0
blue = 0

while True:
    try:
        cm = sonar.distance
        print((sonar.distance))
        time.sleep(0.001)
        if cm < 5:
            dot.fill((255, 0, 0))
        if cm > 5 and cm < 20:
            green=0
            red = simpleio.map_range(cm, 0, 20, 255, 0)
            blue = simpleio.map_range(cm, 5, 20, 0, 255)
            dot.fill((red, green, blue))
        if cm > 20 and cm < 35:
            red = 0
            green = simpleio.map_range(cm, 20, 35, 0, 255)
            blue = simpleio.map_range(cm, 20, 35, 255, 0)
            dot.fill((red, green, blue))
        if cm > 35:
            dot.fill((0, 255, 0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

```
This is  code that uses a sensor to measure the distance in cm and then uses that information to change the color of a neopixel. If the distance is less than 5cm, the neopixel will be red. If the distance is greater than 5cm and less than 20cm, the neopixel will be a gradient of red. If the distance is greater than 20cm and less than 35cm, the neopixel will be a gradient of blue. If the distance is greater than 35cm, the neopixel will be  green.

### Evidence

### Wiring

### Reflection
