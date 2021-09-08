import numpy as np
import argparse
import imutils
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped on Y axis", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped on X axis", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped on both axes", flipped)

cv2.waitKey(0)
