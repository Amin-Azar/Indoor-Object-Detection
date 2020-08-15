import os
import cv2
import re
from pytesseract import image_to_string

# https://towardsdatascience.com/read-text-from-image-with-one-line-of-python-code-c22ede074cac
# PARAMETERS -----------------------------------------------
images_folder = 'images/'
text_info_file="text_info.csv"
wb_re="(https?:\/\/)?(www\.)?([a-zA-Z0-9]+(-?[a-zA-Z0-9])*\.)+[\w]{2,}(\/\S*)?$"
ph_re="(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"

# INITIALIZE -----------------------------------------------
execution_path = os.getcwd()

# COLLECT IMAGES -----------------------------------------------
all_images_array = []
all_files = os.listdir(execution_path+ '/' + images_folder)
for each_file in all_files:
    if(not each_file.startswith('.') and each_file.endswith(".jpg")): # or .png
        all_images_array.append(each_file)

# DETECTION -----------------------------------------------
print("printing message: ")
ti = open(text_info_file,"w")
for image in all_images_array:
    in_image = images_folder + image
    txt_in_image = image_to_string(cv2.imread(in_image), lang='eng')
    emails = re.findall('\S+@\S+', txt_in_image)
    phones = re.findall(ph_re, txt_in_image)
    websites = re.findall(wb_re, txt_in_image)
    ti.write(in_image+", " + str(websites) + ", " + str(emails) + ", "+ str(phones) + str(txt_in_image).replace("\n", "|") +"\n")
