import cv2

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

def area(contour):
    area = cv2.contourArea(contour)
    return area

# width = 1000
# for i in range(0,1000):
#     print(get_disparity(i,width))