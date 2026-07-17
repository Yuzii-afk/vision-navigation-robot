from motor import *
import config as cfg
import time
motor_left = motor(cfg.PWMA_LEFT, cfg.AIN1_LEFT, cfg.AIN2_LEFT)

motor_right = motor(cfg.PWMA_RIGHT, cfg.AIN1_RIGHT, cfg.AIN2_RIGHT)

print("forward")
motor_right.motor_spin(100)
motor_left.motor_spin(100)
time.sleep(3)

print("stop")
motor_right.motor_stop()
motor_left.motor_stop()
time.sleep(2)

print("backward")
motor_right.motor_spin(-100)
motor_left.motor_spin(-100)
time.sleep(3)