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
Arm = Motor(Port.C, positive_direction = Direction.CLOCKWISE)
ColorSen = ColorSensor(Port.S1)

print("initalized")

LeftMotor.reset_angle(0)
RightMotor.reset_angle(0)
Arm.reset_angle(0)
LeftMotor.hold()
RightMotor.hold()
Arm.hold()

#varibles
pi = 3.14
WheelDia = 2.125
WheelCir = pi*WheelDia

#functions
def EncodersReset():
    LeftMotor.reset_angle(0)
    RightMotor.reset_angle(0)

def Grab(status):
    if (status == 1): #close
        Arm.run_target(1000, -10, then=Stop.HOLD, wait=True)
    elif (status == 0): #open
        Arm.run_target(1000, 30, then=Stop.HOLD, wait=True)

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
    LeftMotor.run_target((4448*speed+1), LeftTarget, then=Stop.HOLD, wait=False)
    RightMotor.run_target((4448*speed), RightTarget, then=Stop.HOLD, wait=True)

def SortColor():
    if (ColorSen.color() == Color.YELLOW):
        Grab(1)
        turn(90,1)
        drive(5,1)
        Grab(0)
        drive(-5,1)
        turn(-90,1)
    if (ColorSen.color() == Color.BLUE):
        Grab(1)
        turn(-90,1)
        drive(5,1)
        Grab(0)
        drive(-5,1)
        turn(90,1)
#run
Grab(0)
drive(10,0.5)
Grab(1)
while(True):
    if (ColorSen.color() == Color.BLUE or ColorSen.color() == Color.YELLOW):
        Grab(1)
        break
SortColor()



