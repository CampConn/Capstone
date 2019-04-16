Compile and Run in Microsft Visual Studio at https://visualstudio.microsoft.com/
Before compilation, do the following:
	* Go to Properties -> FANN_Gen Properties...
		* Go to C/C++ -> General -> Additional Include directories, and add the paths for the following:
			third_party\fann\include
			third_party\opencv\include
		* Go to Linker -> Input -> Additional Dependencies, and add the correct paths for the following:
			fann\bin\fannfloatd.lib
			opencv\lib\opencv_core343.lib
			opencv\lib\opencv_imgcodecs343.lib
			opencv\lib\opencv_imgproc343d.lib

Have in the diretory:
	If CSV mode:
		* trainingPixels.csv: data for training the network on, should be 90% of total data
		* testingPixels.csv: data for testing the network, should be 10% of the data
	If Image mode (mutually exclusive with CSV mode, do not use at this time):
		* image.jpeg: an image of the arm to get data from
		* image.png: a mask of the arm from image.jpeg
		* Multiple images may be included by adding sequential numbers (ie, image1.jpeg, image2.jpeg) (do not use at this time)
	If not generating new mask:
		* mask.net: the network file to start with before training

Macros (you can change the following settings in the code before compiling):
	* CSV_DATA: if set to 1, runs in CSV mode. If set to 0, runs in Image mode (do not change at this time)
	* NEW_NET: if set to 1, generates a new network to train from scratch. If set to 0, continues training a preexisting network
	* HSV: if set to 1, converts image data to HSV and uses that for training and testing network. If set to 0, uses RGB (do not use at this time, things may be out of order). 
	* NORMALIZE: if set to 1, image values are normalized from -1 to 1. If set to 0, values are used as-is. Recommended to keep at 1
	* ACC: desired error frequency


Output:
	* The resulting neural network will be outputted to mask.net
	* test.data and train.data are intermediary files that the network training can read. These can be ignored or examined for troubleshooting