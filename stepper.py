#Paolo Lami, ENME441 Lab5
import RPi.GPIO as GPIO
import time
        
#Setup pins for the stepper motor
pins = [18,21,22,23] #controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.OUT, initial=0)

#Define the pin sequence for counter-clockwise motion, noting that
#two adjacent phases must be actuated together before stepping to
#a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

state = 0 #current position in stator sequence

def delay_us(tus): #use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

#Moves the stepper motor by a half step in the direction specified
def halfstep(dir): 
  #dir  = +/-1 (ccw/cw)
  global state, pins, sequence
  state += dir #changes state depending on the direction (ccw, cw)
  if state > 7: state = 0
  elif state < 0: state = 7
  for pin in range(4): #4 pins that need to be energized
    GPIO.output(pins[pin],sequence[state][pin])
  delay_us(1000) #decrease to make stepper motor faster

#Takes angle of travel from text file and converts it into number of halfsteps required 
def goAngle(ang,dir):
  numhalfstep = int(ang/0.087875) #conversion from angle to number of halfsteps
  direction = dir
  for step in range(numhalfstep):
      halfstep(direction)



    