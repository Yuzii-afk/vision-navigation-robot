import cv2
import numpy as np
# import time

# Dynamic v value
def get_adaptive_v_range(frame):
    channel_v = frame[:,:,2]

    mean_v = np.mean(channel_v)
    std_v = np.std(channel_v)

    dynamic_v_min = max(60, int(mean_v - 1.5 * std_v))

    return dynamic_v_min, 255

# Get mask of frame
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

def find_contour(mask):
    # Find contour
    contour, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best_contour = None
    max_area = 0

    for cnt in contour:
        area = cv2.contourArea(cnt)

        if area < 200:
            continue

        if area > max_area:
            max_area = area
            best_contour = cnt

    if best_contour is not None:
        return best_contour, max_area
    else:
        return None , None


def preprocess(frame):
    blur = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    ini_mask = get_red_mask(hsv_frame)

    # Morphology

    # kernel = np.ones((5, 5), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    opening = cv2.morphologyEx(ini_mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    # contour
    best_contour , area = find_contour(closing)

    if best_contour is not None:
        return best_contour , area
    else:
        return None, None

def get_coordinates(frame):

    # preprocess the frame
    best_contour , area = preprocess(frame)

    if best_contour is None:
        return None , None

    # Find centre
    M = cv2.moments(best_contour)

    # if M is 0
    if M['m00'] != 0:
        coor_x = int(M['m10'] / M['m00'])
        coor_y = int(M['m01'] / M['m00'])
    else:
        x, y, w, h = cv2.boundingRect(best_contour)
        coor_x = int(w / 2) + x
        coor_y = int(h / 2) + y

    return coor_x , coor_y

def global_search(frame):
    # Get resized img
    resize_scale = 4
    # Get height and width 获取图片长宽
    y , x = frame.shape[:2]
    # Calculate New image 计算新图像大小
    new_x = x // resize_scale
    new_y = y // resize_scale

    resized = cv2.resize(frame, (new_x, new_y))

    local_x , local_y = get_coordinates(resized)

    if local_x is None or local_y is None:
        return None

    abs_x = int(local_x * resize_scale)
    abs_y = int(local_y * resize_scale)
    new_centre = np.array([abs_x, abs_y])
    return new_centre

def crop_roi(frame, centre, roi_size):
    # Get height and width
    h, w = frame.shape[:2]
    cx, cy = centre

    radius = roi_size // 2

    x1 = cx - radius
    y1 = cy - radius
    x2 = cx + radius
    y2 = cy + radius

    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(x2, w)
    y2 = min(y2, h)

    if x2 < x1 or y2 < y1:
        return None, (0 ,0)

    roi = frame[y1:y2, x1:x2]

    return roi, x1, y1

def local_search(frame , coordinates):
    roi , x1, y1 = crop_roi(frame, coordinates, roi_size=300)

    if roi is None:
        return global_search(frame)

    local_x, local_y = get_coordinates(roi)
    if local_x is None or local_y is None:
        return None
    abs_x = local_x + x1
    abs_y = local_y + y1
    centre = np.array([abs_x, abs_y])
    return centre


# last_centre=None
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("not readable")
#         break
#
#     start = time.time()
#     if last_centre is None:
#         last_centre = global_search(frame)
#     else:
#         new_centre = local_search(frame, last_centre)
#         if new_centre is not None:
#             last_centre = new_centre
#         else:
#             last_centre = None
#
#     if last_centre is not None:
#         # cx, cy = last_centre
#         # cv2.circle(frame, (int(cx), int(cy)), 5, (255, 255, 255), -1)
#         # cv2.imshow("img", frame)
#         # cv2.waitKey(1)
#         print(f"FPS: {1 / (time.time() - start):.1f}")
#         print("last centre found:" , last_centre)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
#
# cap.release()
# cv2.destroyAllWindows()