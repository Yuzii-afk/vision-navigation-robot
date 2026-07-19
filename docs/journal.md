# Development Journal

---

## 2026-6-23
### Objective
set up a new development environment for the project.
### Tasks completed
- Installed necessary software and tools.
- Configured version control system (Git) and ssh authentication.
- Installed OpenCV.
### Problems encountered
- Git push failed due to authentication issues.
- Repository histories diverged.
### Solution
- Resolved by generating a new SSH key and adding it to the GitHub account.
- Used `git pull --rebase` to synchronise the local repository with the remote repository.
### Reflections
Today I learned the basics of Git and GitHub. Although the setup process took time, it will make future development easier.

CN：今天建立了github仓库，学习了基础的git操作。途中遇到过很多困难，比如权限问题，和同步问题。但github仓库管理让以后项目更简单。
### Next steps
- Starting to learn about colour selection algorithms.
- Organise the project structure using folders.
- Transfer repository onto raspberry.

---

## 2026-6-24
### Objective
Implement a basic colour selection algorithm using RGB colour space.  Set up connection on the Raspberry ship.
### Tasks completed
- Researched algorithms for colour selection in RGB space.
- Implemented red colour selection thresholding using OpenCV.
- Showing the selected red areas in the image.
- Uploaded initial project files to the repository.
- Clone github repository onto my raspberry.
- Authenticated raspberry pi.
### Problems encountered
- Do not know how to apply the mask to the original image.
### Research Notes
See in `docs/Research.md` for details on RGB colour selection and OpenCV functions.
### Solution
- Used `cv2.bitwise_and()` to apply the mask to the original image.
- Apply `mask.astype(np.uint8) * 255` to convert `[True, False, False]` into `1 or 0` which is `white or black`.
### Reflections
Today I learned how to implement a basic colour selection algorithm using OpenCV. I also learned how to apply a mask to an image.
Additionally, connect my raspberry pi to my git account and clone the whole repository.

CN: 今天学习并实现了基础的OpenCV操作，包括基于RGB色彩空间的红色筛选，以及如何生成并施加mask黑白图。
同时将我的Raspberry pi连接到我的账户上，并下载已有的仓库。
### Next steps
- Imporve the colour selection algorithm.
- Implement how to draw on the image.

---

## 2026-6-25
### Objective
- Acquire the centre position of the detected red object.
- Learn how to draw on the image.
### Tasks completed
- Apply HSV algorithm to original colour selection.
- Found the contours of the shape.
- Found the rectangle around the shape.
- Found the centre and area of the rectangle.
- Draw the rectangle on the image.
### Problem encountered
- `cv2.findContour(img,  cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)` failed due to the wrong datatype of image.
### Solution
- Used `mask` instead of `img` which is appropriate dtype of image.
### Refelction
Today I have learnt the most interested knowledge since I started project so far.
I understood how to find the **contour** of selected area using `cv2.findContour()`.
Also learnt how to acquire and draw the rectangle around largest contour.

CN: 今天学会了如何找到选中区域的外轮廓，说实话这是我目前学到过最有意思的知识。我还学会了如何绘制轮廓外接长方形，以及其中心点。
### Next steps
- Drawing rectangle using vedio stream.
- Find the distance between centre of object and centre of screen/image/frame.

--- 

## 2026-7-3
### Objective
- Implement Video tracking using openCV on MacOS.
- Strengthen colour selection algorithm.
### Task completed
- Threshold of video stream colour tracking.
### Task Unsolved
- Unprcise colour tracking.
### Problem encountered
- `cv2.waitKey(0)` Not updating video stream.
### Solution
- Using `cv2.waitKey(1)` to update window.
### Refecltion
Today I have learnt the thresholding of the video colour tracking.

CN: 今天学会了基础的视频流获取画面再进行颜色追踪。
### Next steps
- Acquire the point location of the object.
- Improve colour selection algorithm.

---

## 2026-7-4 to 12
### Objective
- Buy hardware required.
  - Including:
    - Car chassis
    - Motor & wheels x 4
    - multimeter
    - Batteries
    - Charger
- Construct the chassis.
- Test the motor.
### Task completed
- Construct the chassis and motor.
- Test the motor and let it work.
### Problem encountered
- How to connect each different elements.
### Solution
- Search online and follow supplier instruction
### Next steps
Get coordinates of the object ready to calculate "central disparity".

---

## 2026-7-13
### Objective
- Improve colour selection to overcome different light surrounding.
- Acquire coordinates of object during the video and print it.
### Task completed
`red_coor.py`
#### Include
- Optimise photo resize technic.
  - `ROI`
  - `Resize frame`
- Preprocessing each frame.
- Dynamic HSV value.
- Locating object.
- Morphology
### Problem encountered
- Previous HSV which is constant does not work perfectly under different surrounding.
- Raspberry pi 5 work only 5 frames per second with unoptimised algorithm.
### Solution
- Apply dynamic `v value`.
- Implement `ROI` and `cv2.resize` to optimise the algorithm.
### Next steps
- Hardware control & associate camera with wheels.

---

## 2026-7-16
### Objective
- Calculate percentage error of red object from the central line.
- Read the area of object to calculate the distance.
- Ready for hardware investigation.
### Task completed
- New function in `disp_and_area.py`.
  - Percentage different of object.
  - Area of the object.
### Problem encountered
- Complicate the algorithm by name the side and calculate seperatly.
### Solution
- Using signed number to label right or left.
### Next steps
Control hardware using python code.

---

## 2026-7-17
### Objective
- Thresholding of hardware control
### Task completed
- Connect each different port to raspberry.
- Simple code control the motor.
- Set up config code.
### Problem encountered
- Wheels do not spin.
- Two wheels spin in a different direction.
- Cannot read `config.py`
### Solution
- Testing voltage of wires.
- Adapt connection of the wires.
- add `echo 'export PYTHONPATH="/home/yuzii/vision-navigation-robot/src:$PYTHONPATH"' >> ~/.bashrc
source ~/.bashrc` to bash
### Next steps
Cooperation between camera and motor.

---

## 2026-7-19
### Objective
- Implement steering code to the car.
- Implement motion code to the car.
### Task completed
- Wrote `steering.py` to implement threshold of direction control.
- Wrote `motion.py` to control when to stop the car.
### Problem encountered
- Speed of two side motor is simply adding to previous.
  Resulting in the car cannot change direction.
### Solution
- Recalculate each side in each cycle base on defult speed.