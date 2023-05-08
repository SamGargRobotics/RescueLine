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
# invert_sensor = ColorSensor(Port.S4)
StopWatch = StopWatch()
greenleftrange = 30-21
greenrightrange = 19-32
rescue_flag = False
def lineFollow():
    wait(10)
    if rescue_flag is True:
        return
    if rightlight_sensor.reflection() < 50 and leftlight_sensor.reflection() < 50:
        motors.drive(40,0)
    # elif invert_sensor.color() == Color.BLACK and rightlight_sensor.reflection() < 20 and leftlight_sensor.reflection() < 20:
    #     KP = 1.9
    #     error = -1*(leftlight_sensor.reflection()) + rightlight_sensor.reflection()
    #     turn_rate = error*KP
    #     motors.drive(70,turn_rate)
    else:
        KP = 1.5
        error = leftlight_sensor.reflection() - rightlight_sensor.reflection()
        turn_rate = error*KP
        motors.drive(50,turn_rate)
    
def waterTower():
    motors.stop()
    left_motor.run(50)
    right_motor.run(-50)
    wait(3500)
    left_motor.hold()
    right_motor.hold()
    motors.drive(50,0)
    wait(3650)
    motors.stop()
    left_motor.run(-50)
    right_motor.run(50)
    wait(3500)
    left_motor.hold()
    right_motor.hold()
    motors.drive(100,0)
    wait(3500)
    motors.stop()
    left_motor.run(-50)
    right_motor.run(50)
    wait(2500)
    left_motor.hold()
    right_motor.hold()
    while not rightlight_sensor.reflection() < 50 or leftlight_sensor.reflection() < 50:
        left_motor.run(50)
        right_motor.run(49)
    right_motor.hold()
    left_motor.hold()

def rescue():
    motors.drive(-50,0) #start line allignment process
    wait(750)
    motors.stop()
    while not rightlight_sensor.reflection() < 66:
        right_motor.run(-30)
        left_motor.run(30)
    right_motor.hold()
    left_motor.hold()
    left_motor.run(50)
    right_motor.run(-50)
    wait(750)
    left_motor.hold()
    right_motor.hold()
    right_motor.run(50)
    left_motor.run(-50)
    wait(750)
    right_motor.hold()
    left_motor.hold()    
    if leftlight_sensor.reflection() < 50:
        motors.drive(50,30)
        wait(200)
        motors.stop() 
    if rightlight_sensor.reflection() < 50:
        motors.drive(50,-30)
        wait(200)
        motors.stop() # end allignment process
    motors.drive(50,0) #start centering chemical spill
    wait(250)
    motors.stop()
    motors.drive(100,0)
    wait(3100)
    motors.stop() #end centering chemical spill
    stopwatch.reset() # finding victim
    while not ultrasonic_sensor.distance() < 310:
        left_motor.run(-50)
        right_motor.run(50)
    spintime1 = stopwatch.time()
    left_motor.hold()
    right_motor.hold() #end finding victim
    wait(1000)
    stopwatch.reset()
    spintime2 = stopwatch.time()
    stopwatch.reset()
    left_motor.run(50)
    right_motor.run(-50)
    wait(spintime2/2)
    left_motor.hold()
    right_motor.hold()
    stopwatch.reset()
    if ultrasonic_sensor.distance() >= 90: # claw alignment
        velocity1 = 1
        while not ultrasonic_sensor.distance() < 35:
            motors.drive(50,0)
        motors.stop()
    else:        
        if ultrasonic_sensor.distance() < 35: #90 (last)
            velocity1 = 0
            while not ultrasonic_sensor.distance() > 35:
                motors.drive(-50,0)
            motors.stop()
    straighttime1 = stopwatch.time()
    claw_motor.run(-1000)
    wait(3500)
    claw_motor.hold()
    stopwatch.reset()
    while not rightlight_sensor.reflection() > 50 and not leftlight_sensor.reflection() > 50:
        motors.drive(50,0)
    motors.stop()
    straighttime2 = stopwatch.time()
    claw_motor.run(1000)
    wait(3500)
    claw_motor.hold()
    motors.drive(-50,0)
    wait(straighttime2)
    motors.stop()
    if velocity1 == 1:
        motors.drive(-50,0)
        wait(straighttime1)
        motors.stop()
    else:
        motors.drive(50,0)
        wait(straighttime1)
        motors.stop()
    left_motor.run(50)
    right_motor.run(-50)
    wait(spintime1)
    wait(spintime2)
    left_motor.hold()
    right_motor.hold()
    ev3.screen.print('START')    
    while not leftlight_sensor.reflection() == 100 or not rightlight_sensor.reflection() == 100:
        motors.drive(-50,0)
    motors.stop()
    ev3.screen.print('FINISHED!')
    left_motor.run(50)
    right_motor.run(-50)
    wait(7000)
    left_motor.hold()
    right_motor.hold()
while True:
    if leftlight_sensor.reflection() >= 100 and rightlight_sensor.reflection() >= 100:
        rescue_flag = True
        rescue()
        rescue_flag = False
    else:
        lineFollow()
