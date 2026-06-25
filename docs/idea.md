# Project Ideas

## Project Goal

Build a Raspberry Pi 5 based autonomous robot that uses computer vision to understand the environment and control movement.

The current project focus is not full autonomy yet. The current focus is learning OpenCV step by step and building a reliable vision pipeline.

## Current Stage

The project is currently in the colour detection stage.

Current experiments:

- `Ex1_basic_opencv.py`: read, display, inspect, and crop images.
- `Ex2_red_object_recognise.py`: test camera input and HSV thresholding.
- `Ex3_Red_Selection.py`: detect red areas from an image using HSV channel selection.

## Current Vision Direction

The current target is to detect a red object from an image or camera frame.

The basic idea is:

1. Read an image or camera frame.
2. Separate the colour channels.
3. Create a mask for red pixels.
4. Use the mask to keep only the red object.
5. Later, calculate the centre position of the detected object.
---
## Current Algorithm

### HSV Red Selection

The next red detection method uses HSV colour space. This allow me to select a wider range of red colours and is more robust.

```python
colour_min = np.array([0, 100, 100])  # Lower bound of the colour in HSV
colour_max = np.array([10, 255, 255])  # Upper bound of the colour in HSV
mask = cv2.inRange(hsv_image, colour_min, colour_max)
```

This method completely replaces the relative RGB method, but it is more complex than RGB.

- It requires converting the image from RGB to HSV.
- It requires understanding the HSV colour space.
- It does not bothered by lighting changes as much as RGB selection.

### Draw a rectangle around the object

This algorithm implement basic function that can draw and find the centre of a rectangle around a red object.

```python
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

if len(contours) == 0:
    print("no contours")
else:
    # 找到contours列表里面最大的contours
    largest_contour = max(contours, key=cv2.contourArea)
    # 获取面积 Area
    area = cv2.contourArea(largest_contour)
    if area < 100:
        print("object too small")
    else:
        x, y, w, h = cv2.boundingRect(largest_contour)

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cv2.rectangle 画矩阵(img 图片，(x,y)左上角坐标,(x+w,y+h)右下角坐标,2 线条粗细)
        cx = x + w / 2
        cy = y + h / 2
        cv2.circle(img, (int(cx), int(cy)), 5, (0, 0, 255), -1)
```
---
## Next Vision Step

The next step is rebost the selection algorithm and put it onto the raspberry pi. Allowing red object tracking using a video stream.

Planned steps:

1. Get frame from a vedio.
2. Find the contours of the red area.
3. Select the largest contour as the target object.
4. Calculate the centre point of the target object.
5. Calculate the area of the object.
6. Draw the centre point on the image.

The centre point can later be used for steering control.

## Future Control Direction

After the red object centre can be detected, the vision result can be connected to robot control.

Basic control idea:

```text
image centre - object centre = position error
position error -> PID controller -> steering adjustment
```

If the object is on the left side of the image, the robot should turn left.

If the object is on the right side of the image, the robot should turn right.

If the object is near the centre, the robot should move forward.

## Future Features

- Improve red detection using HSV colour space. [x]
- Detect the centre of a red object. [x]
- Track the red object using live camera input.
- Add PID steering control.
- Test the system on Raspberry Pi 5.
- Connect camera vision with motor control.
- Add obstacle detection later.

## Current Priorities

1. Make `Ex3_Red_Selection.py` stable and easy to understand.
2. Test red detection with different images.
3. Add object centre detection.
4. Compare RGB and HSV thresholding.
5. Prepare the vision output for robot control.
