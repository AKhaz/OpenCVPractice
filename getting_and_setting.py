from __future__ import print_function
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path to Image")
newArgs = vars(argP.parse_args())

image = cv2.imread(newArgs["image"])
cv2.imshow("Original", image)

(b,g,r) = image[0,0]
print("Da pixel at 0,0 has RGB Values" + str(r) + " - " + str(g) + " - " + str(b))

image[0,0] = (255, 0 , 0)
(b, g, r) = image[0,0]
print("Da pixel at 0,0 has RGB Values" + str(r) + " - " + str(g) + " - " + str(b))

corner = image[image.shape[0]-100:image.shape[0], image.shape[1]-100:image.shape[1]]
cv2.imshow("Corner", corner)

image[image.shape[0]-100:image.shape[0], image.shape[1]-100:image.shape[1]] = (0,0,255)

cv2.imshow("Updated", image)
cv2.waitKey(0)
