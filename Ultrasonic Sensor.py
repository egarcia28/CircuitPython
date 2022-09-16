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
    