import numpy as np
import cv2

canvas = np.zeros((1080,1920,3), dtype = "uint8")

for i in range(0, 80):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 1000, size = (2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
