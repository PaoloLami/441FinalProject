#Paolo Lami and Jake Crossan, ENME441 Final Project
import RPi.GPIO as GPIO
from PCF8591 import PCF8591
import stepper
import time
import Launch
import Ultrasonic

angle = 0
launchCheck = 0
sens = PCF8591(0x48)
light = sens.read(1)*10 #reads data from the photoresistor
ledPinReset = 19
ledPinLaunch = 13
ledPinBalls=18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPinReset, GPIO.OUT)
GPIO.setup(ledPinLaunch, GPIO.OUT)
GPIO.setup(ledPinBalls, GPIO.OUT)
GPIO.output(ledPinReset,1)
GPIO.output(ledPinLaunch,1)
GPIO.output(ledPinBalls,1)

try:
  while True: 
    with open('angle.txt', 'r') as f:
      angle = int(f.read())
    with open('power.txt', 'r') as f:
      power = int(f.read())
    time.sleep(0.5)

    light = sens.read(1)*10 #reads data from the photoresistor
    time.sleep(0.1)

    
    dir = 1

    #Reset function if angle is set to 0 (from cgi file)
    if angle == 0:
      power = 0
      GPIO.setup(ledPinReset, GPIO.OUT)  
      GPIO.output(ledPinReset,0) 
    #  print('Set to 0')
    #  stepper.goAngle(90,-1)

    elif power != 0 or angle != 0:
      if light<1675:
        GPIO.setup(ledPinReset, GPIO.OUT)
        GPIO.output(ledPinReset,1)  
        print(angle)
        stepper.goAngle(angle,dir)
        time.sleep(1.5)

        GPIO.setup(ledPinLaunch, GPIO.OUT)
        GPIO.output(ledPinLaunch,0) 
        #print(light)
        print("Launching!") 
        Launch.Launch(power)
        GPIO.output(ledPinLaunch,1)

        time.sleep(2)
        dist = Ultrasonic.distance()
        print(dist)
        if dist < 10:
          for n in range(10):
            GPIO.output(ledPinLaunch,0) 
            time.sleep(0.3)
            GPIO.output(ledPinLaunch,1)
            time.sleep(0.1)
          GPIO.output(ledPinLaunch,1) 
        else:
          for n in range(10):
            GPIO.output(ledPinReset,0) 
            time.sleep(0.3)
            GPIO.output(ledPinReset,1)
            time.sleep(0.1)
          GPIO.output(ledPinReset,0) 

        GPIO.setup(ledPinReset, GPIO.OUT)  
        GPIO.output(ledPinReset,0) 
        print('Resetting')
        stepper.goAngle(90,-1)
        
      elif light>=1675:
        print("No balls remaining, please insert ball")
        GPIO.setup(ledPinReset, GPIO.OUT)
        GPIO.output(ledPinReset,1)
        GPIO.setup(ledPinBalls, GPIO.OUT)
        for n in range(7):
          GPIO.output(ledPinBalls,0) 
          time.sleep(0.6)
          GPIO.output(ledPinBalls,1)
          time.sleep(0.1)
        GPIO.output(ledPinBalls,1)
    
except KeyboardInterrupt:
  GPIO.cleanup()
  Launch.turnoff()
  print("Exiting...")