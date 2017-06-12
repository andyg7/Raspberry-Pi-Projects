import RPi.GPIO as GPIO

led_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 500)
pwm_led.start(100)

try:
	while True:
		duty_s = input("Enter brightness between 0 and 100:\n")
		duty = int(duty_s)
		pwm_led.ChangeDutyCycle(duty)
finally:
	print "Cleaning up!"
	GPIO.cleanup()

