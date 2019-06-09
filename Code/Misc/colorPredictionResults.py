import csv                          # CSV handling
import math                         # For floor()
from sklearn import svm             # Support Vector Machine
from joblib import dump, load       # SVM Model Persistence

def getCSV(CSVPath):
    with open(CSVPath, newline='') as csvFile:
        reader = list(csv.DictReader(csvFile))

        return reader

def writeToCSV(dataNestedDict, csvFilePath):
    with open(csvFilePath, 'w', newline='') as csvfile:
        fieldnames = ["rgb", "set1Arm", "set1NotArm", "set1Prediction",
            "set2Arm", "set2NotArm", "set2Prediction",
            "set3Arm", "set3NotArm", "set3Prediction",
            "set4Arm", "set4NotArm", "set4Prediction",
            "set5Arm", "set5NotArm", "set5Prediction",
            "set6Arm", "set6NotArm", "set6Prediction",
            "set7Arm", "set7NotArm", "set7Prediction",
            "totalArm", "totalNotArm", "totalPrediction"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for key in dataNestedDict.keys():
            writer.writerow({
                "rgb": key,
                "set1Arm": dataNestedDict[key]["1-1"], "set1NotArm": dataNestedDict[key]["1-0"], "set1Prediction": dataNestedDict[key]["1-p"],
                "set2Arm": dataNestedDict[key]["2-1"], "set2NotArm": dataNestedDict[key]["2-0"], "set2Prediction": dataNestedDict[key]["2-p"],
                "set3Arm": dataNestedDict[key]["3-1"], "set3NotArm": dataNestedDict[key]["3-0"], "set3Prediction": dataNestedDict[key]["3-p"],
                "set4Arm": dataNestedDict[key]["4-1"], "set4NotArm": dataNestedDict[key]["4-0"], "set4Prediction": dataNestedDict[key]["4-p"],
                "set5Arm": dataNestedDict[key]["5-1"], "set5NotArm": dataNestedDict[key]["5-0"], "set5Prediction": dataNestedDict[key]["5-p"],
                "set6Arm": dataNestedDict[key]["6-1"], "set6NotArm": dataNestedDict[key]["6-0"], "set6Prediction": dataNestedDict[key]["6-p"],
                "set7Arm": dataNestedDict[key]["7-1"], "set7NotArm": dataNestedDict[key]["7-0"], "set7Prediction": dataNestedDict[key]["7-p"],
                "totalArm": dataNestedDict[key]["t-1"], "totalNotArm": dataNestedDict[key]["t-0"], "totalPrediction": dataNestedDict[key]["t-p"]
            })

### Main
trainingPixelsCSV = "Data\\Formatted Pixel Data\\trainingPixelsGroup1.csv"
outputPixelCSV = "Data\\ColorPredictionResults" #4.csv"

previousGroup = "1"
pixelDictionary = dict()
totalsPixelList = dict([
    ("1p", 0), ("1t", 0),
    ("2p", 0), ("2t", 0),
    ("3p", 0), ("3t", 0),
    ("4p", 0), ("4t", 0),
    ("5p", 0), ("5t", 0),
    ("6p", 0), ("6t", 0),
    ("7p", 0), ("7t", 0),
    ("tp", 0), ("tt", 0)
])
clusterSize = 256
outputPixelCSV += str(clusterSize) + ".csv"

for group in range(1, 8):
    # print("Group: " + str(group) + " | Prev Group: "+ str(previousGroup))
    trainingPixelsCSV = trainingPixelsCSV.replace(previousGroup, str(group))
    previousGroup = str(group)
    pixelList = getCSV(trainingPixelsCSV)
    # print("Training Path: " + trainingPixelsCSV)

    for pixel in pixelList:
        key = str(int(math.floor(float(pixel['red']) / clusterSize))) + '-' + str(int(math.floor(float(pixel['green']) / clusterSize))) + '-' + str(int(math.floor(float(pixel['blue']) / clusterSize)))
        if(key in pixelDictionary):
            pixelDictionary[key][str(group) + "-" + pixel['class']] += 1
            pixelDictionary[key]["t-" + pixel['class']] += 1
        else:
            pixelDictionary[key] = dict([
                ("1-0", 0), ("1-1", 0), ("1-p", 0),
                ("2-0", 0), ("2-1", 0), ("2-p", 0),
                ("3-0", 0), ("3-1", 0), ("3-p", 0),
                ("4-0", 0), ("4-1", 0), ("4-p", 0),
                ("5-0", 0), ("5-1", 0), ("5-p", 0),
                ("6-0", 0), ("6-1", 0), ("6-p", 0),
                ("7-0", 0), ("7-1", 0), ("7-p", 0),
                ("t-0", 0), ("t-1", 0), ("t-p", 0)
            ])
            pixelDictionary[key][str(group) + "-" + pixel['class']] += 1
            pixelDictionary[key]["t-" + pixel['class']] += 1

for key in pixelDictionary.keys():
    for i in range(1, 9):
        if(i == 8):
            i = "t"
        totalsPixelList[str(i) + "t"] += pixelDictionary[key][str(i) + "-0"]
        totalsPixelList[str(i) + "t"] += pixelDictionary[key][str(i) + "-1"]
        if(pixelDictionary[key][str(i) + "-0"] <= pixelDictionary[key][str(i) + "-1"]):
            pixelDictionary[key][str(i) + "-p"] = 1
            totalsPixelList[str(i) + "p"] += pixelDictionary[key][str(i) + "-1"]
        elif(pixelDictionary[key][str(i) + "-0"] > pixelDictionary[key][str(i) + "-1"]):
            pixelDictionary[key][str(i) + "-p"] = 0
            totalsPixelList[str(i) + "p"] += pixelDictionary[key][str(i) + "-0"]

writeToCSV(pixelDictionary, outputPixelCSV)
# for key in pixelDictionary.keys():
#     print(key + " -> " + str(pixelDictionary[key]))

for i in range(1, 9):
    if(i == 8):
        i = "t"
    print(str(i) + ": " + str(totalsPixelList[str(i) + "p"])
        + " | " + str(totalsPixelList[str(i) + "t"]) + " = "
        + str(round((totalsPixelList[str(i) + "p"] * 100 / totalsPixelList[str(i) + "t"]), 2)))
