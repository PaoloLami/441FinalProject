import RPi.GPIO as GPIO
import stepper
import time

#Set previous angle to 0 at start (needed for required halfsteps calculation first time)
anglePREV = 0
ledPin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

try:
  while True: 
    #Read angle input from user in file
    with open('angle.txt', 'r') as f:
      angleNEW = int(f.read())
    #Calculate the required angle of movement needed  
    angle = angleNEW - anglePREV
    if angle > 0:
      dir = 1  #clockwise
    if angle < 0:
      dir = -1 #counterclockwise if the new angle is lower than previous
      angle = abs(angle)

    #Reset function if angle is set to 0 (from cgi file)
    if angleNEW == 0:
      GPIO.setup(ledPin, GPIO.OUT)  
      GPIO.output(ledPin,1) 
      print('Set to 0')
      stepper.goAngle(90,-1)
    
    #Go to angle if angle is not 0 (from cgi file)
    else:
      GPIO.setup(ledPin, GPIO.OUT)
      GPIO.output(ledPin,0)  
      print(angleNEW)
      stepper.goAngle(angle,dir)
    time.sleep(0.5)
    #Set the previous angle to the current angle for next iteration
    anglePREV = angleNEW
    
except KeyboardInterrupt:
  print("Exiting...")