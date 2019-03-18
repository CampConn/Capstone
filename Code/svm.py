import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff
from sklearn import svm

### Ooooh, I finally fucking get how this will work.
# Essentially, X is your training data.
# Y is your definitions.
# When you call predict, it takes in data like X and returns an expected Y.
# To Do:
# So now that I know what to do here's a nice list to get me the rest of the way:
# Read in X from one raw image.
# Read Y in from one photoshop mask.
# Pick the prediction method that is curved. There was a good example on the wiki.
# Make predictions for all images.
# Output files will create .pngs.
# Stretch goal, use all 21 images to build the neural network (this could be slow AF).

x = [[50, 80, 230], [120, 150, 52]]
y = [1, 0]
clf = svm.SVC(gamma='scale')
clf.fit(x, y)
print(clf.predict([[60, 120, 80]]))
# >>> [0]

