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
def read_img(path, if_gscale):
    i = 0
    for filename in os.listdir(path):
        i += 1
        print(filename)
        hand = mpimg.imread(path + filename)
        if if_gscale:
            hand = greyscale(hand)
        else:
            hand = hand[...,:3]
        if i == 1:
            set = np.array(hand)
        else:  
            set = np.concatenate( ( set, np.array(hand) ), axis = 0 )

    if if_gscale:
        set = set.reshape( i, 480, 640)
    else:
        set = set.reshape( i, 480, 640, 3)
    print(path, 'set shape = ', set.shape)

    return set

# change pixels val
def change_pixels(result, list, png):
    white = 3
    grey = 2
    for n in range(result.shape[0]):
        for x in range(result.shape[1]):
            for y in range(result.shape[2]):
                temp = np.array(result[n][x][y])
                temp = temp.reshape(1, 3)
                if (temp == list[0]).all():
                    result[n][x][y] = white
                elif (temp == list[1]).all():
                    result[n][x][y] = white
                elif (temp == list[2]).all():
                    result[n][x][y] = white
                elif (temp == list[3]).all():
                    result[n][x][y] = white
                elif (temp == list[4]).all():
                    result[n][x][y] = white
                elif (temp == list[5]).all():
                    result[n][x][y] = white
                elif (temp == list[6]).all():
                    result[n][x][y] = white
                elif (temp == list[7]).all():
                    result[n][x][y] = white
                elif (temp == list[8]).all():
                    result[n][x][y] = white
                elif (temp == list[9]).all():
                    result[n][x][y] = 0
                elif (temp == list[10]).all():
                    result[n][x][y] = white
                elif (temp == list[11]).all():
                    result[n][x][y] = white
                elif (temp == list[12]).all():
                    result[n][x][y] = white
                elif (temp == list[13]).all():
                    result[n][x][y] = white
                else:
                    result[n][x][y] = 0
        # save
        print(n)
        x = np.array(result[n])
        x = greyscale(x)
        y = np.array(png[n])
        x = np.concatenate( ( x, y ), axis = 0 )
        fname = 'test_%d.png' % n
        misc.imsave(fname, x)
        

### main
png = read_img("png\\", True)

jpeg = read_img("jpeg\\", False)
jpeg_feed = jpeg.reshape(jpeg.shape[0] * jpeg.shape[1] * jpeg.shape[2] * jpeg.shape[3], 1)


## KMEANS
#print('-------------------------------------------------\nfit\n')
#n_clusters = 4
#kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(jpeg_feed)


## predict
#print('predict')
#result = kmeans.predict(jpeg_feed)
#result = result.reshape(21, 480, 640, 3)
#misc.imsave("test.png", result[0])



#np.save('result.npy', result)
result = np.load('result.npy')

# mask
print("--------------------------\n")

list = []
list.append(np.zeros((1, 3)))

for i in range(result.shape[0]):
    for x in range(result.shape[1]):
        for y in range(result.shape[2]):
            if png[i][x][y] > .9:
                temp = np.array(result[i][x][y])
                temp = temp.reshape(1, 3)
                check = False
                for k in list:
                    if (k == temp).all():
                        check = False
                        break
                    else:
                        check = True
                        
                if check:
                    list.append(temp)
    #break

list.remove(list[0])
print(len(list))
print(list)




#np.save('list.npy', list)
#list = np.load('list.npy')


# change pixels
change_pixels(result, list, png)

# accuracy
#print( accuracy_score(, ) )