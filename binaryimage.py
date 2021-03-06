"""
Reading the car image and changing it to binary format for better recognition of number plate
car image --> grayscale format --> binary format
"""
from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt

# Enter the car image path whose number plate we want to detect
input_car = "test/car1.jpg"

# reading the image
car_image = imread(input_car, as_gray=True)

# print(car_image.shape)  -->  returns 2D array

# A grey scale pixel in sk-image ranges between 0 & 1.
# Multiplying it with 255 will make it range between 0 & 255(something we can relate better with).
gray_car_image = car_image * 255

# plotting the images
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image, cmap="gray")

threshold_value = threshold_otsu(gray_car_image)
# We now need to convert it to a binary image in which a pixel is either complete black or white.
binary_car_image = gray_car_image > threshold_value

ax2.imshow(binary_car_image, cmap="gray")

print("Displaying the car image in grayscale and binary format...\n")
plt.show()
