import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_order = [4, 17, 27]
led_pin_1 = led_order[0]
led_pin_2 = led_order[1]
led_pin_3 = led_order[2]


for pin in led_order:
	GPIO.setup(pin, GPIO.OUT)

try:
	while True:
		for pin in led_order:
			GPIO.output(pin, True)
			time.sleep(2)
		for pin in led_order:
			GPIO.output(pin, False)
		time.sleep(2)
finally:
	print "Cleaning up!"
	GPIO.cleanup()
	
