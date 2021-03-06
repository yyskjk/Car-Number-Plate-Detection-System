"""
Matching the number plate like objects from the binary formatted car image
"""
from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import binaryimage

# grouping of all the connected regions
label_image = measure.label(binaryimage.binary_car_image)

# setting the min, max height and min, max width that a license plate can be
min_height, max_height, min_width, max_width = (0.10 * label_image.shape[0], 0.20 * label_image.shape[0], 
                                                0.20 * label_image.shape[1], 0.40 * label_image.shape[1])
num_plate_objects_coordinates = []
num_plate_like_objects = []

# Plotting the image on which the num plate will be marked
fig, (ax1) = plt.subplots(1)
ax1.imshow(binaryimage.gray_car_image, cmap="gray")

# module regionprops creates a list of properties of all the labelled regions
for region in regionprops(label_image):
    # if the region is so small then it's likely not a license plate
    if region.area < 50:
        continue

    # the bounding box coordinates
    min_row, min_col, max_row, max_col = region.bbox
    region_height = max_row - min_row
    region_width = max_col - min_col

    # ensuring that the region identified satisfies the condition of a typical license plate
    if min_height <= region_height <= max_height and min_width <= region_width <= max_width and \
            region_width > region_height:
        num_plate_like_objects.append(binaryimage.binary_car_image[min_row:max_row, min_col:max_col])
        num_plate_objects_coordinates.append((min_row, min_col, max_row, max_col))
        rectBorder = patches.Rectangle((min_col, min_row), max_col - min_col, max_row - min_row,
                                       edgecolor="darkgreen", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
    # let's draw a red rectangle over those regions

print("Displaying car image with rectangle over number plate like objects...\n")
plt.show()
