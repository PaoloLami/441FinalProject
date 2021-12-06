import RPi.GPIO as GPIO
import stepper
import time
import Launch

#Set previous angle to 0 at start (needed for required halfsteps calculation first time)
anglePREV = 0
powerPREV = 0
angle = 0
launchCheck = 0
ledPinReset = 19
ledPinLaunch = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPinReset, GPIO.OUT)
GPIO.setup(ledPinLaunch, GPIO.OUT)

try:
  while True: 
    #Read angle input from user in file
    with open('angle.txt', 'r') as f:
      angleNEW = int(f.read())
    with open('power.txt', 'r') as f:
      power = int(f.read())
    #Calculate the required angle of movement needed  
    angle = angleNEW - anglePREV
    launchCheck = power-powerPREV
    if angle > 0:
      dir = 1  #clockwise
    if angle < 0:
      dir = -1 #counterclockwise if the new angle is lower than previous
      angle = abs(angle)

    #Reset function if angle is set to 0 (from cgi file)
    if angleNEW == 0:
      angle = 0
      launchCheck = 0
      GPIO.setup(ledPinReset, GPIO.OUT)  
      GPIO.output(ledPinReset,1) 
      print('Set to 0')
      stepper.goAngle(90,-1)
    
    #Go to angle if angle is not 0 (from cgi file)
    else:
      GPIO.setup(ledPinReset, GPIO.OUT)
      GPIO.output(ledPinReset,0)  
      print(angleNEW)
      stepper.goAngle(angle,dir)
    time.sleep(0.5)

    if launchCheck != 0 or angle != 0:
      GPIO.setup(ledPinLaunch, GPIO.OUT)
      GPIO.output(ledPinLaunch,1) 
      print("Launching!") 
      Launch.Launch(power)
      GPIO.output(ledPinLaunch,0) 

    #Set the previous angle to the current angle for next iteration
    anglePREV = angleNEW
    powerPREV = power
    
except KeyboardInterrupt:
  GPIO.cleanup()
  print("Exiting...")