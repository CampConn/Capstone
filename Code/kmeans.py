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

### to grayscale
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

### read
def read_img(path):
    i = 0
    for filename in os.listdir(path):
        i += 1
        print(filename)
        hand = mpimg.imread(path + filename)
        grayscale = rgb2gray(hand)
        if i == 1:
            set = np.array(grayscale)
        else:  
            set = np.concatenate( ( set, np.array(grayscale) ), axis = 0 )

    
    set = set.reshape( i, 480, 640)
    print(path, 'set shape = ', set.shape)

    return set

### main
png = read_img("png\\")
jpeg = read_img("jpeg\\")

png_feed = png.reshape(png.shape[0], png.shape[1] * png.shape[2])
jpeg_feed = jpeg.reshape(jpeg.shape[0], jpeg.shape[1] * jpeg.shape[2])

n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
# png
clusters = kmeans.fit_predict(png_feed)
clusters = np.array(clusters)
clusters = clusters.reshape(clusters.shape[0], 1)

# jpeg
clusters_jpeg = kmeans.fit_predict(jpeg_feed)
clusters_jpeg = np.array(clusters_jpeg)
clusters_jpeg = clusters_jpeg.reshape(clusters_jpeg.shape[0], 1)

# show typical png
for i in range(n_clusters):
    print("-----------------------------")
    print("png clusters\t", i, " = ", clusters[i])
    print("jpeg clusters\t", i, " = ", clusters_jpeg[i])

#fig, ax = plt.subplots(2, n_clusters, figsize=(7, 3))
#centers = kmeans.cluster_centers_.reshape(n_clusters, 480, 640)
#for axi, center in zip(ax.flat, centers):
#    axi.set(xticks=[], yticks=[])
#    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
#plt.show()

# accuracy
print( accuracy_score(clusters, clusters_jpeg) )

#digits = load_digits()

#kmeans = KMeans(n_clusters=10, random_state=0)
#clusters = kmeans.fit_predict(digits.data)

#pic = np.array(digits.data)
#pic = pic.reshape(pic.shape[0], 8, 8)
#labels = np.array(digits.target)
#labels = labels.reshape(labels.shape[0], 1)

#i = 0

#print("pic = ", pic.shape)
#print("labels = ", labels.shape)
#print("label is ", labels[i])

#plt.figure('Image')
#plt.imshow(pic[i])
#plt.axis('on')
#plt.title('Image')
#plt.show()

#### show 10 typical number
#fig, ax = plt.subplots(2, 5, figsize=(8, 3))
#centers = kmeans.cluster_centers_.reshape(10, 8, 8)
#for axi, center in zip(ax.flat, centers):
#    axi.set(xticks=[], yticks=[])
#    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
#plt.show()

#### match cluster with label
#labels = np.zeros_like(clusters)
#print("labels is ", labels.shape)
#for i in range(10):
#    mask = (clusters == i)
#    print("mask is ", mask.shape)
#    labels[mask] = mode(digits.target[mask])[0]
#    print(" is ", labels[mask])


#### accuracy
#print( accuracy_score(digits.target, labels) )