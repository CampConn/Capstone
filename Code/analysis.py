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

fileIncrementor = 1

for truthFile in os.listdir(truthPath):
    print("Trying file " + str(fileIncrementor) + ": " + truthFile)
    print("-----------------------------------------------")
    truthImage = mpimg.imread(truthPath + "\\" + truthFile)
    kmeansImage = mpimg.imread(kmeansPath + "\\" + truthFile)

    truePositive = 0
    trueNegative = 0
    falsePositive = 0
    falseNegative = 0
    truthErrors = 0
    kmeansErrors = 0
    totalPixels = 0
    x = 0
    y = 0
    
    for row in truthImage:
        for truthPixel in row:
            totalPixels += 1
            if(np.array_equal(truthPixel, [1.0, 1.0, 1.0, 1.0])):
                if(np.array_equal(truthPixel, kmeansImage[y][x])):
                    truePositive += 1
                elif(np.array_equal(kmeansImage[y][x], [0.0, 0.0, 0.0, 1.0])):
                    falseNegative +=1
                else:
                    kmeansErrors += 1
            elif(np.array_equal(truthPixel, [0.0, 0.0, 0.0, 1.0])):
                if(np.array_equal(truthPixel, kmeansImage[y][x])):
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

    print("Total pixels: " + str(totalPixels))
    print("True positives: " + str(truePositive) + " at " + str(truePositive * 100 / totalPixels))
    print("True negatives: " + str(trueNegative) + " at " + str(trueNegative * 100 / totalPixels))
    print("False positives: " + str(falsePositive) + " at " + str(falsePositive * 100 / totalPixels))
    print("False negatives: " + str(falseNegative) + " at " + str(falseNegative * 100 / totalPixels))
    if(truthErrors > 0):
        print("Truth errors: " + str(truthErrors))
        # print("Truth errors occur when a pixel in the truth image is not black or white.")
    if(kmeansErrors > 0):
        print("K-means errors: " + str(kmeansErrors))
        # print("K-means errors occur when a pixel in the k-means image is not black or white.")
    print("")
    fileIncrementor += 1