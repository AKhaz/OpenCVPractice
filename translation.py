import numpy as np
import argparse
import imutils
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Downwards and Right Shift", shifted)

shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
