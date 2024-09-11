import os

source_folder_images = 'D:/DeepLearning/YOLO/Competition/datasetsV2/class4/images_trans'
source_folder_labels = 'D:/DeepLearning/YOLO/Competition/datasetsV2/class4/labels_trans_xml'

for filename in os.listdir(source_folder_labels):
    filename_new = filename.split(".")[0] + "_4" + ".xml" # 修改对应的后缀
    os.rename(os.path.join(source_folder_labels, filename), os.path.join(source_folder_labels, filename_new))
    print(filename_new)