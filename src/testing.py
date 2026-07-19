from Vision.red_coor import *
from Vision.disp_and_area import *
from Hardware.motor import *
import config as cfg
from Control.steering import *

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

max_speed = cfg.MAX_SPEED
base_speed = cfg.BASE_SPEED
speed_difference = cfg.KP_TURN

max_area = cfg.AREA_NEAR
min_area = cfg.AREA_FAR

try:
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
        cx, cy = last_centre
        area = get_area(frame, cx, cy)

        _ , width = frame.shape[:2]
        cal_speed = get_speed(area, max_area, min_area, max_speed)
        direction = get_disparity(cx , width)

        turn = cfg.KP_TURN
        speed_left, speed_right = side_speed(direction, turn, cal_speed)

        motor_left.motor_spin(speed_left)
        motor_right.motor_spin(speed_right)
except KeyboardInterrupt:
    print("Closing")
finally:
    motor_left.motor_stop()
    motor_right.motor_stop()
    motor_left.motor_cleanup()
    motor_right.motor_cleanup()
    GPIO.cleanup()