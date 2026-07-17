from Vision import red_coor
from Hardware import motor
import config as cfg
from picamera2 import Picamera2

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