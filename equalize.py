import numpy as np
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())


image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
