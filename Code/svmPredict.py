import os                           # Lists files in a directory
import csv                          # CSV handling
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Special array functionality
from sklearn import svm             # Support Vector Machine
from joblib import dump, load       # SVM Model Persistence

def getRectangles(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(
            csvFile, delimiter=',', quotechar='|'))

        return rectangleReader

# To do: Ensure SVM to prediction doesn't break.
# Follow instructions as much as possible.

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

def pngToList(mask, x1=0, y1=0, x2=639, y2=479):
# Original Line which may be faster (but I don't fully understand):
# x = inputImage.reshape(307200, -1)
    pixelList = []

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            pixelList.append(mask[y][x])

    return pixelList

def svmPredictionToMask(boolList, x1=0, y1=0, x2=639, y2=479):
    mask = []
    boolListIndex = 0

    for row in range(0, 640):
        if(row < y1):
            for column in range(0, 480):
                mask[row][column].append([0, 0, 0])
        elif(row > y2):
            for column in range(0, 480):
                mask[row][column].append([0, 0, 0])
        else:
            for column in range(0, 480):
                if(column < x1):
                    mask[row][column].append([0, 0, 0])
                elif(column > x2):
                    mask[row][column].append([0, 0, 0])
                else:
                    if(boolList[boolListIndex] == 0):
                        mask[row][column].append([0, 0, 0])
                    elif(boolList[boolListIndex] == 1):
                        mask[row][column].append([255, 255, 255])
                    boolListIndex += 1

    return mask

### Main
trainingImagePath = "Robot Arm Pictures\\Originals\\1548556410125876173.jpeg"
trainingMaskPath = "Robot Arm Pictures\\Photoshop Masks\\1548556410125876173.png"
svmMaskPath = "Robot Arm Pictures\\SVM Test Images\\1548556410125876173.png"

print("Setting up images, x, and y without rectangle...")
inputImage = mpimg.imread(trainingImagePath)
inputMask = mpimg.imread(trainingMaskPath)
print("Images completed.")
x = pngToList(inputImage)
print("X completed.")
y = maskPngToBooleanList(inputMask)
print("Y completed.")

print("Setting up SVM.")
clf = svm.SVC(gamma='auto')
# clf = svm.SVC(gamma='scale')
print("SVM gamma set to 'auto'.")
clf.fit(x, y)
print("SVM fitted. Making predictions on input.")
predictedMaskBoolList = clf.predict(x)
print("Predictions complete. Converting to a mask.png.")
predictedMask = svmPredictionToMask(predictedMaskBoolList)
print("Image ready to be saved. Saving now.")
mpimg.imsave(svmMaskPath, predictedMask)
print("Image saved. The svm.py script has completed.")
