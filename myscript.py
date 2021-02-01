import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

ForwardA=22
BackwardA=23
ForwardB=17
BackwardB=27
#enA=12
#enB=13
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(ForwardA, GPIO.OUT)
GPIO.setup(BackwardA, GPIO.OUT)
#GPIO.setup(enA, GPIO.OUT)
GPIO.setup(ForwardB, GPIO.OUT)
GPIO.setup(BackwardB, GPIO.OUT)
#GPIO.setup(enB, GPIO.OUT)

""" pA=GPIO.PWM(enA, 50)
pA.start(1)
pB=GPIO.PWM(enB, 50)
pB.start(1) """

def forward(x):
	GPIO.output(ForwardA, GPIO.HIGH)
	GPIO.output(ForwardB, GPIO.HIGH)
	print("Moving Forward")
	time.sleep(x)
	GPIO.output(ForwardA, GPIO.LOW)
	GPIO.output(ForwardB, GPIO.LOW)

def backward(x):
	GPIO.output(BackwardA, GPIO.HIGH)
	GPIO.output(BackwardB, GPIO.HIGH)
	print("Moving Backward")
	time.sleep(x)
	GPIO.output(BackwardA, GPIO.LOW)
	GPIO.output(BackwardB, GPIO.LOW)

def left(x):
	GPIO.output(ForwardA, GPIO.HIGH)
	time.sleep(x)
	GPIO.output(ForwardA, GPIO.LOW)

def right(x):
	GPIO.output(ForwardB,)

#drive
""" pA.ChangeDutyCycle(35)
pB.ChangeDutyCycle(100) """
#backward(5)
while True:
	key = input()
	if key == 'w':
		forward(2)
	elif key == 's':
		backward(2)

#backward(5)


	#pA.ChangeDutyCycle(75)
	#left(1)

GPIO.cleanup()
