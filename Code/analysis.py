import os
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_digits
from scipy import misc
from scipy.stats import mode
import matplotlib.pyplot as plt
import matplotlib.image as mpimg    # img reading
import numpy as np

# # TO DO: Understand this code. Reshape seems to be used too much.

# ### show
# def show_img(img):
#     plt.figure('Image')
#     plt.imshow(img)
#     plt.axis('on')
#     plt.title('Image')
#     plt.show()

# ### greyscale
# def greyscale(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# Okay, here's what I need to do:
# Read image 1, image 2
# Compare pixel by pixel.
# Image 1 is "truth"
# Image 2 is "kmeans"
# True positive is when they agree on white.
# True negative is when they agree on black.
# False positive is when kmeans says white when truth says black.
# False negative is when kmeans says black when truth says white.

# All I want to do is print out the integer counter for these four states.
# I am expecting to manually record them.
# This script can be given two directories.
# When given two directories it can compare all images of the same name.

