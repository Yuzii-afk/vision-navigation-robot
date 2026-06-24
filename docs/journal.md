# Development Journal

---

## 2026-6-23
### Objective
set up a new development environment for the project.
### Tasks completed
- Installed necessary software and tools.
- Configured version control system (Git) and ssh authentication.
- Installed OpenCV.
- uploaded initial project files to the repository.
### Problems encountered
- Git push failed due to authentication issues.
- Repository histories diverged.
### Solution
- Resolved by generating a new SSH key and adding it to the GitHub account.
- Used `git pull --rebase` to synchronize the local repository with the remote repository.
### Reflections
Today I learned the basics of Git and GitHub. Although the setup process took time, it will make future development easier.
### Next steps
- Starting to learn about colour selection algorithms.
- Organise the project structure using folders.

---

## 2026-6-24
### Objective
Implement a basic colour selection algorithm using RGB colour space.
### Tasks completed
- Researched algorithms for colour selection in RGB space.
- Implemented red colour selection thresholding using OpenCV.
- Showing the selected red areas in the image.
### Problems encountered
- Do not know how to apply the mask to the original image.
### Research Notes
See in `docs/Research.md` for details on RGB colour selection and OpenCV functions.
### Solution
- Used `cv2.bitwise_and()` to apply the mask to the original image.
- Apply `mask.astype(np.uint8) * 255` to convert `[True, False, False]` into `1 or 0` which is `white or black`.
### Reflections
Today I learned how to implement a basic colour selection algorithm using OpenCV. I also learned how to apply a mask to an image.
### Next steps
- Imporve the colour selection algorithm.
- Implement how to draw on the image.