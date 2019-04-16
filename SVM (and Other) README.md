# SVM (and Others) Overviews

There's a few SVM and other scripts which require Python to run.
My build version was 3.5.0 but you should be able to use newer Python 3 versions.
Here's a [link](https://www.python.org/downloads/release/python-350/) to my build version.
You should also ensure

## My Scripts

* analysis.py
* createDataSet.py
* maskToRectangle.py
* outdatedSvmCreate.py (No longer required for deliverables)
* svmCreate.py
* svmPredict.py
* svmTest.py

## Python Libraries I use

### Built in

* csv
* sys
* random
* math
* os

### Third Party

* matplotlib
* numpy
* sklearn
* joblib

### Installing Third Party Libraries with Pip

1. python -m pip install -U pip
2. python -m pip install -U matplotlib
3. python -m pip install -U numpy
4. python -m pip install -U scikit-learn
5. python -m pip install -U joblib

## SVM Script Explanation (How to run)

It's worth noting before running some scripts, configuration is required.
All run commands are expected to be run from the top level directory (Capstone).

### svmCreate

``` bash
python Code\\SVM\\svmCreate.py
```

This creates 7 models from the 7 trainingCSVs located in 'Data\\Formatted Pixel Data'.

### svmTest

``` bash
python Code\\SVM\\svmTest.py
```

Tests 7 models on the the 7 testingCSVs located in 'Data\\Formmatted Pixel Data'.
All output is printed to the commandline.
You can specify an output file (to bash) by adding '> fileName.txt' at the end of the call.

### svmPredict

``` bash
python Code\\SVM\\svmPredict.py
```

Will use the 7 models to create 21 predicted masks.
They will always be saved to the 'Support Vector Machine Images' directory.

### Note about outdatedSvmCreate.py

outdatedSvmCreate used pictures to set up a training model.
This is no longer the ideal approach, but I was unwilling to delete it since it'd be sad to delete work by the file.

## Misc Scripts Explanation (How to run)

It's worth noting before running some scripts, configuration is required.
All run commands are expected to be run from the top level directory (Capstone).

### analysis

Configuration required to run analysis.
In order to perform an analysis on your 21 images, you need to edit analysis.py.
Search for '### Main'.
Set 'implementationMaskPath' to your folder (containing your 21 predicted masks).
(Note, if you're implementationMaskPath is already available, uncomment it and comment out the active one.)

``` bash
python Code\\Misc\\analysis.py
```

Output will be 21 different picture (in the rectangle).
You can dump this into a txt (using Bash) by adding '> fileName.txt' to the bash command.

### maskToRectangle

``` bash
python Code\\Misc\\maskToRectangle.py
```

Will analyze the photoshop masks and create a csv containing two (x,y) coordinates and associated file.
The (x,y) coordinates will create a rectangle (inclusive).
This script creates a simulation of the rough masks that we're expecting as input.

### createDataSet

``` bash
python Code\\Misc\\createDataSet.py
```

Will create 7 CSVs for training and testing (each).
This is a standard set to be used for the 7 group implementation models.
Essentially, every three images will be collected into one list of dictionaries.
The list will then be shuffled randomly and then split 9:1.
90% of pixels from the three images will be used for training.
10% of pixels from the three images will be used for testing.
The random shuffling is currently seeded and will always produce the same output.