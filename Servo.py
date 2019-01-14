# Copyright (C) 2019 Mark L. Woodward
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
# 
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA
# 
# If you want support or to commercially license this library, the author
# can be reached at markw@mohawksoft.com

import time
import RPi.GPIO as GPIO

# Mimics Arduino servo object
# 50HZ Servo
# 0.5 ms = 0 degrees
# 2.5 ms = 180 degrees
#
# 0.5 ms = 2.5% PWM duty cycle (50 hz)
# 2.5 ms = 12.5% PWM duty cycle (50 hz)
# 10% of duty cycle accounts for 0-180 degrees (2.5% to 12.5%)
# A minimum of 2.5% dudty cycle is required for servo operation
# The formula is angle * (10.0/180.0) + 5.0
#
class Servo:
    def __init__(self):
        self.servo_pin = -1
        self.servo = None
        self.angle = 0

    def __del__(self):
        if self.servo != None:
            self.servo.stop()

    def angle_to_duty_cycle(self,angle):
        if angle < 0:
            angle = 0 
        if angle > 180:
            angle = 180

        duty_cycle = (angle * (10.0/180.0)) + 2.5
        # print (str(angle) + " = " + str(duty_cycle) + " " + str((duty_cycle * 20) /100) + "ms")
        return duty_cycle

    def connect_pin(self):
        GPIO.setup(self.servo_pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.servo_pin, 50)

    def attach(self,pin):
        self.servo_pin = pin

    def write(self,angle):
        self.angle = angle
        dc = self.angle_to_duty_cycle(angle)
        if self.servo == None:
            self.connect_pin()
            self.servo.start(dc)
        else:
            self.servo.ChangeDutyCycle(dc)

    def read(self):
        return self.angle;
        



