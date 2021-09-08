import numpy as np
import argparse
import imutils
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

resized = imutils.resize(image, height = 200)
cv2.imshow("Resized on height", resized)
cv2.waitKey(0)
