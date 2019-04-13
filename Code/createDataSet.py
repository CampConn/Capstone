import csv      # 
import sys      # To do: Use sys to implement argv.
import matplotlib.image as mpimg

def getRectangles(rectangleCSVPath):
    with open(rectangleCSVPath, newline='') as csvFile:
        rectangleReader = list(csv.reader(csvFile, delimiter=',', quotechar='|'))

        return rectangleReader

def defineTrainingAndTestingPixels(truthPath, rectangle):
    trainingData = np.array([], dtype=np.uint8).reshape(0, 3)
    innerTestingData = np.array([], dtype=np.uint8).reshape(0, 3)
    outsideTheRectangle = np.array([], dtype=np.uint8).reshape(0, 3)
    outerTestingData = np.array([], dtype=np.uint8).reshape(0, 3)

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
