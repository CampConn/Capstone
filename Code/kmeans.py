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


#for i in range(png_feed.shape[0]):
#    if png_feed[i] < 16.:
#        jpeg_feed[i] = 0


# KMEANS
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(jpeg_feed)
labels = kmeans.labels_
#for i in range(labels.size):
#    if png_feed[i] < 16.:
#        labels[i] = 0
#kmeans.labels_ = labels

# update labels
#labels = np.array(labels)
#labels = labels.reshape(labels.shape[0], 1)



#masks = (labels == png_feed)
#print(masks)


# read a test
test = read_img("test\\")
test = test.reshape(480 * 640, 1)


# predict
result = kmeans.predict(test)
result = result.reshape(480, 640)
show_img(result)



# show typical img
#fig, ax = plt.subplots(2, n_clusters, figsize=(7, 3))
#centers = kmeans.cluster_centers_.reshape(n_clusters, 480, 640)
#for axi, center in zip(ax.flat, centers):
#    axi.set(xticks=[], yticks=[])
#    axi.imshow(center, interpolation='nearest', cmap=plt.cm.binary)
#plt.show()

# accuracy
#print( accuracy_score(clusters_png, clusters_jpeg) )

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