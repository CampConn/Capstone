import csv                          # Used to read and write CSVs.
import sys                          # To do: Use sys to implement argv.
import matplotlib.image as mpimg    # Used to open images
import numpy as np                  # Special array functionality
import random                       # Used to pick random pixels

def getRectangles(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(csvFile, delimiter=',', quotechar='|'))

        return rectangleReader

def getPixelValue(pixel):
    if(str(pixel).find("[") == -1):
        return pixel
    else:
        if((pixel[0] == 0.) and (pixel[1] == 0.) and (pixel[2] == 0.)):
            return 0
        elif((pixel[0] == 1.) and (pixel[1] == 1.) and (pixel[2] == 1.)):
            return 1
        else:
            return -1

    pngFile = rectangle[0]
    jpegFile = pngFile.replace("png", "jpeg")
    x1 = int(rectangle[1])
    y1 = int(rectangle[2])
    x2 = int(rectangle[3])
    y2 = int(rectangle[4])
    inputImage = mpimg.imread(trainingImagePath + "\\" + jpegFile)

    for y in range(y1, (y2 + 1)):
        for x in range(x1, (x2 + 1)):
            

    return (trainingData, innerTestingData, outerTestingData)

### Main
# rectangleCSVPath = "Data\\trainingPixels.csv"
# rectangleCSVPath = "Data\\testingPixels.csv"
# truthPath = "Robot Arm Pictures\\Photoshop Masks"


# Everytime I process an image, I want to add it to the CSV.
