# This document will explain the process of `red_coor.py`
## Main Steps
1. `Last_centre` contain the last coordinate of object. If is `None` then use global search.
2. `Global search` search in the whole frame and where `Local` search around `Last_centre`.
3. Preprocess the image.
4. Generate mask of frame.
5. find contour.
6. find coordinate.
7. save in the `Last_centre`.

## Global search
1. resize the whole picture with factor `1/4`.
2. finding coordinates.
3. calculate initial centre.
4. store values and turn to local search `ROI`

## Local search
1. Area around `Last_centre`.
2. finding coordinates.
3. if lost turn to global.
4. if get coordinates.
   - store the values
   - searching around the centre