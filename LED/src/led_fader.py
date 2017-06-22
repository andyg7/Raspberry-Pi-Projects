import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

pwm_red = GPIO.PWM(18, 500)

pwm_green = GPIO.PWM(23, 500)

pwm_blue = GPIO.PWM(24, 500)

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
		color_s = input("Color? 1->red 2->green 3-blue")
		curr_pwm.stop()
		if is_int(color_s) is False:
			continue
		color = int(color_s)
		if color not in num_to_pwm:
			continue
		curr_pwm = num_to_pwm[color]
		curr_pwm.start(100)
		duty_s = input("Brightness between 0 and 100")
		if is_int(duty_s) is False:
			continue
		duty = int(duty_s)
		curr_pwm.ChangeDutyCycle(duty)

finally:
	print 'Cleaning up!'
	GPIO.cleanup()
