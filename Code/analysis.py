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

# All I want to do is print out the integer counter for these four states.
# I am expecting to manually record them.
# This script can be given two directories.
# When given two directories it can compare all images of the same name.
