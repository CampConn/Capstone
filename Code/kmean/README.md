this is the kmean for 90% training and 10% testing field

How to run:

1. install python35 if you have no python on your device.

2. then install whl for packages that are going to use.

3. open the file and run the kmeans_10_test.py

it will take a while even though the model's been loaded

You will see avg accuracy around 75% without rectangles. And for each images with rectangles there are low accuracy. This is because the person, who set the rectangles, did include the arm base and it is not on the board. Then the environment out of the board was labeled with arm pixel which is different. You will recognize this if you look at the sample images created by kmeans. Anyway, the best prediction of our three models is over 90% if I remembered correctly.


***********you can also look at these .py files.

kmeans-hsv.py method is ok but has ambiguous boundary detection.

kmeans.py generated masks and those images were analyzed by Chase's test script.

other files are trials.

notice: Every code line commented by hand is aimed for matrix process, training, saving models. Therefore, it is important and it is commented out because no need to train images every single run. You will see load function right after commented code.
