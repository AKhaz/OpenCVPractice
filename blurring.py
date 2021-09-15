import numpy as np
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

blurred = np.hstack([cv2.blur(image, (3, 3)), cv2.blur(image, (5, 5)), cv2.blur(image, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# cv2.destroyAllWindows()
blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0), cv2.GaussianBlur(image, (5, 5), 0), cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

blurred = np.hstack([cv2.medianBlur(image, 3), cv2.medianBlur(image, 5), cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)
