# General knowledge and research

---

### General useful Python Functions and utilities.
#### numpy
- `name.astype(np."datatype")` is converting the data type of `name`.
  - example: `mask.astype(np.uint8)` make `mask` become a 8 bits unsigned integer (0-255).
  - `np.uint8` unsigned integer 8 bits.
  - `np.float32` 32 bits floating point.
  - `np.int32` 32 bits signed integer.
  - `np.bool_` boolean type.

---
### RGB colour selection
- Colour selection algorithms:
  - RGB represents the intensity of red, green, and blue channels in an image.
  - `mask` is a balck and white image.
    - White pixels represent the selected colour.
    - Black pixels represent the unselected colours.
    - `mask = (R > 150) & (G < 100) & (B < 100)` can be used to select red areas.
- OpenCV functions:
  - `cv2.bitwise_and(p1 , p2, mask=mask_name)` can be used to apply the mask to the original image.
    - `p1` is the first image join the calculate and `p2` is the second image.
    - `mask = mask_ name` is the mask to apply.
      - when mask is `1` represent stay and `0` will make it black.
  - `mask = mask.astype(np.uint8)` is converting `[true,false,false]` into `1 or 0`
    - .astype(np.uint8) is converting the boolean mask into 1 & 0
    - np.uint8 is a data type in NumPy that represents an `8-bit unsigned integer` 0-255.
  - `mask.astype(np.uint8) * 255` results `0 or 255` which is `white or black` 
  
---
### Locating the centre of a detected object
- OpenCV functions:
  - HVS #色彩空间
    - More accurate than RGB selection.
    - Wider range of colour selection.
```python
import cv2
import numpy as np
rgb_image = cv2.imread("image_path")
# Convert RGB to HSV 从BRG到HSV图像
hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BRG2HSV)
# Select the colour选择颜色
colour_min = np.array([0, 100, 100])  # Lower bound of the colour in HSV 下限阈值
colour_max = np.array([10, 255, 255])  # Upper bound of the colour in HSV 上限阈值
mask = cv2.inRange(hsv_image, colour_min, colour_max)
```
  - Contours
    ```python
    import cv2
    IMG = cv2.imread("IMG_PATH")
    
    contours, hierarchy = cv2.findContours(IMG, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # mask -> the binary image 黑白图
    # cv2.RETR_EXTERNAL -> retrieve only the external contours 只找外轮廓
    # cv2.CHAIN_APPROX_SIMPLE -> compresses horizontal, vertical, and diagonal segments
    # -> 压缩轮廓点，减少数据量
    # hierarchy -> relationship between contours. 轮廓之间子父关系
    
    largest_contour = max(contours, key=cv2.contourArea)# 在刚刚建立的列表找最大红色
    area = cv2.contourArea(largest_contour) # 获取面积
    x, y, w, h = cv2.boundingRect(largest_contour) # 获取x和y以及宽和长
    
    ```
#### Sources
- https://pyimagesearch.com/2016/02/01/opencv-center-of-contour/?utm_source=chatgpt.com [article] (2026-6-25)

- https://www.geeksforgeeks.org/computer-vision/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-with-cv-inrange-opencv/ [article] (2026-6-25)

- https://www.geeksforgeeks.org/python/python-opencv-find-center-of-contour/ [article] (2026-6-25)
---