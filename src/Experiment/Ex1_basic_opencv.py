# 引用所需数据库
import cv2 #OpenCV库
from pathlib import Path #路径检查
import matplotlib.pyplot as plt #展示图片所需

# 检查OpenCV版本
def opencv():
    print(cv2.__version__)

# def show_im(imN): #cv2.imshow()适用于windows
#     if imN is None:
#         print("Image not found or cannot be opened.")
#         return
#
#     window_name = 'image'
#     cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
#     cv2.imshow(window_name, imN)
#
#     while True:
#         key = cv2.waitKeyEx(50)
#         if key in (ord('q'), ord('Q'), 27):
#             break
#
#         try:
#             is_visible = cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE)
#         except cv2.error:
#             break
#
#         if is_visible < 1:
#             break
#
#     cv2.destroyWindow(window_name)
#
#     for _ in range(5):
#         cv2.waitKey(1)

# 展示图片
def show_im(imN):
    if imN is None:
        print("Image not found or cannot be opened.")
        return
    if len(imN.shape) == 3:
        im_rgb = cv2.cvtColor(imN, cv2.COLOR_BGR2RGB)
        plt.imshow(im_rgb)
    else:
        plt.imshow(imN, cmap='gray')
    plt.axis('off')
    plt.show()

# 读取图片
Image_Dir = Path(__file__).resolve().parent.parent / 'images'
def readim(photo):
    photo_path = Path(photo)

    if not photo_path.is_file():
        photo_path = Image_Dir / photo
    if not photo_path.is_file():
        return None

    im = cv2.imread(str(photo_path))
    return im

# 图片信息
def info(im):

    if(im is None):
        print("Image not found or cannot be opened.")
        return
    height,width=im.shape[:2]
    print("height:",height," width:",width)
    if len(im.shape) == 3:
        print("channels: ", im.shape[2])
    else:
        print("channels: 1")

    print("dtype:", im.dtype)
    print("total pixels:", im.size)

    imG = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    show_im(imG)

# 图片裁切
def crop_im(im, x1, y1, x2, y2):
    imC=im[y1:y2, x1:x2]
    return imC

# 裁切
def CropIm(imN):
    # while True:
    if imN is None:
        print("Image not found or cannot be opened.")
        return
    print("Image Info :", imN.shape[0], "x", imN.shape[1])
    while True:
         x1=int(input("Enter x1:"))
         x2=int(input("Enter x2:"))
         y1=int(input("Enter y1:"))
         y2=int(input("Enter y2:"))
         if x1>=0 and y1>=0 and x2<=imN.shape[1] and y2<=imN.shape[0]:
            break
    imcrop=crop_im(imN, x1, y1, x2, y2)
    show_im(imcrop)

# 菜单
def manu(photo):
    im = readim(photo)
    names=["Show im","Info","Crop Im"]
    x=1
    for i in names:
        print(str(x) + ": " + i)
        x+=1
    choice=input("Enter a choice (x to exit):")
    while choice != 'x':
        if choice == '1':
            show_im(im)
        elif choice == '2':
            info(im)
        elif choice == '3':
            CropIm(im)
        choice=input("Enter a choice (x to exit):")
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #opencv()
    mode=input("Choose your photo (x to exit):")
    while mode != 'x':
        manu(mode)
        mode = input("Choose your photo (x to exit):")
    #os.system('clear')
    # print("Welcome to Image Info")
    # while True:
    #     im=input("Enter a photo, or x to exit: ")
    #     if im == 'x':
    #         break
    #     info(im)
    # print("Welcome to Image Crop")
    # CropIm()
    #os.system('clear')
