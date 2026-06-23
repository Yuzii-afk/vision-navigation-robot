import numpy as np
import cv2


def hsvGraph(frame):
    HsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower1 = np.array([35, 80, 80])
    upper1 = np.array([85, 255, 255])

    # lower2 = np.array([160, 100, 100])
    # upper2 = np.array([179, 255, 255])
    # mask1 = cv2.inRange(HsvFrame, lower1, upper2)
    mask = cv2.inRange(HsvFrame, lower1, upper1)
    # mask = cv2.bitwise_or(mask1, mask2)
    cv2.imshow('mask', mask)
    cv2.waitKey(0)

if __name__ == '__main__':
    # 0 表示默认摄像头。如果你有多个摄像头，可以尝试改成 1、2。
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('无法打开摄像头')
        exit()

    while True:
        # ret 表示是否成功读取到画面，frame 是当前这一帧图像。
        ret, frame = cap.read()

        if not ret:
            print('无法读取摄像头画面')
            break

        #name = "Red object"
        #cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        #cv2.imshow('Camera', frame)

        #plt.imshow(frame)

        # waitKey(1) 表示等待 1 毫秒读取键盘输入。
        # 按 q 键退出实时画面。
        hsvGraph(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break




    cap.release()
    cv2.destroyAllWindows()
