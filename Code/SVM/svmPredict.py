import os                           # Lists files in a directory
import csv                          # CSV handling
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Special array functionality
import math                         # Needed to define group number
from sklearn import svm             # Support Vector Machine
from joblib import dump, load       # SVM Model Persistence

def getRectangles(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(
            csvFile, delimiter=',', quotechar='|'))

        return rectangleReader

def jpegToList(mask, x1=0, y1=0, x2=639, y2=479):
    pixelList = np.array([], dtype=np.uint8).reshape(0, 3)

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            # Helpful data debug statement
            # print("Mask: " + str(mask[y][x]) + " at x[" + str(x) + "] y[" + str(y) + "].")
            pixelList = np.concatenate(
                (pixelList, np.array([mask[y][x]])), axis=0)

    return pixelList

def svmPredictionToMask(boolList, x1=0, y1=0, x2=639, y2=479):
    mask = []
    boolListIndex = 0

    for row in range(0, 480):
        maskRow = []
        if(row < y1):
            for column in range(0, 640):
                maskRow.append([0., 0., 0.])
        elif(row > y2):
            for column in range(0, 640):
                maskRow.append([0., 0., 0.])
        else:
            for column in range(0, 640):
                if(column < x1):
                    maskRow.append([0., 0., 0.])
                elif(column > x2):
                    maskRow.append([0., 0., 0.])
                else:
                    if(boolList[boolListIndex] == 0):
                        maskRow.append([0., 0., 0.])
                    elif(boolList[boolListIndex] == 1):
                        maskRow.append([1., 1., 1.])
                    boolListIndex += 1
        mask.append(maskRow)

    return mask

### Main
trainingImagePath = "Robot Arm Pictures\\Originals"
svmMaskPath = "Robot Arm Pictures\\Support Vector Machine Images"
rectangleCSVPath = "Data\\rectangles.csv"
modelOutputPath = "Data\\SVM Group Models\\svmLinearModelGroup1.joblib"
fileIterator = 0
previousGroup = 0

print("Grabbing all rectangles from CSV.")
rectangleList = getRectangles(rectangleCSVPath)
print("--------------------------------------------------------")

for rectangle in rectangleList:
    fileIterator += 1
    group = math.floor((fileIterator - 1) / 3) + 1

    if(group != previousGroup):
        modelOutputPath = modelOutputPath.replace(str(previousGroup), str(group))
        print("Loading up SVM model " + str(group) + ".")
        clf = load(modelOutputPath)
        previousGroup = group

    print("Working on file: " + str(fileIterator) + " | Group: " + str(group))
    pngFile = rectangle[0]
    jpegFile = pngFile.replace("png", "jpeg")
    x1 = int(rectangle[1])
    y1 = int(rectangle[2])
    x2 = int(rectangle[3])
    y2 = int(rectangle[4])
    print("Setting up image and cropping to rectangle coordinates.")
    inputImage = mpimg.imread(trainingImagePath + "\\" + jpegFile)
    croppedImage = jpegToList(inputImage, x1, y1, x2, y2)
    print("Cropping completed. Making predictions...")
    predictedMaskBoolList = clf.predict(croppedImage)
    print("Predictions complete. Converting to a mask.png.")
    predictedMask = svmPredictionToMask(predictedMaskBoolList, x1, y1, x2, y2)
    print("Image ready to be saved. Saving now.")
    mpimg.imsave((svmMaskPath + "\\" + pngFile), predictedMask)
    print("Image saved.")
    print("--------------------------------------------------------")
