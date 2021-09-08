from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

argP = argparse.ArgumentParser()
argP.add_argument("-i", "--image", required = True, help = "Path of da image")
args = vars(argP.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Orginal", image)

chans = cv2.split(image)
color = ("b", "g", "r")
plt.figure()
plt.title("Flattened Color Histograms")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, color):
    hist = cv2.calcHist([chan], [0], None, [256], [0,256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0,1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color historgram for GB")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[0]], [0,1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color historgram for GR")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0,1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D color historgram for BR")
plt.colorbar(p)

print("2d historgram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
plt.show()

cv2.waitKey(0)
