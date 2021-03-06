"""
segmentation of each characters from the number plate
"""
import numpy as np
from skimage.transform import resize
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import CCA1

# The invert was done so as to convert the black pixel to white pixel and vice versa
number_plate = np.invert(CCA1.num_plate_like_objects[0])

labelled_plate = measure.label(number_plate)

# plotting the number plate
fig, ax1 = plt.subplots(1)
ax1.imshow(number_plate, cmap="gray")

# the next two lines is based on the assumptions that
# the width of the characters should be between 5% and 15% of the number plate,
# and height should be between 35% and 60%
min_height, max_height, min_width, max_width = (0.35 * number_plate.shape[0], 0.60 * number_plate.shape[0],
                                                0.03 * number_plate.shape[1], 0.15 * number_plate.shape[1])

# list for storing all the detected characters
characters = []
counter = 0

# for correct sequence of the characters of the number plate
column_list = []

for regions in regionprops(labelled_plate):
    # y0, x0 : min row, min col  coordinates
    # y1, x1 : max row, max col  coordinates
    y0, x0, y1, x1 = regions.bbox
    region_height = y1 - y0
    region_width = x1 - x0

    if min_height < region_height < max_height and min_width < region_width < max_width:
        # roi : region of interest
        roi = number_plate[y0:y1, x0:x1]

        # draw a red bordered rectangle over the character.
        rect_border = patches.Rectangle((x0, y0), x1 - x0, y1 - y0, edgecolor="yellow",
                                        linewidth=2, fill=False)
        ax1.add_patch(rect_border)

        # resize the characters to 20X20 and then append each character into the characters list
        resized_char = resize(roi, (20, 20))
        characters.append(resized_char)

        # this is just to keep track of the arrangement of the characters
        column_list.append(x0)

print("Displaying segmented characters from the number plate...\n")
plt.show()
