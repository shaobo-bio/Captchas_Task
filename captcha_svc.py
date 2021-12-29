from PIL import Image, ImageOps
from sklearn import svm
# from sklearn.model_selection import train_test_split
import numpy as np
import glob
import os


class Captcha_svc():
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        # sort the files to make sure the input images correspond to the correct annotated text
        self.input_files = sorted(glob.glob(os.path.join(self.input_folder, '*.jpg')))
        self.output_files = sorted(glob.glob(os.path.join(self.output_folder, '*.txt')))

        # load the SVC classifier using the default parameters
        self.svc = svm.SVC()
        self.text_list = []
        self.img_set = []

        # build the training dataset (here I used all the provided files)
        self.__build_dataset__()
        # train the svc classifier
        self.__train__()

    def __build_dataset__(self):
        # build the character-image dataset
        img_set = np.zeros((len(self.output_files) * 5, 10, 8))
        for i in range(len(self.output_files)):
            im = Image.open(self.input_files[i])
            im = ImageOps.grayscale(im)
            im = np.array(im)

            with open(self.output_files[i], 'r') as f:
                text = f.read().strip()
                for j in range(len(text)):
                    char = text[j]
                    self.text_list.append(char)
                    im_c = im[11:21, 5 + 9 * j:13 + 9 * j]
                    img_set[i * 5 + j, :, :] = im_c

        im_n = len(img_set)
        img_set = img_set.reshape((im_n, -1))  # linearize the 2d image array into 1d
        self.img_set = img_set
        # for larger dataset, it can be splitted into training and testing groups to examine the model
        # x_train,x_test,y_train,y_test = train_test_split(self.img_list,self.text_list, test_size=0.1, random_state=0)

    def __train__(self):
        # train a svc classifier model using the collected training datasets
        self.svc.fit(self.img_set, self.text_list)

    def __save__(self, text_cap, save_path):
        # save the identified characters into files
        with open(save_path, 'w') as f:
            f.write(text_cap)

    def __call__(self, im_path, save_path):
        # identify unseen captcha images
        im = Image.open(im_path)
        im = ImageOps.grayscale(im)
        im.show()
        im = np.array(im)
        text_cap = []
        for j in range(5):
            char_img = im[11:21, 5 + 9 * j:13 + 9 * j]
            char_img = char_img.reshape(1, -1)
            text_cap.append(self.svc.predict(char_img)[0])

        text_cap = ''.join(text_cap)
        print(text_cap)
        self.__save__(text_cap, save_path)


if __name__ == "__main__":

    input_folder = "data/input"  # the folder of training image
    output_folder = "data/output"  # the folder of image annotation labels
    Captcha_my = Captcha_svc(input_folder, output_folder)

    input_file = "data/input100.jpg"  # path of unseen image
    output_file = "data/output100.txt"  # path of output image file
    Captcha_my(input_file, output_file)
