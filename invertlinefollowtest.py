#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.ev3devices import TouchSensor
from pybricks.ev3devices import ColorSensor
from pybricks.ev3devices import InfraredSensor
from pybricks.ev3devices import UltrasonicSensor
from pybricks.ev3devices import  GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)
claw_motor = Motor(Port.A)
motors = DriveBase(left_motor,right_motor,56,85)
rightlight_sensor = ColorSensor(Port.S3)
leftlight_sensor = ColorSensor(Port.S2)
ultrasonic_sensor = UltrasonicSensor(Port.S1)
invert_sensor = ColorSensor(Port.S4)
StopWatch = StopWatch()
greenleftrange = 30-21
greenrightrange = 19-32
while True:
    KP = 2.35
    error = -1*(leftlight_sensor.reflection()) + rightlight_sensor.reflection()
    turn_rate = error*KP
    motors.drive(70,turn_rate)