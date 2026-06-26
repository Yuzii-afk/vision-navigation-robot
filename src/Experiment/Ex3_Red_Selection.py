import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


# 获取路径
def path_img(path):
    Dir_path = Path(__file__).resolve().parent.parent.parent / 'images'
    img_path = Path(path)
    if not img_path.exists():
        img_path = Dir_path / img_path
    if not img_path.exists():
        return None
    return img_path

def read_img(path):
    if path is None:
        print("not such file or directory")
        return path

    img = cv2.imread(str(path))
    return img

def show_img(img):
    if len(img.shape) == 3:
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(im_rgb)
    elif len(img.shape) == 2:
        plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()

# 选择颜色
def colour_red(img):
    if len(img.shape) < 3:
        print("a single channel image, no color selection")
        return
    # 获取通道 RGB
    # B = img[:, :, 0]
    # G = img[:, :, 1]
    # R = img[:, :, 2]

    # 选择红色 - absolute red
    # mask = (R > 150) & (G < 100) & (B < 100)

    # 选择红色 - relative red
    # mask = (R > 80) & (R > G * 1.3) & (R > B * 1.3)

    # mask = mask.astype(np.uint8)
    # mask = mask * 255


    # HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # change into HSV
    # Red range 1
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    # Red range 2
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    # Add two ranges
    mask = mask1 + mask2

    # Map to original image
    # img = cv2.bitwise_and(img, img, mask=mask)

    return img, mask

def find_largest_red(img, mask):
    # 生成轮廓
    # 在mask二值图上做计算，img上面画图

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("no contours")
        return
    else:
        # 找到contours列表里面最大的contours
        largest_contour = max(contours, key=cv2.contourArea)
        # 获取面积 Area
        area = cv2.contourArea(largest_contour)
        if area < 100:
            print("object too small")
        else:
            x, y, w, h = cv2.boundingRect(largest_contour)

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 6)
            # cv2.rectangle 画矩阵(img 图片，(x,y)左上角坐标,(x+w,y+h)右下角坐标,2 线条粗细)
            cx = x + w / 2
            cy = y + h / 2
            # 中心点
            cv2.circle(img, (int(cx), int(cy)), 5, (255, 255, 255), -1)



if __name__ == '__main__':
    img_name = input("photo:")
    img_pathing = path_img(img_name)
    img = read_img(img_pathing)
    if not img is None:
        red_img, mask = colour_red(img)
        find_largest_red(red_img, mask)
        show_img(red_img)
