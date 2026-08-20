import config as cfg
def side_speed(disparity, KP_TURN, Speed):

    base_speed = Speed
    dire = disparity*KP_TURN

    speed_left = base_speed + dire
    speed_right = base_speed - dire

    speed_left = max(-100, min(speed_left, 100))
    speed_right = max(-100, min(speed_right, 100))

    return speed_left, speed_right

def get_speed(area,max_speed):
    area_max = cfg.AREA_NEAR

    if area >= area_max:
        speed = 0
    else:
        speed = max_speed * 0.4
    return speed