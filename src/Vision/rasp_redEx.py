from red_coor import *
from picamera2 import Picamera2

last_centre=None
picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (1536, 864)},
    controls={
        "ExposureTime": 20000,
        "AwbEnable": False
    }
)
picam2.configure(config)

picam2.start()

import time
time.sleep(0.5)

fps_counter = 0
fps_timer = time.time()

while True:
    frame_rgb = picam2.capture_array()
    frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    start = time.time()
    if last_centre is None:
        last_centre = global_search(frame)
    else:
        new_centre = local_search(frame, last_centre)
        if new_centre is not None:
            last_centre = new_centre
        else:
            last_centre = None

    fps_counter += 1
    if time.time() - fps_timer >= 1.0:
        print(f"FPS: {fps_counter}")
        fps_counter = 0
        fps_timer = time.time()

    if last_centre is not None:
        print("last centre found:", last_centre)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
#
# cap.release()
# cv2.destroyAllWindows()