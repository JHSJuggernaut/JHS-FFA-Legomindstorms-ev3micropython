#!/usr/bin/env pybricks-micropython
__name__ == "__main__"
#imports
import random, time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# setup
ev3 = EV3Brick()
LeftMotor = Motor(Port.A, positive_direction = Direction.CLOCKWISE)
RightMotor = Motor(Port.B, positive_direction = Direction.CLOCKWISE)
print("initalized")

LeftMotor.reset_angle(0)
RightMotor.reset_angle(0)
LeftMotor.hold()
RightMotor.hold()

#varibles
pi = 3.14
WheelDia = 2.125
WheelCir = pi*WheelDia

#functions
def EncodersReset():
    LeftMotor.reset_angle(0)
    RightMotor.reset_angle(0)

def drive(distance, speed):
    EncodersReset()
    #math for angle to distance
    TargetAngle = distance/(WheelCir/360)
    #move the motors
    LeftMotor.run_target((4448*speed), TargetAngle, then=Stop.HOLD, wait=False)
    RightMotor.run_target((4448*speed), TargetAngle, then=Stop.HOLD, wait=True)


def turn(angle,speed):
    EncodersReset()
    #math for turning each wheel
    ArchLength = ((pi * WheelDia * angle) / 130.25)
    LeftTarget = ArchLength/(WheelCir/360)
    RightTarget = (ArchLength/(WheelCir/360)) * -1

    #Move the motors
    LeftMotor.run_target((4448*speed), LeftTarget, then=Stop.HOLD, wait=False)
    RightMotor.run_target((4448*speed), RightTarget, then=Stop.HOLD, wait=True)

# run
for i in range(4):
    drive(10,1)
    turn(90,1)