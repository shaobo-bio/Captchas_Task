# Captchas_Task

Here, two methods that solve the Captchas Identification issue are provided.The first method is based on simple image processing and dictionary referencing, the second method uses supervised machine learning.

Problem: Build a method that can identify the unseen captchas based on provided captchas image examples

A website uses Captchas on a form to keep the web-bots away. However, the captchas it generates follow certain rules, including:

- the same number of characters
- same font and spacing each time
- background and foreground remains similar
- no skew in the structure of the characters 

In this folder the example captchas images and their corresponding texts are provided: 'data/input' and 'data/output'

The first method ('captcha.py') uses binary image conversion and a hard-coded dictionary to perform the task:

First, captchas images were converted to binary images based on their intensity. Second, each image region corresponding to the character is cropped and stored in a dictionary. For unseen captchas image, it will also be processed similarly: converting to a binary image, cropped out each character region. Then each cropped out region will be referenced to the dictionary to identify their corresponding character. 

Here provides an example code that runs the scripts:

##################################################################################

from captcha import Captcha

input_folder = "data/input" #change this to the folder of 'input' in your computer
output_folder = "data/output" #change this to the folder of 'output' in your computer

Captcha_my = Captcha(input_folder,output_folder)

input_file = "data/input100.jpg" #change this to path of the test image
output_file = "data/output100.txt"  #change this to path of the saving file
Captcha_my(input_file,output_file)

##################################################################################


The second method ('captcha_svc.py') applies supervised machine learning to do this task: 

First, each image region that corresponds to the character was cropped out and stored as the image dataset. Second, using the captcha image dataset and their corresponding labels, a support vector classifier was trained. For an unseen image, image regions correpsond to each character were cropped out one by one and pass to the classifier to predict the character labeling. 

Here provides an example code that runs the scripts:

##################################################################################

from captcha_svc import Captcha_svc

input_folder = "data/input" #change this to the folder of 'input' in your computer
output_folder = "data/output" #change this to the folder of 'output' in your computer

Captcha_my = Captcha_svc(input_folder,output_folder)

input_file = "data/input100.jpg" #change this to path of the test image
output_file = "data/output100.txt"  #change this to path of the saving file
Captcha_my(input_file,output_file)

##################################################################################


