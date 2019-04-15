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
            if(counter % 5000 == 0):
                print('Progress: ' + str(counter))

            pixelFeatures = np.array([int(pixel['red']), int(pixel['green']), int(pixel['blue'])])
            pixelClass = np.array(int(pixel['class']))
            pixelFeatureSet = np.concatenate((pixelFeatureSet, pixelFeatures), axis=0)
            pixelClassSet = np.concatenate((pixelClassSet, pixelClass), axis=None)

    pixelFeatureSet = pixelFeatureSet.reshape(int(len(pixelFeatureSet) / 3), 3)

    return (pixelFeatureSet, pixelClassSet)

### Main
trainingImagePath = "Robot Arm Pictures\\Originals"
trainingMaskPath = "Robot Arm Pictures\\Photoshop Masks"
rectangleCSVPath = "Data\\rectangles.csv"
modelOutputPath = "Data\\svmLinearModel.joblib"

print("Using CSV to get best rectangle.")
rectangle = smallestRectangle(rectangleCSVPath)
pngFile = rectangle[0]
jpegFile = pngFile.replace("png", "jpeg")
x1 = int(rectangle[1])
y1 = int(rectangle[2])
x2 = int(rectangle[3])
y2 = int(rectangle[4])
print("Setting up images, x, and y with rectangle.")
inputImage = mpimg.imread(trainingImagePath + "\\" + jpegFile)
inputMask = mpimg.imread(trainingMaskPath + "\\" + pngFile)
print("Images completed.")
x = jpegToList(inputImage, x1, y1, x2, y2)
print("X completed.")
y = maskPngToBooleanList(inputMask, x1, y1, x2, y2)
print("Y completed.")
# Helpful data debug statements
# print("X: " + str(x))
# print("Y: " + str(y))
# print("X len: " + str(len(x)))
# print("Y len: " + str(len(y)))
print("Setting up SVM.")
# Kernel's are rbf, linear, poly, sigmoid and "precomputed" (I don't think I should do precomputed)
# Gamma's are auto, scale
clf = svm.SVC(kernel='linear', gamma='scale', verbose=True, cache_size=500)
print("SVM gamma set to 'scale'.")
print("Beginning to fit data... (This will take a while.)")
clf.fit(x, y)
print("SVM fitted. Saving SVM model for repeated use.")
dump(clf, modelOutputPath)
print("SVM Model saved.")
