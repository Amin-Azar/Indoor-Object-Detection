from imageai.Prediction import ImagePrediction
import os
import numpy as np

# PARAMETERS -----------------------------------------------
_result_count_per_image = 5
output_file_name = 'predictions.csv'
images_folder = 'images/'

# INITIALIZE -----------------------------------------------
execution_path = os.getcwd()
multiple_prediction = ImagePrediction()
multiple_prediction.setModelTypeAsResNet()
multiple_prediction.setModelPath(os.path.join(execution_path, "models/resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
multiple_prediction.loadModel()

# COLLECT IMAGES -----------------------------------------------
all_images_array = []
all_files = os.listdir(execution_path+ '/' + images_folder)
for each_file in all_files:
    if(not each_file.startswith('.') and each_file.endswith(".jpg")): # or .png
        all_images_array.append(images_folder+ each_file)

# PREDICT -----------------------------------------------
results_array = multiple_prediction.predictMultipleImages(all_images_array, result_count_per_image=_result_count_per_image)

# OUTPUT -----------------------------------------------
out_file  = open(output_file_name,'w')

header = ["IMAGE_ID"] + ["OBJECT"]*_result_count_per_image + ["Prob."]*_result_count_per_image
out_file.write(', '.join(header)+"\n")
for image, each_result in zip(all_images_array, results_array):    
    preds, probs = each_result["predictions"], each_result["percentage_probabilities"]
    str_imag, str_pred, str_prob = str(image), ', '.join(preds), ', '.join(str(v) for v in np.round(probs,1))
    str_out = [str_imag, str_pred, str_prob]
    out_file.write(', '.join(str_out)+"\n")
    
