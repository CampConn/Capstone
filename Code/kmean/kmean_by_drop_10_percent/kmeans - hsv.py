import os
from PIL import Image
import colorsys
import csv
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
        #print(filename)
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
    #print(path, 'set shape = ', set.shape)

    return set

### change pixels val
def change_pixels(result, list, png):
    data = read_csv()
    white = 3
    n = 0
    for i in data:
        # get coords
        left_x =  int(i[1])
        left_y =  int(i[2])
        right_x = int(i[3])
        right_y = int(i[4])

        for x in range(result.shape[1]):
            for y in range(result.shape[2]):
                if (y >= left_x and y <= right_x and x >= left_y and x <= right_y):
                    temp = np.array(result[n][x][y])
                    temp = temp.reshape(1, 3)
                    for j in list:
                        if (temp == j).all():
                            result[n][x][y] = white
                    #if (temp == list[0]).all():
                    #    result[n][x][y] = white
                    #elif (temp == list[1]).all():
                    #    result[n][x][y] = white
                    #elif (temp == list[2]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[3]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[4]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[5]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[6]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[7]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[8]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[9]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[10]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[11]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[12]).all():
                    #    result[n][x][y] = 0
                    #elif (temp == list[13]).all():
                    #    result[n][x][y] = 0
                    #else:
                    #    result[n][x][y] = 0
        # save
        print(n)
        x = np.array(result[n])
        x = greyscale(x)
        #y = np.array(png[n])
        #x = np.concatenate( ( x, y ), axis = 0 )
        fname = 'hsv_%d.png' % n
        misc.imsave(fname, x)
        n += 1
        break;

###        
def HSVColor(img):
    if isinstance(img,Image.Image):
        r,g,b = img.split()
        Hdat = []
        Sdat = []
        Vdat = [] 
        for rd,gn,bl in zip(r.getdata(),g.getdata(),b.getdata()) :
            h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

###
def read_csv():
    data = csv.reader(open('rectangles.csv', 'r'))
    return data

###
def set_rectangles(jpeg):
    data = read_csv()
    idx = 0
    for i in data:
        # get coords
        left_x =  int(i[1])
        left_y =  int(i[2])
        right_x = int(i[3])
        right_y = int(i[4])

        # change val
        for m in range(jpeg[idx].shape[0]):
            for n in range(jpeg[idx].shape[1]):
                if (not(n >= left_x and n <= right_x and m >= left_y and m <= right_y)):
                    jpeg[idx][m][n] = 0.

        idx += 1

    return jpeg

### tohsv
def toHSV(jpeg):
    idx = 0
    for img in jpeg:
        idx += 1
        i = Image.fromarray(img)
        i = HSVColor(i)
        i = np.array(i)

        if idx == 1:
            set = i
        else:
            set = np.concatenate( ( set, i ), axis = 0 )
    return set.reshape(idx, 480, 640, 3)

#### main
png = read_img("png\\", True)
jpeg = read_img("jpeg\\", False)

print('-------------------------toHSV------------------------\n')
jpeg = toHSV(jpeg)

#im=Image.fromarray(jpeg[0])
#im.save('b.jpg')

jpeg_feed = jpeg.reshape(jpeg.shape[0] * jpeg.shape[1] * jpeg.shape[2] * jpeg.shape[3], 1)

# KMEANS
print('-------------------------fit--------------------------\n')
n_clusters = 3
kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(jpeg_feed)


# predict
print('-------------------------predict----------------------\n')
result = kmeans.predict(jpeg_feed)
result = result.reshape(21, 480, 640, 3)
misc.imsave("hsv_test_3.png", result[0])

print('-------------------------set rectangles---------------\n')
result = set_rectangles(result)

np.save('result_hsv.npy', result)
result = np.load('result_hsv.npy')

# match
#print('-------------------------match------------------------\n')

#list = []
#list.append(np.zeros((1, 3)))

#for i in range(result.shape[0]):
#    for x in range(result.shape[1]):
#        for y in range(result.shape[2]):
#            if png[i][x][y] > .9:
#                temp = np.array(result[i][x][y])
#                temp = temp.reshape(1, 3)
#                check = False
#                for k in list:
#                    if (k == temp).all():
#                        check = False
#                        break
#                    else:
#                        check = True
                        
#                if check:
#                    list.append(temp)
#    #break

#list.remove(list[0])
#print(len(list))
#print(list)

#np.save('list_hsv.npy', list)
#list = np.load('list.npy')


# change pixels
#change_pixels(result, list, png)

# accuracy
#print( accuracy_score(, ) )