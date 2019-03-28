import csv                          # CSV handling
import matplotlib.image as mpimg    # Image reading

def getPixelValue(pixel):
    if(str(pixel).find("[") == -1):
        return pixel
    else:
        if((pixel[0] == 0.) and (pixel[1] == 0.) and (pixel[2] == 0.)):
            return 0.
        elif((pixel[0] == 1.) and (pixel[1] == 1.) and (pixel[2] == 1.)):
            return 1.
        else:
            return -1.

def getRectangles(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(
            csvFile, delimiter=',', quotechar='|'))

        return rectangleReader

def performAnalysisOnImages(truthImage, predictionsImage, resolution=307200, x1=0, y1=0, x2=639, y2=479):
    truePositive = 0
    trueNegative = 0
    falsePositive = 0
    falseNegative = 0
    truthErrors = 0
    predictionErrors = 0
    totalPixels = 0
    x = 0
    y = 0
    
    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            totalPixels += 1
            if(getPixelValue(truthImage[y][x]) == 1.):
                if(getPixelValue(predictionsImage[y][x]) == 1.):
                    truePositive += 1
                elif(getPixelValue(predictionsImage[y][x]) == 0.):
                    falseNegative += 1
                else:
                    predictionErrors += 1
            elif(getPixelValue(truthImage[y][x]) == 0.):
                if(getPixelValue(predictionsImage[y][x]) == 0.):
                    trueNegative += 1
                elif(getPixelValue(predictionsImage[y][x]) == 1.):
                    falsePositive += 1
                else:
                    predictionErrors += 1
            else:
                truthErrors += 1
                # print("Truth Error Coords | Row: " + str(x) + " | " + "Column: " + str(y))

    printResults(totalPixels, resolution, truePositive, trueNegative, falsePositive, falseNegative, truthErrors, predictionErrors)

def printResults(totalPixels, resolution, truePositive, trueNegative, falsePositive, falseNegative, truthErrors, predictionErrors):
    noRectangleTrueNegative = trueNegative + (resolution - totalPixels)
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
    if(truthErrors > 0):
        print("Truth errors: " + str(truthErrors))
        # print("Truth errors occur when a pixel in the truth image is not black or white.")
    if(predictionErrors > 0):
        print("Prediction errors: " + str(predictionErrors))
        # print("K-means errors occur when a pixel in the k-means image is not black or white.")
    print("")
    fileIncrementor += 1