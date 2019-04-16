Have in the diretory:
	* image.jpeg: an image of the arm to be analyzed
	* mask.net: a network file from FANN_Gen

Command Line Arguments:
	* Define the boundaries of the rectangle: top boundary, bottom boundary, left boundary, right boundary

Macros (you can change the following settings in the code before compiling):
	* HSV: if set to 1, reads the image in HSV and feeds input to the network based on that. If set to 0, reads in GBR. This should be set the same way as FANN_Gen when the network was generated

Output:
	* The result mask will be outputted to newmask.jpeg