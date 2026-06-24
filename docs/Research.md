# General knowledge and research
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