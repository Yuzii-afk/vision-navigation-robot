import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PWMA = 12
AIN1 = 23
AIN2 = 24

GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

pwm = GPIO.PWM(PWMA, 1000)
pwm.start(0)

def motor_spin(speed):
    if(speed > 0):
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        pwm.ChangeDutyCycle(min(speed, 100))
    elif(speed < 0):
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        pwm.ChangeDutyCycle(min(abs(speed), 100))
    else:
        pwm.ChangeDutyCycle(0)

try:
    print("Motor Spin clockwise 3s")
    motor_spin(60)
    time.sleep(3)

    print("Motor Stop 1s")
    motor_spin(0)
    time.sleep(1)

    print("Motor Spin anti-clockwise 3s")
    motor_spin(-60)
    time.sleep(3)

    motor_spin(0)

except KeyboardInterrupt:
    print("Stopping motors")

finally:
    print("Cleaning up")
    pwm.stop()
    GPIO.cleanup()