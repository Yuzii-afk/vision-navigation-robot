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
    # 获取通道
    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    # 选择红色 - absolute red
    # mask = (R > 150) & (G < 100) & (B < 100)

    # 选择红色 - relative red
    mask = (R > 80) & (R > G * 1.3) & (R > B * 1.3)

    mask = mask.astype(np.uint8)
    mask = mask * 255
    img = cv2.bitwise_and(img, img , mask = mask)

    return img


if __name__ == '__main__':
    img_name = input("photo:")
    img_pathing = path_img(img_name)
    img = read_img(img_pathing)
    if not img is None:
        img = colour_red(img)
        show_img(img)
