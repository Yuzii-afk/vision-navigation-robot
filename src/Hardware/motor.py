import RPi.GPIO as GPIO

class motor:
    def __init__(self, PWMA, AIN1, AIN2):
        self.PWMA = PWMA
        self.AIN1 = AIN1
        self.AIN2 = AIN2

        # Only do once 只做一次
        if not hasattr(GPIO, 'mode_set') or GPIO.mode_set is None:
            GPIO.setmode(GPIO.BCM)
            GPIO.mode_set = True

        GPIO.setup(self.PWMA, GPIO.OUT)
        GPIO.setup(self.AIN1, GPIO.OUT)
        GPIO.setup(self.AIN2, GPIO.OUT)

        self.pwm = GPIO.PWM(self.PWMA, 1000)  # 频率 1kHz
        self.pwm.start(0)

    def motor_spin(self, speed):
        # Between -100 and 100
        if(speed > 0):
            GPIO.output(self.AIN1, GPIO.HIGH)
            GPIO.output(self.AIN2, GPIO.LOW)
            self.pwm.ChangeDutyCycle(min(speed, 100))
        elif(speed < 0):
            GPIO.output(self.AIN1, GPIO.LOW)
            GPIO.output(self.AIN2, GPIO.HIGH)
            self.pwm.ChangeDutyCycle(min(abs(speed), 100))
        else:
            self.pwm.ChangeDutyCycle(0)

    def motor_stop(self):
        self.pwm.ChangeDutyCycle(0)

    def motor_cleanup(self):
        self.pwm.stop()