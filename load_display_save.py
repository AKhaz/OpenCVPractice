from __future__ import print_function
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path to Image")
newArgs = vars(argP.parse_args())
newImage = cv2.imread(newArgs["image"])
print("Width: {} Pixels".format(newImage.shape[1]))
print("Height: {} Pixels".format(newImage.shape[0]))
print("Channels: {}".format(newImage.shape[2]))

cv2.imshow("Image", newImage)
cv2.waitKey(0)
cv2.imwrite("newImage.jpg", newImage)
