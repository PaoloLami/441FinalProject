import RPi.GPIO as GPIO
import time

#PMW WORKS, NEEDS MORE THAN 6V PER MOTOR TO RUN with h bridge
#SETUP shown here: https://www.rhydolabz.com/wiki/?p=11288

Motor1cw = 23 # Motor 1 +Red pin
Motor1ccw = 24 # Motor 1 +Ground pin
Motor2cw = 5 # Motor 2 +Red pin
Motor2ccw = 6 # Motor 2 +Ground pin
Motor1EN = 25 #Enabler for motor 1
Motor2EN = 26 #Enabler for motor 2
#Plug both Vcc to Pi 5V

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
  pwm1.start(0)
  pwm2.start(0)
  
  if power == 1:
    dc1=30
    dc2=35
  elif power == 2:
    dc1=50
    dc2=55
  elif power==3:
    dc1=70
    dc2=75
  
  GPIO.output(Motor1cw,GPIO.LOW)
  GPIO.output(Motor1ccw,GPIO.HIGH) #turn HIGH for counterclockwise

  GPIO.output(Motor2cw,GPIO.HIGH)
  GPIO.output(Motor2ccw,GPIO.LOW) #turn HIGH for counterclockwise

  time.sleep(0.5)
 
  pwm1.ChangeDutyCycle(dc1)
  pwm2.ChangeDutyCycle(dc2)
  time.sleep(5)

  for dc in range(dcMin,dcMax):
    pwmServo.ChangeDutyCycle(dc)
    time.sleep(0.025)
  time.sleep(1.5)  
  pwmServo.ChangeDutyCycle(dcMin)  
  time.sleep(1.5)  

  pwm1.ChangeDutyCycle(0)
  pwm2.ChangeDutyCycle(0)
  time.sleep(1)  

def turnoff():
  pwm1.stop(0)
  pwm2.stop(0)

