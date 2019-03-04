import os
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from scipy import misc
from scipy.stats import mode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg    # img reading
import numpy as np

truthPath = 'Robot Arm Pictures\\Photoshop Masks'
kmeansPath = 'Robot Arm Pictures\\K-means Strawman'

print('\nTruth Images')
for truthFile in os.listdir(truthPath):
    print(truthFile)

print('\nK-means Images')
for kmeansFile in os.listdir(kmeansPath):
    print(kmeansFile)

# Okay, here's what I need to do:
# Read image 1, image 2
# Compare pixel by pixel.
# Image 1 is "truth"
# Image 2 is "kmeans"
# True positive is when they agree on white.
# True negative is when they agree on black.
# False positive is when kmeans says white when truth says black.
# False negative is when kmeans says black when truth says white.
truthPath = "Robot Arm Pictures\\Photoshop Masks"
kmeansPath = "Robot Arm Pictures\\K-means Strawman"

for truthFile in os.listdir(truthPath):
    for kmeansFile in os.listdir(kmeansPath):
        if(truthFile == kmeansFile):
            print("Found a match with file: " + truthFile)
            truthImage = mpimg.imread(truthPath + "\\" + truthFile)
            kmeansImage = mpimg.imread(kmeansPath + "\\" + kmeansFile)
            truePositive = 0
            trueNegative = 0
            falsePositive = 0
            falseNegative = 0
            truthErrors = 0
            kmeansErrors = 0
            totalPixels = 0
            x = 0
            y = 0

            for row in truthImage:
                for truthPixel in row:
                    totalPixels += 1
                    if(np.array_equal(truthPixel, [1.0, 1.0, 1.0, 1.0])):
                        if(np.array_equal(truthPixel, kmeansImage[x][y])):
                            truePositive += 1
                        elif(np.array_equal(kmeansImage[x][y], [0.0, 0.0, 0.0, 1.0])):
                            falseNegative +=1
                        else:
                            kmeansErrors += 1
                    elif(np.array_equal(truthPixel, [0.0, 0.0, 0.0, 1.0])):
                        if(np.array_equal(truthPixel, kmeansImage[x][y])):
                            trueNegative += 1
                        elif(np.array_equal(kmeansImage[x][y], [1.0, 1.0, 1.0, 1.0])):
                            falsePositive +=1
                        else:
                            kmeansErrors += 1
                    else:
                        truthErrors += 1
                    y += 1
                y = 0
                x += 1
