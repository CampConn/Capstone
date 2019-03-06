import os                           # Important for file matching
import csv                          # Handle CSV Stuff
import matplotlib.image as mpimg    # Image reading
import numpy as np                  # Mandatory array stuff


with open('rectangles.csv', 'w', newline='') as csvFile:
    rectangleWriter = csv.writer(csvFile, delimiter= ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

