import cv2
import matplotlib.pyplot as plt
import numpy as np



image = cv2.imread("pic.jpg", 0)
print('Image type: ', type(image), 'Image dimensions: ', image.shape)
image_copy = np.copy(image)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
lower_green = np.array([0, 100, 0])
upper_green = np.array([254, 255, 254])
mask = cv2.inRange(image_copy, lower_green, upper_green)
plt.imshow(mask, cmap='gray')
plt.show()
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
plt.imshow(masked_image)
plt.show()
background_image = cv2.imread('grass.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
crop_background = background_image[0:342, 0:608]
crop_background[mask == 0] = [0, 0, 0]
plt.imshow(crop_background)
plt.show()
final_image = crop_background + masked_image
plt.imshow(final_image)
plt.show()