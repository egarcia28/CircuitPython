First, you will need to import the necessary libraries:

import time
import board

Next, you will need to create a PWMOut object on the specified pin. In this case, we will use pin D1:

servo = pulseio.PWMOut(board.D1, frequency=50)

To move the servo, you will need to set the duty cycle of the PWM signal. A value of 2000 corresponds to a fully clockwise rotation, while a value of 1000 corresponds to a fully counter-clockwise rotation. Values in between will result in proportional movement.

For example, to rotate the servo clockwise by 90 degrees:

servo.duty_cycle = 2000
time.sleep(0.5)

To rotate the servo counter-clockwise by 90 degrees:

servo.duty_cycle = 1000
time.sleep(0.5)

Finally, to stop the servo:

servo.duty_cycle = 0
