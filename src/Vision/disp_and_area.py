import cv2
import numpy as np

def get_adaptive_v_range(frame):
    channel_v = frame[:,:,2]

    mean_v = np.mean(channel_v)
    std_v = np.std(channel_v)

    dynamic_v_min = max(60, int(mean_v - 1.5 * std_v))

    return dynamic_v_min, 255

def get_red_mask(img):
    v_min, v_max = get_adaptive_v_range(img)

    lower_red1 = np.array([0, 120, v_min])
    upper_red1 = np.array([10, 255, v_max])
    mask1 = cv2.inRange(img, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, v_min])
    upper_red2 = np.array([180, 255, v_max])
    mask2 = cv2.inRange(img, lower_red2, upper_red2)

    mask = mask1 + mask2
    return mask

def get_disparity(x, width):
    centre_line = width//2

    # If central 是否在中心
    if centre_line-10 <= x <= centre_line+10:
        return 0

    else:
        # Calculate disparity 计算偏差
        disp = x - centre_line
        percentage = float(disp/centre_line)

        # Positive means on the right 正数代表右
        # Otherwise means on the left 反之则依然

        return percentage # Float number between -1 and 1

def get_area(frame, cx, cy, width = 1536, height = 864):
    roi = 500

    x1 = cx - roi
    y1 = cy - roi
    x2 = cx + roi
    y2 = cy + roi

    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(x2, width)
    y2 = min(y2, height)

    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    ini_mask = get_red_mask(hsv_frame)

    # Morphology

    # kernel = np.ones((5, 5), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))

    opening = cv2.morphologyEx(ini_mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # contour
    contour, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0

    for cnt in contour:
        area = cv2.contourArea(cnt)

        if area < 300:
            continue

        if area > max_area:
            max_area = area

    return max_area
# width = 1000
# for i in range(0,1000):
#     print(get_disparity(i,width))