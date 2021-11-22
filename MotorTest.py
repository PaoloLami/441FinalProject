import RPi.GPIO as GPIO
import time

#SETUP shown here: https://www.rhydolabz.com/wiki/?p=11288
GPIO.setwarnings(False)

Motor1cw = 23 # Motor 1 +Red pin
Motor1ccw = 24 # Motor 1 +Ground pin
Motor2cw = 5 # Motor 2 +Red pin
Motor2ccw = 6 # Motor 2 +Ground pin
Motor1EN = 25 #Enabler for motor 1
Motor2EN = 26 #Enabler for motor 2
#Plug both Vcc to Pi 5V

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1cw,GPIO.OUT) 
GPIO.setup(Motor1ccw,GPIO.OUT)
GPIO.setup(Motor2cw,GPIO.OUT)
GPIO.setup(Motor2ccw,GPIO.OUT)

GPIO.setup(Motor1EN, GPIO.OUT)
GPIO.setup(Motor2EN, GPIO.OUT)

#PWM setup
M1cw=GPIO.PWM(Motor1EN,100)
M1ccw=GPIO.PWM(Motor2EN,100)
M2cw=GPIO.PWM(Motor1EN,100)
M2ccw=GPIO.PWM(Motor2EN,100)
pwm1=GPIO.PWM(Motor1EN,100)
pwm2=GPIO.PWM(Motor2EN,100)
pwm1.start(0)
pwm2.start(0)
M1cw.start(0)
M1ccw.start(0)
M2cw.start(0)
M2ccw.start(0)

try:

    #GPIO.output(Motor1cw,GPIO.LOW)
    #GPIO.output(Motor1ccw,GPIO.HIGH) #turn HIGH for counterclockwise
    #GPIO.output(Motor1EN,GPIO.HIGH)
    pwm1.ChangeDutyCycle(99)
    M1ccw.ChangeDutyCycle(99)

    #GPIO.output(Motor2cw,GPIO.HIGH)
    #GPIO.output(Motor2ccw,GPIO.LOW) #turn HIGH for counterclockwise
    #GPIO.output(Motor2EN,GPIO.HIGH)
    pwm2.ChangeDutyCycle(99)
    M2cw.ChangeDutyCycle(99)

    time.sleep(300)

    #GPIO.output(Motor1EN,GPIO.LOW)
    #GPIO.output(Motor2EN,GPIO.LOW)
    pwm1.stop(0)
    pwm2.stop(0)
    M1cw.stop(0)
    M1ccw.stop(0)
    M2cw.stop(0)
    M2ccw.stop(0) 

    GPIO.cleanup()   

except KeyboardInterrupt:
  print("Ending")
  #GPIO.output(Motor1EN,GPIO.LOW)
  #GPIO.output(Motor2EN,GPIO.LOW)
  pwm1.stop(0)
  pwm2.stop(0)
  M1cw.stop(0)
  M1ccw.stop(0)
  M2cw.stop(0)
  M2ccw.stop(0)
  GPIO.cleanup() 

