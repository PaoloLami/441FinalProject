#Paolo Lami and Jake Crossan, ENME441 Final Project
import RPi.GPIO as GPIO
import time

#Using a Dual H-bridge to control both motors

Motor1cw = 23 # Motor 1 +Red pin
Motor1ccw = 24 # Motor 1 +Ground pin
Motor2cw = 5 # Motor 2 +Red pin
Motor2ccw = 6 # Motor 2 +Ground pin
Motor1EN = 25 #Enabler for motor 1 pwm
Motor2EN = 26 #Enabler for motor 2 pwm

servoPin = 4

dcMin = 3
dcMax = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1cw,GPIO.OUT) 
GPIO.setup(Motor1ccw,GPIO.OUT)
GPIO.setup(Motor2cw,GPIO.OUT)
GPIO.setup(Motor2ccw,GPIO.OUT)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(Motor1EN, GPIO.OUT)
GPIO.setup(Motor2EN, GPIO.OUT)

#PWM setup
pwm1=GPIO.PWM(Motor1EN,100)
pwm2=GPIO.PWM(Motor2EN,100)
pwmServo = GPIO.PWM(servoPin, 50) # PWM object at 50 Hz (20 ms period)
pwmServo.start(dcMin)

def Launch(power):
  #Turn on motors
  pwm1.start(0)
  pwm2.start(0)

  #Depending on the power option selected, change speed (calibrated for straight shots)
  if power == 1:
    dc1=55
    dc2=50
  elif power == 2:
    dc1=65
    dc2=60
  elif power==3:
    dc1=75
    dc2=70
  
  #Set direction of motors (based on wiring)
  GPIO.output(Motor1cw,GPIO.LOW)
  GPIO.output(Motor1ccw,GPIO.HIGH) #turn HIGH for counterclockwise

  GPIO.output(Motor2cw,GPIO.LOW)  #turn HIGH for counterclockwise
  GPIO.output(Motor2ccw,GPIO.HIGH) 

  time.sleep(0.5)
 
  #Turn on both motors to desired speed (based on power)
  pwm1.ChangeDutyCycle(dc1)
  pwm2.ChangeDutyCycle(dc2)
  time.sleep(5)

  #Rotate the servo motor to push ball towards spinning motors
  for dc in range(dcMin,dcMax):
    pwmServo.ChangeDutyCycle(dc)
    time.sleep(0.025)
  time.sleep(1.5)  
  pwmServo.ChangeDutyCycle(dcMin)  
  time.sleep(1.5)  

  #Set speed of motors back to 0
  pwm1.ChangeDutyCycle(0)
  pwm2.ChangeDutyCycle(0)
  time.sleep(1)  

def turnoff():
  pwm1.stop(0)
  pwm2.stop(0)

