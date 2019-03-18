import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff
from sklearn import svm

# Oh, I finally understand how this will work.
# Essentially, X is your training data.
# Y is your definitions.
# When you call predict, it takes in data like X and returns an expected Y.
# To Do:
# So now that I know what to do here's a nice list to get me the rest of the way:
# Read in X from one raw image.
# Read Y in from one photoshop mask.
# Pick the prediction method that is curved. There was a good example on the wiki.
# Make predictions for all images.
# Output files will create .pngs.
# Stretch goal, use all 21 images to build the neural network (this could be slow AF).

# x = [[50, 80, 230], [120, 150, 52]]
# y = [1, 0]
# clf = svm.SVC(gamma='scale')
# clf.fit(x, y)
# print(clf.predict([[60, 120, 80]]))
# >>> [0]

def maskPngToBooleanList(mask, x1=0, y1=0, x2=639, y2=479):
    boolList = []
    truthErrors = 0

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            if(np.array_equal(mask[y][x], [1.0, 1.0, 1.0, 1.0])):
                boolList.append(1)
            elif(np.array_equal(mask[y][x], [0.0, 0.0, 0.0, 1.0])):
                boolList.append(0)
            else:
                truthErrors += 1
                boolList.append(0)
                # print("Truth Error Coords | Row: " + str(x) + " | " + "Column: " + str(y))

    return boolList

