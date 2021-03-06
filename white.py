import cv2
import numpy as np
import matplotlib.pyplot as plt
daun = cv2.imread('download (1).jpg')
daun = cv2.cvtColor(daun, cv2.COLOR_BGR2RGB)
hsv_daun = cv2.cvtColor(daun, cv2.COLOR_RGB2HSV)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_daun, light_white, dark_white)
result_white = cv2.bitwise_and(daun, daun, mask=mask_white)

plt.subplot(2, 2, 1)
plt.imshow(daun)
plt.axis('off')
plt.title("Original Image")
plt.subplot(2, 2, 2)
plt.imshow(hsv_daun)
plt.axis('off')
plt.title("HVS Image")
plt.subplot(2, 2, 3)
plt.imshow(mask_white)
plt.axis('off')
plt.title("Mask Image")
plt.subplot(2, 2, 4)
plt.imshow(result_white)
plt.axis('off')
plt.title("Hasil Image")
plt.show()