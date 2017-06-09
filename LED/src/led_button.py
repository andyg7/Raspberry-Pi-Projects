import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red_switch_pin = 23
blue_switch_pin = 24
yellow_switch_pin = 25

input_to_output = {23: 4, 24: 17, 25: 27}

led_order = [4, 17, 27]
for pin in led_order:
	GPIO.setup(pin, GPIO.OUT)

GPIO.setup(red_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(blue_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(yellow_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle_pressed_pin(output_pin):
	if GPIO.input(output_pin) == True:
		GPIO.output(output_pin, False)
	else:
		GPIO.output(output_pin, True)

try:
	while True:
		if GPIO.input(red_switch_pin) == False:
			print "Red button pressed!"
			handle_pressed_pin(input_to_output[red_switch_pin])
		if GPIO.input(blue_switch_pin) == False:
			handle_pressed_pin(input_to_output[blue_switch_pin])
			print "Blue button pressed!"
		if GPIO.input(yellow_switch_pin) == False:
			handle_pressed_pin(input_to_output[yellow_switch_pin])
			print "Yellow button pressed!"
		time.sleep(0.5)
finally:
	print "Cleaning up!"
	GPIO.cleanup()
