import cv2
import matplotlib.pyplot as plt
import numpy as np

pertama = cv2.imread('maple.png')
pertama = cv2.cvtColor(pertama, cv2.COLOR_BGR2RGB)
hsv_pertama = cv2.cvtColor(pertama, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_pertama, light_orange, dark_orange)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_pertama, light_white, dark_white)
final_mask = mask + mask_white
pertamaa = cv2.bitwise_and(pertama, pertama, mask=final_mask)


kedua = cv2.imread('download (1).jpg')
kedua = cv2.cvtColor(kedua, cv2.COLOR_BGR2RGB)
hsv_kedua = cv2.cvtColor(kedua, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_kedua, light_orange, dark_orange)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_kedua, light_white, dark_white)
final_mask = mask + mask_white
keduaa = cv2.bitwise_and(kedua, kedua, mask=final_mask)


ketiga = cv2.imread('pohon.jpg')
ketiga  = cv2.cvtColor(ketiga , cv2.COLOR_BGR2RGB)
hsv_ketiga  = cv2.cvtColor(ketiga , cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_ketiga, light_orange, dark_orange)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_ketiga, light_white, dark_white)
final_mask = mask + mask_white
ketigaa = cv2.bitwise_and(ketiga, ketiga, mask=final_mask)


keempat = cv2.imread('daun (4).png')
keempat = cv2.cvtColor(keempat, cv2.COLOR_BGR2RGB)
hsv_keempat = cv2.cvtColor(keempat, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_keempat, light_orange, dark_orange)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_keempat, light_white, dark_white)
final_mask = mask + mask_white
keempatt = cv2.bitwise_and(keempat, keempat, mask=final_mask)


kelima = cv2.imread('ranting.png')
kelima = cv2.cvtColor(kelima, cv2.COLOR_BGR2RGB)
hsv_kelima = cv2.cvtColor(kelima, cv2.COLOR_RGB2HSV)
light_orange = (1, 190, 200)
dark_orange = (18, 255, 255)
mask = cv2.inRange(hsv_kelima, light_orange, dark_orange)
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_kelima, light_white, dark_white)
final_mask = mask + mask_white
kelimaa = cv2.bitwise_and(kelima, kelima, mask=final_mask)


plt.figure(figsize=(10, 10))

plt.subplot(5,5,1)
plt.axis('off')
plt.imshow(pertama)

plt.subplot(5, 5, 2)
plt.axis('off')
plt.imshow(kedua)

plt.subplot(5, 5, 3)
plt.axis('off')

plt.imshow(ketiga)

plt.subplot(5, 5, 4)
plt.axis('off')
plt.imshow(keempat)

plt.subplot(5,5, 5)
plt.axis('off')
plt.imshow(kelima)


plt.subplot(5, 5, 6)
plt.imshow(pertamaa)
plt.axis('off')

plt.subplot(5, 5, 7)
plt.imshow(keduaa)
plt.axis('off')

plt.subplot(5, 5, 8)
plt.imshow(ketigaa)
plt.axis('off')
plt.title("(a)Citra Original atau Input")

plt.subplot(5, 5, 9)
plt.imshow(keempatt)
plt.axis('off')

plt.subplot(5, 5, 10)
plt.imshow(kelimaa)
plt.axis('off')

plt.subplot(5, 5, 13)

plt.axis('off')
plt.title("(b) Citra Output/Tersegmentasi")



plt.show()