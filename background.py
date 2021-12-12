import RPi.GPIO as GPIO
from PCF8591 import PCF8591
import stepper
import time
import Launch

#Set previous angle to 0 at start (needed for required halfsteps calculation first time)
anglePREV = 0
powerPREV = 0
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

    #Read angle input from user in file
    #Calculate the required angle of movement needed  
    #angle = angleNEW - anglePREV
    #launchCheck = power-powerPREV
    #if angle > 0:
    #  dir = 1  #clockwise
    #if angle < 0:
    #  dir = -1 #counterclockwise if the new angle is lower than previous
    #  angle = abs(angle)
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
        time.sleep(2.5)

        GPIO.setup(ledPinLaunch, GPIO.OUT)
        GPIO.output(ledPinLaunch,0) 
        #print(light)
        print("Launching!") 
        Launch.Launch(power)
        GPIO.output(ledPinLaunch,1) 

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
        
    #Set the previous angle to the current angle for next iteration
    #anglePREV = angleNEW
    #powerPREV = power
    
except KeyboardInterrupt:
  GPIO.cleanup()
  Launch.turnoff()
  print("Exiting...")