# Captchas_Task

Here, one of the methods that solve the Captchas Identification issue is provided.

A website uses Captchas on a form to keep the web-bots away. However, the captchas it generates follow certain rules, including:

- the same number of characters
- same font and spacing each time
- background and foreground remains similar
- no skew in the structure of the characters 

In this folder the example captchas images and their corresponding texts are provided: 'data/input' and 'data/output'

This method uses binary image conversion and a hard-coded dictionary to perform the task:

First, captchas images were converted to binary images based on their intensity. Second, each image region corresponding to the character is cropped and stored in a dictionary. For unseen captchas image, it will also be processed similarly: converting to a binary image, cropped out each character region. Then each cropped out region will be referenced to the dictionary to identify their corresponding character. 

Here provides an example code that runs the scripts:

##################################################################################
from captcha import Captcha

input_folder = "data/input" #change this to the folder of input in your computer
output_folder = "data/output" #change this to the folder of output in your computer

Captcha_my = Captcha(input_folder,output_folder)

input_file = "data/input100.jpg" #change this to path of the test image
output_file = "data/output100.txt"  #change this to path of the saving file
Captcha_my(input_file,output_file)
##################################################################################
