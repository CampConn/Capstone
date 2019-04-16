Compile and Run in Microsft Visual Studio at https://visualstudio.microsoft.com/
Before compilation, do the following:
	* Go to Properties -> FANN_Use Properties...
		* Go to C/C++ -> General -> Additional Include directories, and add the paths for the following:
			third_party\fann\include
			third_party\opencv\include
		* Go to Linker -> Input -> Additional Dependencies, and add the correct paths for the following:
			fann\bin\fannfloatd.lib
			opencv\lib\opencv_core343.lib
			opencv\lib\opencv_imgcodecs343.lib
			opencv\lib\opencv_imgcodecs343d.lib
			opencv\lib\opencv_imgproc343d.lib

Have in the diretory:
	* image.jpeg: an image of the arm to be analyzed
	* mask.net: a network file from FANN_Gen

Command Line Arguments:
	* Define the boundaries of the rectangle: left boundary, top boundary, right boundary, bottom boundary. Same order as rectangles.csv in Capstone/Data
	* To change, go to Properties -> FANN_Use Properties -> Debugging -> Command Arguments

Macros (you can change the following settings in the code before compiling):
	* HSV: if set to 1, reads the image in HSV and feeds input to the network based on that. If set to 0, reads in GBR. This should be set the same way as FANN_Gen when the network was generated

Output:
	* The result mask will be outputted to newmask.jpeg