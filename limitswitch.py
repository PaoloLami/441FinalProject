import RPi.GPIO as GPIO

pinled = 18
switch = 17

GPIO.setmode(GPIO.BCM)
#GPIO.setup(Motor1cw,GPIO.OUT) 
#GPIO.setup(Motor1ccw,GPIO.OUT)
GPIO.setup(pinled,GPIO.OUT)
GPIO.setup(switch,GPIO.IN)

while True:
  if GPIO.input(switch):
    GPIO.output(pinled,GPIO.HIGH)
  else:
    GPIO.output(pinled,GPIO.LOW)