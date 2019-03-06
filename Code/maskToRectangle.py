import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff

truthPath = "Robot Arm Pictures\\Photoshop Masks"

with open('rectangles.csv', 'w', newline='') as csvFile:
    rectangleWriter = csv.writer(csvFile, delimiter= ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for truthFile in os.listdir(truthPath):
        truthImage = mpimg.imread(truthPath + "\\" + truthFile)
        currentX = 0
        currentY = 0
        x1 = 640
        y1 = 480
        x2 = 0
        y2 = 0
        truthErrors = 0

        for row in truthImage:
            for truthPixel in row:
                if(np.array_equal(truthPixel, [1.0, 1.0, 1.0, 1.0])):
                elif(np.array_equal(truthPixel, [0.0, 0.0, 0.0, 1.0]) != True):
                    truthErrors += 1
                currentY += 1
            currentY = 0
            currentX += 1
