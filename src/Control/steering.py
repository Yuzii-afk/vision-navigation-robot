def side_speed(disparity, KP_TURN, Speed):

    base_speed = Speed
    dire = disparity*KP_TURN

    speed_left = base_speed + dire
    speed_right = base_speed - dire

    speed_left = max(-100, min(speed_left, 100))
    speed_right = max(-100, min(speed_right, 100))

    return speed_left, speed_right

def get_speed(area, area_n, area_f, max_speed):
    area_max = area_n
    area_min = area_f

    if area >= area_max:
        speed = 0
    elif area <= area_min:
        speed = max_speed
    else:
        ratio = (area - area_min) / (area_max - area_min)
        speed = max_speed * (1-ratio)

    return speed