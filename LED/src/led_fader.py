import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

red_pin = 18
green_pin = 23
blue_pin = 24

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

pwm_red = GPIO.PWM(red_pin, 500)
pwm_green = GPIO.PWM(green_pin, 500)
pwm_blue = GPIO.PWM(blue_pin, 500)

num_to_pwm = {1: pwm_red, 2: pwm_green, 3:pwm_blue}

def is_int(i):
	try:
		int(i)
		return True
	except ValueError:
		return False


try:
	curr_pwm = pwm_red
	curr_pwm.start(100)

	while True:
		color_s = input("Color? 1->red 2->green 3-blue\n")
		curr_pwm.stop()
		if is_int(color_s) is False:
			continue
		color = int(color_s)
		if color not in num_to_pwm:
			continue
		curr_pwm = num_to_pwm[color]
		curr_pwm.start(100)
		duty_s = input("Brightness between 0 and 100\n")
		if is_int(duty_s) is False:
			continue
		duty = int(duty_s)
		curr_pwm.ChangeDutyCycle(duty)

finally:
	print 'Cleaning up!'
	GPIO.cleanup()
