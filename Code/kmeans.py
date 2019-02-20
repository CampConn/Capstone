import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.image as mpimg    # img reading
from scipy import misc
import numpy as np
from sklearn.datasets import load_digits
from scipy.stats import mode
from sklearn.metrics import accuracy_score

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
png = read_img("png\\")
jpeg = read_img("jpeg\\")
print("--------------------------\n")
png_feed = png.reshape(png.shape[0] * png.shape[1] * png.shape[2], 1) * 255.
jpeg_feed = jpeg.reshape(jpeg.shape[0] * jpeg.shape[1] * jpeg.shape[2], 1)

# KMEANS
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(jpeg_feed)
labels = kmeans.labels_

# read a test
test = read_img("test\\")
test = test.reshape(480 * 640, 1)

# predict
result = kmeans.predict(test)
result = result.reshape(480, 640)
show_img(result)