import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff

truthPath = "Robot Arm Pictures\\Photoshop Masks"

with open('Data\\rectangles.csv', 'w', newline='') as csvFile:
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

        print("Processing " + truthFile + "...")

        for row in truthImage:
            for truthPixel in row:
                if(np.array_equal(truthPixel, [1.0, 1.0, 1.0, 1.0])):
                    if(currentX > x2):
                        x2 = currentX
                    elif(currentX < x1):
                        x1 = currentX
                    if(currentY > y2):
                        y2 = currentY
                    elif(currentY < y1):
                        y1 = currentY
                elif(np.array_equal(truthPixel, [0.0, 0.0, 0.0, 1.0]) != True):
                    truthErrors += 1
                currentX += 1
            currentX = 0
            currentY += 1

        if(truthErrors > 0):
            # Truth errors occur when a pixel in the truth image is not black or white
            print("Truth errors: " + str(truthErrors))
        print('')

        rectangleWriter.writerow([truthFile, x1, y1, x2, y2])
