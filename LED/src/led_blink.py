import RPi.GPIO as GPIO
import time

led_pin_1 = 4
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin_1, GPIO.OUT)

try:
	while True:
		if GPIO.input(led_pin_1) == 1:
			GPIO.output(led_pin_1, False)
		else:
			GPIO.output(led_pin_1, True)
		time.sleep(2)
	
finally:
	print "Cleaning up!"
	GPIO.cleanup()
	
