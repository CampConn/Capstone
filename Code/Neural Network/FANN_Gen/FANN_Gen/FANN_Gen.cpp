// FANN_Gen.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "floatfann.h"
#include "fann_cpp.h"
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <ios>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cmath>

#define CSV_DATA 1 //0-generate data from images, 1-generate data from csv data file
#define NEW_NET 1 //0-update current mask.net, 1-make new mask.net
#define HSV 1 //0-BGR, 1-HSV
#define NORMALIZE 1 //0-inputs values as is, 1-normalizes from -1 to 1
#define ACC 2*0.09 //desired error. Depicted as as output nodes multiplied by desired frequency of false outputs

using std::cout;
using std::cerr;
using std::endl;
using std::setw;
using std::left;
using std::right;
using std::showpos;
using std::noshowpos;

void gen_data();
int print_callback(FANN::neural_net, FANN::training_data, unsigned int, unsigned int, float, unsigned int, void*, int*);
void net_train();
void rgb_hsv(float*);

int min;

int main()
{
	
	min = INT_MAX;
	//int arg = atoi(argv[1]);
	//generate data
	gen_data();
	//train network
	//test on train data
	try
	{
		std::ios::sync_with_stdio(); // Syncronize cout and printf output
		net_train();
	}
	catch (...)
	{
		cerr << endl << "Abnormal exception." << endl;
	}
    return 0;
}

void rgb_hsv(float* colors) {
	colors[0] /= 255.0;
	colors[1] /= 255.0;
	colors[2] /= 255.0;
	float c_max, c_min, delta, hue, sat, val;
	c_max = colors[0];
	if (colors[1] > c_max)
		c_max = colors[1];
	if (colors[2] > c_max)
		c_max = colors[2];
	c_min = colors[0];
	if (colors[1] < c_min)
		c_min = colors[1];
	if (colors[2] < c_min)
		c_min = colors[2];
	delta = c_max - c_min;
	if (delta == 0) {
		hue = 0;
	}
	else if (c_max == colors[0]) {
		hue = (colors[1] - colors[2]) / delta;
		while (hue >= 6.0) {
			hue -= 6.0;
		}
		hue *= 60.0;
	}
	else if (c_max == colors[1]) {
		hue = 60.0*((colors[2] - colors[0]) / delta + 2);
	}
	else {
		hue = 60.0*((colors[0] - colors[1]) / delta + 4);
	}
	if (c_max == 0) {
		sat = 0;
	}
	else {
		sat = delta / c_max;
	}
	val = c_max;
	colors[0] = hue / 180 - 1;
	colors[1] = sat * 2 - 1;
	colors[2] = val * 2 - 1;
}


void gen_data() {
	//take in image and mask
	printf("Preparing data...\n");
	int test_num = 0;
	int train_num = 0;
	float colors[3];
	std::string temp[9];


	if (CSV_DATA) {
		//printf("1\n");
		std::ofstream test("test.data", std::ios_base::binary | std::ios_base::out);
		std::ofstream train("train.data", std::ios_base::binary | std::ios_base::out);

		std::ifstream csv_test("testingPixels.csv", std::ios_base::binary | std::ios_base::in);
		std::ifstream csv_train("trainingPixels.csv", std::ios_base::binary | std::ios_base::in);
		

		test << "                    " << endl;//we'll need to add to the start of the file later
		train << "                    " << endl;//this ensures nothing is overwritten
		//printf("2\n");
		getline(csv_test, temp[0]);//get rid of first line
		while (getline(csv_test, temp[0], ',')) {
			//printf("3\n");
			for (int i = 1; i < 8; i++) {
				getline(csv_test, temp[i], ',');
			}
			getline(csv_test, temp[8]);
			//printf("4\n");
			//for (int i = 0; i < 9; i++) {
			//	cout << "temp[" << i << "]: " << temp[i] << endl;
			//}
			if (stoi(temp[7]) == 1) {
				test_num++;
				for (int i = 0; i < 3; i++) {
					colors[i] = stof(temp[i]);
				}

				if (HSV) {
					rgb_hsv(colors);
					//printf("6\n");
				}
				else {
					for (int i = 0; i < 3; i++) {
						colors[i] = colors[i] / 127.5 - 1;
					}
				}
				test << colors[0] << " " << colors[1] << " " << colors[2] << endl;
			}
			
			if (stoi(temp[8]) == 0) {
				test << "-1 1" << endl;
			}
			else {
				test << "1 -1" << endl;
			}
			//printf("7\n");
			//printf("???\n");
		}
		test.seekp(0, std::ios::beg);
		test << test_num << " 3 2" << endl;
		//printf("8\n");
		getline(csv_train, temp[0]);//get rid of first line
		while (getline(csv_train, temp[0], ',')) {
			for (int i = 1; i < 8; i++) {
				getline(csv_train, temp[i], ',');
			}
			getline(csv_train, temp[8]);
			
			if (stoi(temp[7]) == 1) {
				train_num++;
				for (int i = 0; i < 3; i++) {
					colors[i] = stof(temp[i]);
				}

				if (HSV) {
					rgb_hsv(colors);
				}
				else {
					for (int i = 0; i < 3; i++) {
						colors[i] = colors[i] / 127.5 - 1;
					}
				}
				train << colors[0] << " " << colors[1] << " " << colors[2] << endl;
			}

			
			if (stoi(temp[8]) == 0) {
				train << "-1 1" << endl;
			}
			else {
				train << "1 -1" << endl;
			}
			
		}
		train.seekp(0, std::ios::beg);
		train << train_num << " 3 2" << endl;

		test.close();
		train.close();

		csv_test.close();
		csv_train.close();

	}
	else {//For direct image training. Not fully ready at the moment
		cv::Mat original, mask;
		if (HSV) {
			cv::Mat temp = cv::imread("1548556547879731673.jpeg", cv::IMREAD_COLOR);
			cv::cvtColor(temp, original, cv::COLOR_BGR2HSV);
		}
		else {
			original = cv::imread("1548556547879731673.jpeg", cv::IMREAD_COLOR);
		}

		mask = cv::imread("1548556547879731673.png", cv::IMREAD_GRAYSCALE);
		//create file pic.data
		std::ofstream out("test.data", std::ios_base::binary | std::ios_base::out);
		//ofstream pix("pixels.txt");
		//header: train examples, input, output
		
		out << (545 - 0 + 1)*(339 - 84 + 1) << " 3 2\n";

		//iterate through pixels
		//int channels = original.channels();
		//int nRows = original.rows;
		//int nCols = original.cols * channels;
		/*if (original.isContinuous())
		{
		printf("Original is continuous\n");
		nCols *= nRows;
		nRows = 1;
		}*/
		int i, j, k;
		uchar* p;
		uchar* q;
		k = 0;
		for (i = 84; i <= 339; ++i)
		{
			p = original.ptr<uchar>(i);
			q = mask.ptr<uchar>(i);
			for (j = 0; j <= 545; ++j)
			{
				if (!(k % 1000)) {
					//printf("Preparing data: %d/%d\n", k, (545 - 0 + 1)*(339 - 84 + 1));
				}
				k++;
				//add values from original and int
				if (NORMALIZE) {
					if (HSV) {
						out << (int)p[j * 3] / 90.0 - 1;
					}
					else {
						out << (int)p[j * 3] / 127.5 - 1;
					}
					out << " " << (int)p[j * 3 + 1] / 127.5 - 1 << " " << (int)p[j * 3 + 2] / 127.5 - 1 << "\n";

					//add desired output based on mask
					if (q[j] < 128) {
						out << "-1 1\n";
					}
					else {
						out << "1 -1\n";
					}
				}
				else {
					out << (int)p[j * 3] << " " << (int)p[j * 3 + 1] << " " << (int)p[j * 3 + 2] << "\n";

					//add desired output based on mask
					if (q[j] < 128) {
						out << "-1 1\n";
					}
					else {
						out << "1 -1\n";
					}
				}




			}
		}
		out.close();
	}
	


	
	//pix.close();
}

int print_callback(FANN::neural_net &net, FANN::training_data &train,
	unsigned int max_epochs, unsigned int epochs_between_reports,
	float desired_error, unsigned int epochs, void *user_data)
{
	cout << "Epochs     " << setw(8) << epochs << ". "
		<< "Current Fail: " << left << net.get_bit_fail() << right << endl;
	if (net.get_bit_fail() < min) {
		min = net.get_bit_fail();
	}
	return 0;
}

// Test function that demonstrates usage of the fann C++ wrapper
void net_train()
{
	cout << endl << "Mask Network generation started." << endl;
	FANN::training_data data;
	if (data.read_train_from_file("train.data"))
	{
		const float desired_error = 0.06f;
		int desired_fail = ACC*data.length_train_data();
		const unsigned int max_iterations = 10000;
		const unsigned int iterations_between_reports = 100;

		cout << endl << "Creating network." << endl;
		FANN::neural_net net;
		if (NEW_NET) {
			const float learning_rate = 0.7f;
			const unsigned int num_layers = 5;
			const unsigned int num_input = 3;
			const unsigned int num_hidden = 4;
			const unsigned int num_output = 2;
		
			net.create_standard(num_layers, num_input, num_hidden, num_hidden, num_hidden, num_output);

			net.set_learning_rate(learning_rate);

			net.set_activation_steepness_hidden(1.0);
			net.set_activation_steepness_output(1.0);

			net.set_activation_function_hidden(FANN::SIGMOID_SYMMETRIC_STEPWISE);
			net.set_activation_function_output(FANN::SIGMOID_SYMMETRIC_STEPWISE);

			net.set_train_stop_function(FANN::STOPFUNC_BIT);
			if (NORMALIZE) {
				net.set_bit_fail_limit(0.5);
			}
			else {
				net.set_bit_fail_limit(0.5);
			}
		
		}
		else {
			net.create_from_file("mask.net");
		}

	

		// Set additional properties such as the training algorithm
		//net.set_training_algorithm(FANN::TRAIN_QUICKPROP);

		// Output network type and parameters
		cout << endl << "Network Type                         :  ";
		switch (net.get_network_type())
		{
		case FANN::LAYER:
			cout << "LAYER" << endl;
			break;
		case FANN::SHORTCUT:
			cout << "SHORTCUT" << endl;
			break;
		default:
			cout << "UNKNOWN" << endl;
			break;
		}
		net.print_parameters();

		cout << endl << "Training network." << endl;

		
	
		// Initialize and train the network with the data
		if (NEW_NET) {
			net.init_weights(data);
		}
		cout << "Max Epochs " << setw(8) << max_iterations << ". "
			<< "Desired Fail: " << left << desired_fail << right << endl;
		net.set_callback(print_callback, NULL);
		net.train_on_data(data, max_iterations,
			iterations_between_reports, desired_fail);

		cout << endl << "Minimum fail was" << min << endl;
		if (data.read_train_from_file("test.data")) {
			cout << endl << "Testing network." << endl;
			int wrong = 0;
			for (unsigned int i = 0; i < data.length_train_data(); ++i)
			{
				// Run the network on the test data
				fann_type *calc_out = net.run(data.get_input()[i]);

				if (((calc_out[0] < calc_out[1]) && (data.get_output()[i][0] > data.get_output()[i][1])) || ((calc_out[0] > calc_out[1]) && (data.get_output()[i][0] < data.get_output()[i][1]))) {
					wrong++;
					//cout << "Error " << wrong << ": (" << showpos << data.get_input()[i][0] << ", "
					//	<< data.get_input()[i][1] << ", "
					//	<< data.get_input()[i][2] << ") -> " << *calc_out
					//	<< ", should be " << data.get_output()[i][0] << endl;
				}


			}
			cout << "Total Error: " << wrong << " out of " << data.length_train_data() << endl;
		}
		

		cout << endl << "Saving network." << endl;

		// Save the network in floating point and fixed point
		net.save("mask.net");
		//unsigned int decimal_point = net.save_to_fixed("xor_fixed.net");
		//data.save_train_to_fixed("xor_fixed.data", decimal_point);

		cout << endl << "Mask Network completed." << endl;
	}
}