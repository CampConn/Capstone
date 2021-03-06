// FANN_Use.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "floatfann.h"
#include "fann_cpp.h"
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <fstream>

#define HSV 1 //0-BGR, 1-HSV

using namespace std;

int main(int argc, char **argv)
{
	if (argc != 5) {
		cout << "Error: enter 4 coordinates" << endl;
		exit(0);
	}
	cv::Mat original;
	if (HSV) {
		cv::Mat temp = cv::imread("image.jpeg", cv::IMREAD_COLOR);
		cv::cvtColor(temp, original, cv::COLOR_BGR2HSV);
	}
	else {
		original = cv::imread("image.jpeg", cv::IMREAD_COLOR);
	}


	FANN::neural_net net;
	fann_type *calc_out;
	fann_type* input;
	input = new fann_type[3];
	//printf("1\n");
	net.create_from_file("mask.net");
	//printf("2\n");
	
	int channels = original.channels();

	int nRows = original.rows;
	int nCols = original.cols;
	/*if (original.isContinuous())
	{
		nCols *= nRows;
		nRows = 1;
	}*/
	int i, j;
	uchar* p;
	for (i = 0; i < nRows; ++i)
	{
		p = original.ptr<uchar>(i);
		for (j = 0; j < nCols; ++j)
		{
			//printf("Looping: %d/%d\n", i * nCols + j, (int)channels*original.total());
			//add rgb values from original and int
			//pix << p[j] / 127.5 - 1 << endl;
			if (i < atoi(argv[2]) || i > atoi(argv[4]) || j < atoi(argv[1]) || j > atoi(argv[3])) {
				p[3 * j] = (uchar)0;
				p[3 * j + 1] = (uchar)0;
				p[3 * j + 2] = (uchar)0;
			}
			else {
				if (HSV) {
					input[0] = p[3 * j] / 90.0 - 1;
				}
				else {
					input[0] = p[3 * j] / 127.5 - 1;
				}
				input[1] = p[3 * j + 1] / 127.5 - 1;
				input[2] = p[3 * j + 2] / 127.5 - 1;

				calc_out = net.run(input);
				//printf("5\n");
				if (*calc_out < 0) {
					//printf("6\n");
					p[3 * j] = (uchar)0;
					p[3 * j + 1] = (uchar)0;
					p[3 * j + 2] = (uchar)0;
				}
				else {
					//printf("7\n");
					p[3 * j] = (uchar)255;
					p[3 * j + 1] = (uchar)255;
					p[3 * j + 2] = (uchar)255;
				}
			}

			

			//if (j % 3 == 2) {
			//pix << "1" << endl;
			//}

		}
	}



	//printf("8\n");
	imwrite("newmask.png", original);
	//printf("9\n");


	
    return 0;
}

