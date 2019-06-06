# CS461-3

## Senior Capstone Group 15: Lux Vision

Our Capstone project is about solving a computer vision problem.
We're trying to get a robot arm to see itself with 90% accuracy.

## April 15th Code Freeze

All readme's are at the top level for easy access!
You can read the SVM and Other page [here](https://github.com/CampConn/Capstone/wiki/Code-Freeze-README---SVM-and-Others).

## Semantic Segmentation CNN model
model is in the link: https://drive.google.com/open?id=1WAAC2q4yd6iZeXbE57m-unSpTTf-YlQy 
github only allows files less than 100Mb. there are lots of files are over 200Mb and some of them are over 1Gb.
'installation files' folder contains exe file you might need.
'Semantic-Segmentation-CNN' contains the model

I past README.txt from 'Semantic-Segmentation-CNN'
Retrieved From https://github.com/GeorgeSeif/Semantic-Segmentation-Suite 

1. description
choose DeepLabV3 as the model, ResNet101 as the frontend net. There are other frontend nets: MobileNetV2, ResNet50/152, and InceptionV4.

2. prepare
I am using python3.5, tensorflow-gpu 1.13.1, numpy1.16.3 and you can use 'pip install' to install other packages or upgrade packages.

aiming to use gpu, I also use CUDA10.0 and cudnn10.0-v7.5.0.56
I will put them in the 'prepare' folder.

notice that different gpu will ask for different version of CUDA and cudnn. NVIDIA affords a list on their site.

it is very slow to train by using cpu, it took me over 30h to train under 70 images.

3. folders
5_5_trial_1 is the first trial. there are checkpoints, accuracy and loss graphs inside.

5_15_trial_2 is the second trial.

checkpoints contains the third trial. around 180 images are used, containing train, validation, and test. also has checkpoints and accuracy.

images contains a gif file, which is compressed by serialized 182 images, combining masks and original images to show effects.

pred_out is the folder that has predicted masks

predict_them has the images that are going to be prediced

Test contains test output and a score file that you can see the performance of the test

trial_3 has the organized files for training, vlidation and testing. class_dict is using RGB 0, 0, 0 as background and 1, 1, 1 as the robotics arm. you can add other colors to represent other objects

prepare.py: organize images and labels, like what trial_3 shows

refine_mask.py: tune some pixels that are not 0, 0, 0 nor 1, 1, 1

predict.py: to predict an image

test.py: to test an image set

train.py: to train

pred.py: use cmd to predict lots of images

**notice that you may need to change 'path' or 'dir' str in the code to run on your own device

4. commands explain
train
python train.py --num_epochs 250 --checkpoint_step 6 (6 epoches, 1 checkpoint) --validation_step 1 (validate for each epoch) --dataset trial_3 (the folder contains images) --crop_width 480 --crop_height 480 --batch_size 1 --model DeepLabV3 --frontend ResNet101

test
python test.py --checkpoint_path .\checkpoints\0080\model.ckpt (different dir for different checkpoints) --crop_height 480 --crop_width 640 --model DeepLabV3 --dataset trial_3

predict
python pred.py
or
python predict.py --image 'path' --checkpoint_path .\checkpoints\latest_model_DeepLabV3_trial_3.ckpt (different dir for different checkpoints) --crop_height 480 --crop_width 640 --model DeepLabV3 --dataset trial_3
