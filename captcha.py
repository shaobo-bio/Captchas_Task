from PIL import Image, ImageOps
import numpy as np
import glob
import os


class Captcha():
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        self.input_files = sorted(glob.glob(os.path.join(self.input_folder, '*.jpg')))
        self.output_files = sorted(glob.glob(os.path.join(self.output_folder, '*.txt')))

        self.__build_dict__(self.input_files, self.output_files)

    def __image_process__(self, im):
        im = ImageOps.grayscale(im)
        im = np.array(im)
        bw = im < 100
        return bw

    def __build_dict__(self,input_files,output_files):
        dict_cap = {}
        # generate a captcha dictionary of all the characters
        for i in range(len(self.output_files)):
            im = Image.open(self.input_files[i])
            bw = self.__image_process__(im)

            with open(output_files[i], 'r') as f:
                text = f.read().strip()
                # text_list.append(text)

                for j in range(len(text)):
                    char = text[j]
                    if char not in dict_cap.keys():
                        img = Image.fromarray(bw[11:21, 5 + 9 * j:13 + 9 * j])
                        dict_cap[char] = bw[11:21, 5 + 9 * j:13 + 9 * j]
        self.dict_cap = dict_cap

    def __save__(self, text_cap, save_path):
        with open(save_path, 'w') as f:
            f.write(text_cap)


    def __call__(self,im_path,save_path):
        im = Image.open(im_path)
        im.show()
        bw = self.__image_process__(im)
        text_cap = []
        for j in range(5):
            value_bw = bw[11:21, 5 + 9 * j:13 + 9 * j]

            for key, value in self.dict_cap.items():
                if (value_bw == value).all():
                    text_cap.append(key)
        text_cap=''.join(text_cap)
        print(text_cap)
        self.__save__(text_cap,save_path)


if __name__  == "__main__":
    input_folder = "/Users/shaobo/Desktop/captchas/sampleCaptchas/input"
    output_folder = "/Users/shaobo/Desktop/captchas/sampleCaptchas/output"
    Captcha_my = Captcha(input_folder,output_folder)

    input_file = "/Users/shaobo/Desktop/captchas/sampleCaptchas/input100.jpg"
    output_file = "/Users/shaobo/Desktop/captchas/sampleCaptchas/output100.txt"
    Captcha_my(input_file,output_file)

