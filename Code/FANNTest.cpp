// FANNTest.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "src/include/fann.h"
#include <stdio.h>
#include "src/include/floatfann.h"
//#include <opencv2/opencv.hpp>
//#include <opencv2/core/hal/interface.h>
#include <iostream>
#include <fstream>
#include <string>


void gen_data();
void gen_network();
void run_network();
void get_pix();
void gen_mask();

using namespace std;

int main()
{
//gen data from images
	//gen_data();
//train NN with data
	//gen_network();
//run network on separate image
	//get_pix();
	run_network();
	//gen_mask();
	return 0;
}

/*
void get_pix() {
	cv::Mat original;
	original = cv::imread("1548556547879731673.jpeg", cv::IMREAD_COLOR);
	ofstream pix("pixels.txt");
	int channels = original.channels();

	int nRows = original.rows;
	int nCols = original.cols * channels;
	if (original.isContinuous())
	{
		nCols *= nRows;
		nRows = 1;
	}
	int i, j;
	uchar* p;
	for (i = 0; i < nRows; ++i)
	{
		p = original.ptr<uchar>(i);
		for (j = 0; j < nCols; ++j)
		{
			printf("Looping: %d/%d\n", i * nCols + j, (int)channels*original.total());
			//add rgb values from original and int
			pix << p[j] / 127.5 - 1 << endl;
			//if (j % 3 == 2) {
				//pix << "1" << endl;
			//}

		}
	}
}

void gen_data() {
	//take in image and mask
	cv::Mat original, mask;
	original = cv::imread("1548556547879731673.jpeg", cv::IMREAD_COLOR);
	mask = cv::imread("1548556547879731673.png", cv::IMREAD_GRAYSCALE);
	//create file pic.data
	ofstream out("pic.data");
	//ofstream pix("pixels.txt");
	//header: train examples, input, output
	printf("Made pic.data\n");
	out << "139776 3 2" << endl << endl;
	printf("Added header to pic.data\n");
	//iterate through pixels
	int channels = original.channels();
	int nRows = original.rows;
	int nCols = original.cols * channels;
	if (original.isContinuous())
	{
		nCols *= nRows;
		nRows = 1;
	}
	int i, j;
	uchar* p;
	uchar* q;
	for (i = 84; i <= 339; ++i)
	{
		p = original.ptr<uchar>(i);
		q = mask.ptr<uchar>(i);
		for (j = 0; j <= 545; ++j)
		{
			printf("Looping: %d/%d\n", (i-100)* 381+(j-79), 139776);
			//add rgb values from original and int
			out << (int)p[j * 3] / 127.5 - 1 << " " << (int)p[j * 3 + 1] / 127.5 - 1 << " " << (int)p[j * 3 + 2] / 127.5 - 1 << endl << endl;
			//pix << p[j * 3] << endl << p[j * 3 + 1] << endl << p[j * 3 + 2] << endl << "1" << endl;
			//add desired output based on mask
			if (q[j] < 128) {
				out << "-1 1" << endl << endl;
			}
			else {
				out << "1 -1" << endl << endl;
			}
			//++itm;
			//i++;
			//p[j] = table[p[j]];
		}
	}

	
	out.close();
	//pix.close();
}

void gen_mask() {
	//take in image and mask
	cv::Mat original;
	original = cv::imread("1548556547879731673.jpeg", cv::IMREAD_COLOR);
	//create file pic.data
	ifstream in("temp.txt");
	string line;
	//header: train examples, input, output



	//iterate through pixels
	cv::MatIterator_<cv::Vec3b> it, end;

	it = original.begin<cv::Vec3b>();

	end = original.end<cv::Vec3b>();

	for (int i = 1; it != end; ++it) {
		printf("Looping: %d/%d\n", i, original.total());
		getline(in, line);
		if (line == "1") {
			(*it)[0] = (uchar)255;
			(*it)[1] = (uchar)255;
			(*it)[2] = (uchar)255;
		}
		else {
			(*it)[0] = (uchar)0;
			(*it)[1] = (uchar)0;
			(*it)[2] = (uchar)0;
		}

		i++;
	}
	imwrite("newmask.jpeg", original);
	in.close();
}
*/

//


void gen_network() {
	struct fann *ann = fann_create_standard(5, 3, 4, 4, 4, 2);
	fann_set_rprop_delta_max(ann, 50);//default 50
	fann_set_rprop_increase_factor(ann, 1.2);//default 1.2
	fann_set_rprop_decrease_factor(ann, 0.5);//default 0.5
	//fann_randomize_weights(ann, -0.1, 0.1);
	fann_set_bit_fail_limit(ann, 0.35); //default 0.35

	fann_train_on_file(ann, "pic.data", 200, 10, (float) 0.01);
	fann_save(ann, "mask.net");
	fann_destroy(ann);
}

void run_network() {

	fann_type *calc_out;
	fann_type input[4];

	struct fann *ann = fann_create_from_file("mask.net");

	ifstream in("pixels.txt");
	ofstream out("temp.txt");
	int temp;
	string line;
	for (int i = 0; i < 3 * 307200; i++) {
		getline(in, line);
		input[i % 3] = atof(line.c_str());
		if (i % 3 == 2) {
			printf("%d/%d\t", i / 3, 307200);
			calc_out = fann_run(ann, input);
			printf("(%f,%f,%f)\t(%f, %f)\n", (float)input[0], (float)input[1], (float)input[2], (float)calc_out[0], (float)calc_out[1]);
			if ((float)calc_out[0] < (float)calc_out[1]) {
				out << "0" << endl;
			}
			else {
				out << "1" << endl;
			}
		}


	}
	fann_destroy(ann);
}



