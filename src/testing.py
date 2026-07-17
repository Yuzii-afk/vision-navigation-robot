from Vision.red_coor import *
from Vision.disp_and_area import *
from Hardware.motor import *
import config as cfg

from picamera2 import Picamera2
import cv2
import RPi.GPIO as GPIO

last_centre=None
picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (cfg.CAMERA_WIDTH, cfg.CAMERA_HEIGHT)},
    controls={
        "ExposureTime": cfg.EXPOSURE_TIME,
        "AwbEnable": cfg.AWB_ENABLE
    }
)
picam2.configure(config)

picam2.start()

import time
time.sleep(0.5)

motor_left = motor(cfg.PWMA_LEFT, cfg.AIN1_LEFT, cfg.AIN2_LEFT)
motor_right = motor(cfg.PWMA_RIGHT, cfg.AIN1_RIGHT, cfg.AIN2_RIGHT)

speed_left = cfg.BASE_SPEED
speed_right = cfg.BASE_SPEED
speed_difference = 10
direction = 0
while True:
    frame_rgb = picam2.capture_array()
    frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    if last_centre is None:
        last_centre = global_search(frame)
    else:
        new_centre = local_search(frame, last_centre)
        if new_centre is not None:
            last_centre = new_centre
        else:
            last_centre = None


    if last_centre is None:
        motor_left.motor_stop()
        motor_right.motor_stop()
        continue

    cx, _ = last_centre
    _ , width = frame.shape[:2]

    direction = get_disparity(cx , width) * speed_difference

    speed_left = speed_left + direction*speed_difference
    speed_right = speed_right - direction*speed_difference

    motor_left.motor_spin(speed_left)
    motor_right.motor_spin(speed_right)

    print("direction:", direction)

motor_left.motor_stop()
motor_right.motor_stop()
motor_left.motor_cleanup()
motor_right.motor_cleanup()
GPIO.cleanup()