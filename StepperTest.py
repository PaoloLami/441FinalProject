import RPi.GPIO as GPIO
import stepper
import time

dir = input("Set direction: ")
dir=int(dir)
angle = input("Set angle: ")
angle=int(angle)

stepper.goAngle(angle,dir)
time.sleep(1)
GPIO.cleanup