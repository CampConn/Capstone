import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff

# This script must be given two directories.
# When given two directories it can compare all images of the same name.
# Read image 1 from directory A, image 2 from directory B
# Image 1 is "truth"
# Image 2 is "kmeans"
# Compare truth and kmeans pixel by pixel
# True positive is when they agree on white.
# True negative is when they agree on black.
# False positive is when kmeans says white when truth says black.
# False negative is when kmeans says black when truth says white.
# Prints these four counters (and two error counters when necessary)

truthPath = "Robot Arm Pictures\\Photoshop Masks"
kmeansPath = "Robot Arm Pictures\\K-means RGB Strawman"
# kmeansPath = "Robot Arm Pictures\\K-means HSV Strawman"

# To do: Make the CSV file be more map like to attribute meaning behind indicies.

with open('Data\\rectangles.csv', newline='') as csvFile:
    rectangleReader = csv.reader(csvFile, delimiter=',', quotechar='|')
    fileIncrementor = 1

    for rectangleRow in rectangleReader:
        print("Trying file " + str(fileIncrementor) + ": " + rectangleRow[0])
        print("-----------------------------------------------")
        truthImage = mpimg.imread(truthPath + "\\" + rectangleRow[0])
        kmeansImage = mpimg.imread(kmeansPath + "\\" + rectangleRow[0])

        # print("Truth Image: " + str(len(truthImage)))
        # print("K-means Image: " + str(len(kmeansImage)))
        # print("K-means Image: " + str(len(kmeansImage[0])))
        # print("K-means Image: " + str(kmeansImage[0][0]))

        truePositive = 0
        trueNegative = 0
        falsePositive = 0
        falseNegative = 0
        truthErrors = 0
        kmeansErrors = 0
        rectanglePixels = 0

        for y in range(int(rectangleRow[2]), (int(rectangleRow[4]) + 1)): # Row
            for x in range(int(rectangleRow[1]), (int(rectangleRow[3]) + 1)):  # Column
                rectanglePixels += 1
                if(np.array_equal(truthImage[y][x], [1.0, 1.0, 1.0, 1.0])):
                    if(np.array_equal(truthImage[y][x], kmeansImage[y][x])):
                        truePositive += 1
                    elif(np.array_equal(kmeansImage[y][x], [0.0, 0.0, 0.0, 1.0])):
                        falseNegative +=1
                    else:
                        kmeansErrors += 1
                elif(np.array_equal(truthImage[y][x], [0.0, 0.0, 0.0, 1.0])):
                    if(np.array_equal(truthImage[y][x], kmeansImage[y][x])):
                        trueNegative += 1
                    elif(np.array_equal(kmeansImage[y][x], [1.0, 1.0, 1.0, 1.0])):
                        falsePositive +=1
                    else:
                        kmeansErrors += 1
                else:
                    truthErrors += 1
                    # print("Truth Error Coords | Row: " + str(x) + " | " + "Column: " + str(y))
                x += 1
            x = 0
            y += 1

        print("Rectangle pixels: " + str(rectanglePixels))
        print("True positives: " + str(truePositive) + " at " + str(truePositive * 100 / rectanglePixels))
        print("True negatives: " + str(trueNegative) + " at " + str(trueNegative * 100 / rectanglePixels))
        print("False positives: " + str(falsePositive) + " at " + str(falsePositive * 100 / rectanglePixels))
        print("False negatives: " + str(falseNegative) + " at " + str(falseNegative * 100 / rectanglePixels))
        if(truthErrors > 0):
            print("Truth errors: " + str(truthErrors))
            # print("Truth errors occur when a pixel in the truth image is not black or white.")
        if(kmeansErrors > 0):
            print("K-means errors: " + str(kmeansErrors))
            # print("K-means errors occur when a pixel in the k-means image is not black or white.")
        print("")
        fileIncrementor += 1
