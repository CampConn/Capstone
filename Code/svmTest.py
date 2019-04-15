import csv                          # CSV handling
import numpy as np                  # Special array functionality
from sklearn import svm             # Support Vector Machine
from joblib import dump, load       # SVM Model Persistence

def getPixelDataFromCSV(csvPath):
    pixelFeatureSet = np.array([], dtype=np.uint8)
    pixelClassSet = np.array([], dtype=np.uint8)
    counter = 0

    with open(csvPath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for pixel in reader:
            counter += 1
            # if(counter % 5000 == 0):
                # print('Progress: ' + str(counter))
            
            if(int(pixel['inRectangle']) == 1):
                pixelFeatures = np.array([int(pixel['red']), int(pixel['green']), int(pixel['blue'])])
                pixelClass = np.array(int(pixel['class']))
                pixelFeatureSet = np.concatenate((pixelFeatureSet, pixelFeatures), axis=0)
                pixelClassSet = np.concatenate((pixelClassSet, pixelClass), axis=None)

    pixelFeatureSet = pixelFeatureSet.reshape(int(len(pixelFeatureSet) / 3), 3)

    return (pixelFeatureSet, pixelClassSet, counter)

def calculateAccuracy(predictedClasses, truthClasses):
    truePositive = 0
    trueNegative = 0
    falsePositive = 0
    falseNegative = 0
    predictionCounter = 0

    for truthClass in truthClasses:
        if(truthClass == 0):
            if(predictedClasses[predictionCounter] == 0):
                trueNegative += 1
            elif(predictedClasses[predictionCounter] == 1):
                falsePositive += 1
        elif(truthClass == 1):
            if(predictedClasses[predictionCounter] == 0):
                falseNegative += 1
            elif(predictedClasses[predictionCounter] == 1):
                truePositive += 1
        predictionCounter += 1
    
    return (truePositive, trueNegative, falsePositive, falseNegative, predictionCounter)

def printResults(totalPixels, resolution, truePositive, trueNegative, falsePositive, falseNegative):
    noRectangleTrueNegative = trueNegative + (resolution - totalPixels)
    print("-----------------------------------------------")
    print("Total resolution pixels: " + str(resolution))
    print("True positives: " + str(truePositive) + " at " + str(truePositive * 100 / resolution))
    print("True negatives: " + str(noRectangleTrueNegative) + " at " + str(noRectangleTrueNegative * 100 / resolution))
    print("False positives: " + str(falsePositive) + " at " + str(falsePositive * 100 / resolution))
    print("False negatives: " + str(falseNegative) + " at " + str(falseNegative * 100 / resolution))
    if(totalPixels != resolution):
        print("Rectangle pixels: " + str(totalPixels) + " which is " + str(totalPixels * 100 / resolution) + "% of the image.")
        print("Rectangle true positives: " + str(truePositive) + " at " + str(truePositive * 100 / totalPixels))
        print("Rectangle true negatives: " + str(trueNegative) + " at " + str(trueNegative * 100 / totalPixels))
        print("Rectangle false positives: " + str(falsePositive) + " at " + str(falsePositive * 100 / totalPixels))
        print("Rectangle false negatives: " + str(falseNegative) + " at " + str(falseNegative * 100 / totalPixels))
    print("====><====")
    print("In rectangle accuracy: " + str(
        (truePositive * 100 / totalPixels) + (trueNegative * 100 / totalPixels)
    ))
    print("Total accuracy: " + str(
        (truePositive * 100 / resolution) + (noRectangleTrueNegative * 100 / resolution)
    ))
    print("-----------------------------------------------")
    print()

### Main
testingPixelsCSV = "Data\\Formatted Pixel Data\\testingPixelsGroup1.csv"
modelOutputPath = "Data\\SVM Group Models\\svmLinearModelGroup1.joblib"
previousGroup = 1

for(i in range(1, 8)):
    if(i != previousGroup):
        testingPixelsCSV = testingPixelsCSV.replace(str(previousGroup), str(i))
        modelOutputPath = modelOutputPath.replace(str(previousGroup), str(i))
        previousGroup = i

    # print("Loading CSV into NumPy array.")
    (pixelFeatureSet, pixelClassSet, testPixelCount) = getPixelDataFromCSV(testingPixelsCSV)
    # print("NumPy arrays loaded. Setting up SVM.")
    clf = load(modelOutputPath)
    # print("SVM loaded. Making predictions...")
    predictedClassList = clf.predict(pixelFeatureSet)
    # print("Predictions complete. Calculating accuracy.")
    (truePositive, trueNegative, falsePositive, falseNegative, predictionCount) = calculateAccuracy(predictedClassList, pixelClassSet)
    # print("Accuracy calculated, now printing.")
    printResults(predictionCount, testPixelCount, truePositive, trueNegative, falsePositive, falseNegative)