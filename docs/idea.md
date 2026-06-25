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

## Current Algorithm

### Relative RGB Red Selection

The first red detection method used fixed RGB thresholds. This worked in simple cases, but it can miss red objects when lighting changes.

The current method uses relative RGB values:

```python
mask = (R > 80) & (R > G * 1.3) & (R > B * 1.3)
```

This means a pixel is selected when:

- The red channel is bright enough.
- The red channel is clearly stronger than the green channel.
- The red channel is clearly stronger than the blue channel.

This method is easier to understand at the current learning stage than HSV thresholding.

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

## Next Vision Step

The next step is not only selecting red pixels, but also understanding where the red object is.

Planned steps:

1. Generate a red mask.
2. Find the contours of the red area.
3. Select the largest contour as the target object.
4. Calculate the centre point of the target object.
5. Draw the centre point on the image.

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

- Improve red detection using HSV colour space.
- Detect the centre of a red object.
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
