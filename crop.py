import numpy as np
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

cropped = image[250:500, 250:500]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
