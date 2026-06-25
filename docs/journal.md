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