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
trainingPixelsCSV = "Data\\Formatted Pixel Data\\trainingPixelsGroup1.csv"
modelOutputPath = "Data\\svmLinearModelGroup1.joblib"

print("Loading CSV into NumPy array.")
(pixelFeatureSet, pixelClassSet) = getPixelDataFromCSV(trainingPixelsCSV)
print("NumPy arrays loaded. Setting up SVM.")
# Kernel's are rbf, linear, poly, sigmoid and "precomputed" (I don't think I should do precomputed)
# Gamma's are auto, scale
clf = svm.SVC(kernel='linear', gamma='scale', verbose=True, cache_size=500)
print("SVM: Using SVC classifier, linear kernel, scale gamma, and 500MB cache.")
print("Beginning to fit data... (This will take a while.)")
clf.fit(pixelFeatureSet, pixelClassSet)
print("SVM fitted. Saving SVM model for repeated use.")
dump(clf, modelOutputPath)
print("SVM Model saved.")
