import RPi.GPIO as GPIO
import time

#SETUP shown here: https://www.rhydolabz.com/wiki/?p=11288

Motor1cw = 23 # Motor 1 +Red pin
Motor1ccw = 24 # Motor 1 +Ground pin
Motor2cw = 5 # Motor 2 +Red pin
Motor2ccw = 6 # Motor 2 +Ground pin
pwmPin1 = 25 #Enabler for motor 1
pwmPin2 = 26 #Enabler for motor 2
#Plug both Vcc to Pi 3.3V

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1cw,GPIO.OUT) 
GPIO.setup(Motor1ccw,GPIO.OUT)
GPIO.setup(Motor2cw,GPIO.OUT)
GPIO.setup(Motor2ccw,GPIO.OUT)

GPIO.setup(pwmPin1, GPIO.OUT)
GPIO.setup(pwmPin2, GPIO.OUT)

#pwm1=GPIO.PWM(pwmPin1,100)
#pwm2=GPIO.PWM(pwmPin2,100)

try:
  while True:
    #pwm1.start(100)
    #pwm2.start(100)

    GPIO.output(Motor1cw,GPIO.LOW)
    GPIO.output(Motor1ccw,GPIO.HIGH) #turn HIGH for counterclockwise
    GPIO.output(pwmPin1,GPIO.HIGH)

    GPIO.output(Motor2cw,GPIO.HIGH)
    GPIO.output(Motor2ccw,GPIO.LOW) #turn HIGH for counterclockwise
    GPIO.output(pwmPin2,GPIO.HIGH)

except KeyboardInterrupt:
  print("Ending")
  GPIO.output(pwmPin1,GPIO.LOW)
  GPIO.output(pwmPin2,GPIO.LOW)
  #pwm1.stop()
  #pwm2.stop()
GPIO.cleanup() 

