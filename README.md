# CircuitPython

If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).

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
#Elias
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT
#This code rotates a servo back and forth

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

![ezgif com-gif-maker](https://user-images.githubusercontent.com/112961319/192808365-425dc20f-adb3-4a49-96a3-89f3e8195865.gif)

### Wiring

![image](https://user-images.githubusercontent.com/112961319/192807559-d1add3fb-849b-4811-b61a-297383081065.png)

### Reflection




## CircuitPython_LCD

### Description & Code

Code credit goes to [Grant Gastinger](https://github.com/ggastin30/CPython)

```
#Elias Garcia
#When a button is presses it increses or decreases the count based on the position of a switch
#Code from Grant Gastinger

import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
clickCount = 0

switch = DigitalInOut(board.D7)
switch.direction = Direction.INPUT
switch.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27...
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("elias")
print("son, i am disapoint.")
while True:
    if not switch.value:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount + 1
            lcd.print(str(clickCount))
        else:
            pass
    else:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount - 1
            lcd.print(str(clickCount))
        else:
            pass
    time.sleep(0.1) # sleep for debounce
```
This code creates an LCD object and prints "elias" to the LCD. It also sets up a button and a switch, and tracks the number of times the button is clicked. If the switch is on, clicking the button decreases the click count. If the switch is off, clicking the button increases the click count.

### Evidence

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/112961319/193040969-56204239-2e81-486f-a2e2-43e14046091b.gif)

### Wiring

![Screenshot 2022-09-29 8 37 07 AM](https://user-images.githubusercontent.com/112961319/193033429-e5198fd6-79fd-4952-a702-64e0c3bba90c.png)

### Reflection



## CircuitPython_Ultrasonic

### Description & Code

Code credit goes to my classmates [Graham Gilbert-Schroeer](https://github.com/VeganPorkChop/CircutPython) and [Jack Helmke](https://github.com/jhelmke45/CircuitPython)

```
#Elias Garcia
#This changes a gradient on the neopixel based on the distance outputted by the ultrasonic sensor
#Base code from Graham Gilbert-Schroeer

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

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/112961319/193037726-5598bf39-e9a5-4eb4-a133-c633c204e274.gif)

### Wiring

![snapture23](https://user-images.githubusercontent.com/112961319/193045742-26a5ac02-6881-416c-9d54-af293deceae0.PNG)

### Reflection
