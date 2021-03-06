import csv                          # Used to read and write CSVs.
import sys                          # To do: Use sys to implement argv.
import matplotlib.image as mpimg    # Used to open images
import numpy as np                  # Special array functionality
import random                       # Used to pick random pixels
import math                         # Needed for floor function

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

def defineAllPixels(imagePath, maskPath, rectangle, group):
    maskFile = rectangle[0]
    originalFile = maskFile.replace("png", "jpeg")
    x1 = int(rectangle[1])
    y1 = int(rectangle[2])
    x2 = int(rectangle[3])
    y2 = int(rectangle[4])
    original = mpimg.imread(imagePath + "\\" + originalFile)
    mask = mpimg.imread(maskPath + "\\" + maskFile)

    trainingData = []
    outsideRectangle = []

    for y in range(0, 480):
        for x in range(0, 640):
            dataPoint = dict(jpeg=originalFile, group=group)
            if((y >= y1) and (y <= y2)):
                if((x >= x1) and (x <= x2)):
                    dataPoint.update({
                        'red': original[y][x][0],
                        'green': original[y][x][1],
                        'blue': original[y][x][2],
                        'x': x,
                        'y': y,
                        'inRectangle': 1,
                        'class': getPixelValue(mask[y][x])
                    })
                    trainingData.append(dataPoint)
                else:
                    dataPoint.update({
                        'red': original[y][x][0],
                        'green': original[y][x][1],
                        'blue': original[y][x][2],
                        'x': x,
                        'y': y,
                        'inRectangle': 0,
                        'class': 0
                    })
                    outsideRectangle.append(dataPoint)
            else:
                dataPoint.update({
                    'red': original[y][x][0],
                    'green': original[y][x][1],
                    'blue': original[y][x][2],
                    'x': x,
                    'y': y,
                    'inRectangle': 0,
                    'class': 0
                })
                outsideRectangle.append(dataPoint)

    return (trainingData, outsideRectangle)

def writeToCSV(dataDictList, csvFilePath):
    with open(csvFilePath, 'w', newline='') as csvfile:
        fieldnames = ['red', 'green', 'blue', 'x', 'y', 'jpeg', 'group', 'inRectangle', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for dataDict in dataDictList:
            writer.writerow({
                'red': dataDict['red'],
                'green': dataDict['green'],
                'blue': dataDict['blue'],
                'x': dataDict['x'],
                'y': dataDict['y'],
                'jpeg': dataDict['jpeg'],
                'group': dataDict['group'],
                'inRectangle': dataDict['inRectangle'],
                'class': dataDict['class']
            })

### Main
imagePath = "Robot Arm Pictures\\Originals"
maskPath = "Robot Arm Pictures\\Photoshop Masks"
rectangleCSVPath = "Data\\rectangles.csv"
trainingCSVPath = "Data\\Formatted Pixel Data\\trainingPixels.csv"
testingCSVPath = "Data\\Formatted Pixel Data\\testingPixels.csv"
random.seed(a='Lux Vision')

rectangleList = getRectangles(rectangleCSVPath)
fileIncrementor = 0
allTrainingData = []
allTestingData = []
previousGroup = 1

print('--------------------------------------------')
for rectangle in rectangleList:
    fileIncrementor += 1
    group = math.floor((fileIncrementor - 1) / 3) + 1

    if(previousGroup != group):
        print('Writing to group ' + str(previousGroup) + '\'s files.')
        groupTrainingCSVPath = trainingCSVPath.replace(
            '.csv', ('Group' + str(previousGroup) + '.csv'))
        groupTestingCSVPath = testingCSVPath.replace(
            '.csv', ('Group' + str(previousGroup) + '.csv'))
        writeToCSV(allTrainingData, groupTrainingCSVPath)
        writeToCSV(allTestingData, groupTestingCSVPath)
        allTrainingData = []
        allTestingData = []
        previousGroup = group
        print('Done writing!')
        print('--------------------------------------------')

    print('File: ' + str(fileIncrementor) + ' | Group: '+ str(group))
    print('Running defineAllPixels.')
    (trainingData, outsideRectangle) = defineAllPixels(imagePath, maskPath, rectangle, group)
    print('Running random shuffle twice.')
    random.shuffle(trainingData)
    random.shuffle(outsideRectangle)
    print('Appending all data')
    print('Length of training data is: ' + str(int(len(trainingData) / 10)))
    print('Length of outsideRectangle data is: ' + str(int(len(outsideRectangle) / 10)))
    allTestingData.extend(trainingData[0:int(len(trainingData) / 10)])
    allTestingData.extend(outsideRectangle[0:int(len(outsideRectangle) / 10)])
    allTrainingData.extend(trainingData[(int(len(trainingData) / 10) + 1):int(len(trainingData))])
    print('--------------------------------------------')
print('Done looping.')
print('Writing to group ' + str(previousGroup) + '\'s files.')
groupTrainingCSVPath = trainingCSVPath.replace(
    '.csv', ('Group' + str(previousGroup) + '.csv'))
groupTestingCSVPath = testingCSVPath.replace(
    '.csv', ('Group' + str(previousGroup) + '.csv'))
writeToCSV(allTrainingData, groupTrainingCSVPath)
writeToCSV(allTestingData, groupTestingCSVPath)
print('Done writing!')
print('--------------------------------------------')