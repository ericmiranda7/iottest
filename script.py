import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

ForwardA=26
BackwardA=20
ForwardB=5
BackwardB=6

sleeptime=1

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ForwardA, GPIO.OUT)
	GPIO.setup(BackwardB, GPIO.OUT)
	GPIO.setup(ForwardB, GPIO.OUT)
	GPIO.setup(BackwardB, GPIO.OUT)

def forward(x):
	init()
	GPIO.output(ForwardA, GPIO.HIGH)
	GPIO.output(ForwardB, GPIO.HIGH)
	print("Moving Forward")
	time.sleep(x)
	GPIO.output(ForwardA, GPIO.LOW)
	GPIO.output(ForwardB, GPIO.LOW)
	GPIO.cleanup()

def reverse(x):
	init()
	GPIO.output(BackwardA, GPIO.HIGH)
	GPIO.output(BackwardB, GPIO.HIGH)
	print("Moving Backward")
	time.sleep(x)
	GPIO.output(BackwardA, GPIO.LOW)
	GPIO.output(BackwardB, GPIO.LOW)
	GPIO.cleanup()

while (1):
	forward(5)
	reverse(5)
