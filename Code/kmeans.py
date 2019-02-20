import os
# TO DO: Delete all unnecessary references (load_digits; accuracy_score; etc)
import matplotlib.pyplot as plt
import matplotlib.image as mpimg    # img reading
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from scipy import misc

# TO DO: Understand this code. Reshape seems to be used too much.

### show
def show_img(img):
    plt.figure('Image')
    plt.imshow(img)
    plt.axis('on')
    plt.title('Image')
    plt.show()

### greyscale
def greyscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

### read
def read_img(path):
    i = 0
    for filename in os.listdir(path):
        i += 1
        print(filename)
        hand = mpimg.imread(path + filename)
        hand = greyscale(hand)
        if i == 1:
            set = np.array(hand)
        else:  
            set = np.concatenate( ( set, np.array(hand) ), axis = 0 )
    set = set.reshape( i, 480, 640)
    print(path, 'set shape = ', set.shape)
    return set

### main
# png = read_img("png\\")
raw = read_img("..\\Robot Arm Pictures\\Originals")
print("--------------------------\n")
# png_feed = png.reshape(png.shape[0] * png.shape[1] * png.shape[2], 1) * 255.
rawFeed = raw.reshape(raw.shape[0] * raw.shape[1] * raw.shape[2], 1)

# KMEANS
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(rawFeed)
labels = kmeans.labels_

# read a test
test = read_img("test\\")
test = test.reshape(480 * 640, 1)

# predict
result = kmeans.predict(test)
result = result.reshape(480, 640)
show_img(result)