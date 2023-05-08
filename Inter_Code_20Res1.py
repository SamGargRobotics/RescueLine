#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
claw_motor = Motor(Port.A)
rightlight_sensor = ColorSensor(Port.S3)
leftlight_sensor = ColorSensor(Port.S4)
ultrasonic_sensor = UltrasonicSensor(Port.S1)
error = 0 #to initialise error
P = 100 #If this does not work change this back to 15 or change it to be below 50 but above 15.
turn_rate = 0 #to initialise turn_rate
def lineFollow():
    error = 100/(-1*leftlight_sensor.reflection()) + 100/(rightlight_sensor.reflection())
    turn_rate = error*P
    # if turn_rate >= 0: (If needed insert this back into the code)
    if rightlight_sensor.reflection() > 40 and leftlight_sensor.reflection() > 40:
        left_motor.run(160)
        right_motor.run(160)
    if rightlight_sensor.reflection() < 40 and leftlight_sensor.reflection() > 40:
        left_motor.run(-1*turn_rate)
        right_motor.run(turn_rate)
    # if turn_rate < 0: (If needed insert this back into the code)
    if rightlight_sensor.reflection() > 40 and leftlight_sensor.reflection() < 40:
        left_motor.run(turn_rate)
        right_motor.run(-1*turn_rate)
    # NON COMMENT: making clearer to read
    # !ASK: If anything above is not happening how do I do the green shortcuts?!
    if rightlight_sensor.color() == Color.BLUE or rightlight_sensor.color() == Color.GREEN:
        while not (rightlight_sensor.color() == Color.WHITE):
                    right_motor.run(80)
                    left_motor.run(190)
    if leftlight_sensor.color() == Color.BLUE or leftlight_sensor.color() == Color.GREEN:
        while not (rightlight_sensor.color() == Color.WHITE):
                    right_motor.run(190)
                    left_motor.run (40)
    if rightlight_sensor.color() == Color.BLACK:
        while (rightlight_sensor.color() == Color.BLACK):
                    right_motor.run(80)
                    left_motor.run (80)
    if rightlight_sensor.color() == Color.BROWN:
        while (rightlight_sensor.color() == Color.BROWN):
                left_motor.run(80)
                right_motor.run(80)
    if rightlight_sensor.color() == Color.BROWN:
        while (rightlight_sensor.color() == Color.BROWN):
                right_motor.run(80)
                left_motor.run(80)
def waterTower():
    if ultrasonic_sensor.distance() < 70:
        left_motor.run(-50)
        right_motor.run(50)
        wait(39)
        left_motor.hold()
        right_motor.hold()
        left_motor.run(12)
        right_motor.run(12)
        wait(250)
        left_motor.hold()
        right_motor.hold()
        left_motor.run(50)
        right_motor.run(-50)
        wait(34)
        left_motor.hold()
        right_motor.hold()
        left_motor.run(12)
        right_motor.run(12)
        wait(550)
        left_motor.hold()
        right_motor.hold()
        left_motor.run(50)
        right_motor.run(-50)
        wait(30)
        left_motor.hold()
        right_motor.hold()
        while not (leftlight_sensor.reflection() < 50):
            left_motor.run(12)
            right_motor.run(12)
def rescue():
    1 == 1
    ## WIP Work in Progress 
        if leftlight_sensor.reflection() > 100 or rightlight_sensor.reflection() > 100:
            left_motor.rotation_angle(1.7)
            right_motor.rotation_angle(1.7)
            claw_motor.run(-1.75)
            reset()
            while not (ultrasonic_sensor.distance() < 300):
                left_motor.run(-5)
                right_motor.run(5)
            left_motor.hold()
            right_motor.hold()
            TurningTime1 = time()
            reset()
            while not (ultrasonic_sensor.distance() > 300)
                left_motor.run(-5)
                right_motor.run(5)
            left_motor.hold()
            right_motor.hold()
            turningTime2 = time()
            left_motor.run(5)
            right_motor.run(-5)
            wait(turningTime2()/2)
            left_motor.hold()
            right_motor.hold()
            reset()
            while not (ultrasonic_sensor.distance < 100)
                left_motor.run(12)
                right_motor.run(12)
                left_motor.hold()
                right_motor.hold()
                claw_motor.run(-1.8)
            while not (rightlight_sensor.reflection > 60)
                right_motor.run(12)
                left_motor.run(12)
            StraightTime1 = timer()
            left_motor.hold()
            right_motor.hold()
            claw_motor.run(12)
            wait(350)
            left_motor.hold()
            right_motor.hold()
            right_motor.run(-12)
            left_motor.run(-12)
            wait(straightTime1)
            left_motor.hold()
            right_motor.hold()
            left_motor.run(5)
            right_motor.run(-5)
            wait(turningTime2/2 + turningTime1)
            left_motor.hold()
            right_motor.hold()
            while not rightlight_sensor.reflection() > 95 or rightlight_sensor.reflection() > 95:
                left_motor.run(-25)
                right_motor.run(-25)
            left_motor.hold()
            right_motor.hold()
            left_motor.rotation_angle(-50)
            right_motor.rotation_angle(50)
            left_motor.run(-20)
            right_motor.run(-20)
            wait(40)
            left_motor.hold()
            right_motor.hold()
while True:
    if leftlight_sensor.reflection() > 100 or rightlight_sensor.reflection() > 100:
        rescue()
    elif ultrasonic_sensor.distance() < 7:
        waterTower()
    else:
        lineFollow()