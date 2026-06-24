import cv2
import numpy as np

image = cv2.imread("sample_leaf.jpg.png")
image = cv2.resize(image, (300, 300))
green = np.mean(image[:, :, 1])
print("Green Value:", green)

if green > 100:
    print("Healthy Plant")
else:
    print("Diseased Plant")
