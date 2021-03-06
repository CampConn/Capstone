import os                           # Lists files in a directory
import csv                          # CSV handling
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Special array functionality
from sklearn import svm             # Support Vector Machine
from joblib import dump, load       # SVM Model Persistence

# This function is no longer needed...
def smallestRectangle(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(
            csvFile, delimiter=',', quotechar='|'))

        # Possible To Do: Parse through CSV to find best rectangle
        # Only necessary if the csv changes a lot or is given a large amount of data.
        # for rectangleRow in rectangleReader:
        #   parse for smallest x2 - x1 and y2 - y1
        #   result can't be 0, must actually find a rectangle

        return rectangleReader[20]

# This function is no longer needed...
# Note, this function can be optimized for nearest neighbor groupings.
def jpegToList(mask, x1=0, y1=0, x2=639, y2=479):
    pixelList = np.array([], dtype=np.uint8).reshape(0, 3)

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            # Helpful data debug statement
            # print("Mask: " + str(mask[y][x]) + " at x[" + str(x) + "] y[" + str(y) + "].")
            pixelList = np.concatenate((pixelList, np.array([mask[y][x]])), axis=0)

    return pixelList

# This function is no longer needed...
def maskPngToBooleanList(mask, x1=0, y1=0, x2=639, y2=479):
    boolList = np.array([], dtype=np.uint8)
    truthErrors = 0

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            # Helpful data debug statement
            # print("Mask: " + str(mask[y][x]) + " at x[" + str(x) + "] y[" + str(y) + "].")
            if(np.array_equal(mask[y][x], [1.0, 1.0, 1.0, 1.0])):
                boolList = np.append(boolList, 1)
            elif(np.array_equal(mask[y][x], [0.0, 0.0, 0.0, 1.0])):
                boolList = np.append(boolList, 0)
            else:
                truthErrors += 1
                boolList = np.append(boolList, 0)

    return boolList

### Outdated Main
trainingImagePath = "Robot Arm Pictures\\Originals"
trainingMaskPath = "Robot Arm Pictures\\Photoshop Masks"
rectangleCSVPath = "Data\\rectangles.csv"
modelOutputPath = "Data\\svmLinearModelGroup1.joblib"

print("Using CSV to get best rectangle.")
rectangle = smallestRectangle(rectangleCSVPath)
pngFile = rectangle[0]
jpegFile = pngFile.replace("png", "jpeg")
x1 = int(rectangle[1])
y1 = int(rectangle[2])
x2 = int(rectangle[3])
y2 = int(rectangle[4])

print("Setting up images, x, and y with rectangle.")
inputImage = mpimg.imread(trainingImagePath + "\\" + jpegFile)
inputMask = mpimg.imread(trainingMaskPath + "\\" + pngFile)
print("Images completed.")
x = jpegToList(inputImage, x1, y1, x2, y2)
print("X completed.")
y = maskPngToBooleanList(inputMask, x1, y1, x2, y2)
print("Y completed.")
# Helpful data debug statements
# print("X: " + str(x))
# print("Y: " + str(y))
# print("X len: " + str(len(x)))
# print("Y len: " + str(len(y)))

print("Setting up SVM.")
# Kernel's are rbf, linear, poly, sigmoid and "precomputed" (I don't think I should do precomputed)
# Gamma's are auto, scale
clf = svm.SVC(kernel='linear', gamma='scale', verbose=True, cache_size=500)
print("SVM gamma set to 'scale'.")
print("Beginning to fit data... (This will take a while.)")
clf.fit(x, y)
print("SVM fitted. Saving SVM model for repeated use.")
dump(clf, modelOutputPath)
print("SVM Model saved.")
