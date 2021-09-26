from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
argP.add_argument("-s", "--size", required = False, help = "Size of largest color bin")
argP.add_argument("-b", "--bins", required = False, help = "Number of bins per color channel", default = 8)
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orginal", image)
size = float(args["size"])
bins =int(args["bins"])

#Convert to Grayscale image format
#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imageMask = np.zeros((image.shape[0], image.shape[1], 3), dtype = "uint8")
#image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

#Make white border mask
imageMask[0:(image.shape[0]), 0:(image.shape[1]//6)] = (255, 255, 255)
imageMask[0:(image.shape[0]), (image.shape[1] - (image.shape[1]//6)): (image.shape[1])] = (255, 255, 255)
imageMask[0:(image.shape[0]//6), 0:(image.shape[1])] = (255, 255, 255)
imageMask[(image.shape[0] - (image.shape[0]//6)):(image.shape[0]), 0:(image.shape[1])] = (255, 255, 255)


#convert the mask to grayscale so I can add the contour mask as well.
imageMask = cv2.cvtColor(imageMask, cv2.COLOR_BGR2GRAY)
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grayImage = cv2.GaussianBlur(image, (5,5), 0)
cannyImage = cv2.Canny(grayImage, 30, 150)
cv2.imshow("Canny Mask", cannyImage)

newImageMask = cv2.bitwise_xor(imageMask, cannyImage)
cv2.imshow("Added Masks", newImageMask)
invertedImage = cv2.bitwise_not(image)
cv2.imshow("Inverted Original", invertedImage)
mixedImages = cv2.bitwise_and(invertedImage, image, mask = newImageMask)
cv2.imshow("Final Result", mixedImages)


hist = cv2.calcHist([mixedImages], [0, 1, 2], None, [bins,bins,bins], [0, 256, 0 , 256, 0 , 256])

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ratio = size / np.max(hist)

for (x, plane) in enumerate(hist):
    for (y, row) in enumerate(plane):
        for (z, col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio * hist[x][y][z]
                rgb = (z / (bins - 1), y / (bins - 1), x / (bins - 1))
                ax.scatter(x, y, z, s = siz, facecolors = rgb)

plt.show()
cv2.waitKey(0)
