from imageai.Detection import ObjectDetection
import os
import numpy as np

# PARAMETERS -----------------------------------------------
_min_percentage = 30
output_file_name = 'detection.csv'
images_folder = 'images/'
out_images_folder = 'images_out/'

# INITIALIZE -----------------------------------------------
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "models/yolo.h5"))
detector.loadModel()

# COLLECT IMAGES -----------------------------------------------
all_images_array = []
all_files = os.listdir(execution_path+ '/' + images_folder)
for each_file in all_files:
    if(not each_file.startswith('.') and each_file.endswith(".jpg")): # or .png
        all_images_array.append(each_file)

# DETECTION -----------------------------------------------
results_array =[]
for image in all_images_array:
    in_image, out_image = images_folder + image , out_images_folder + image
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , in_image), output_image_path=os.path.join(execution_path , out_image), minimum_percentage_probability=_min_percentage)
    results_array.append(detections)

# OUTPUT -----------------------------------------------
out_file  = open(output_file_name,'w')

for image, detect_objs in zip(all_images_array, results_array):
    preds, probs = [], []
    # TODO: not reporting the largest percentage!
    for eachObject in detect_objs:
        if eachObject["name"] not in preds:
            preds.append(eachObject["name"])
            probs.append(eachObject["percentage_probability"])
    str_imag, str_pred, str_prob = str(image), ', '.join(preds), ', '.join(str(v) for v in np.round(probs,1))
    str_out = [str_imag, str_pred, str_prob]
    out_file.write(', '.join(str_out)+"\n")
