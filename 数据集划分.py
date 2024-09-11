import os
import random
import shutil

# 假设你有包含图片文件的文件夹和包含标签文件的文件夹
image_folder = "D:/DeepLearning/YOLO/Competition/datasetsV11.18(重新打标但无任何更改)/datasetsV1.18/images"
label_folder = "D:/DeepLearning/YOLO/Competition/datasetsV11.18(重新打标但无任何更改)/datasetsV1.18/labels"
output_img_folder = "D:\DeepLearning\YOLO\Competition\datasetsV11.18(重新打标但无任何更改)/images"
output_lab_folder = "D:\DeepLearning\YOLO\Competition\datasetsV11.18(重新打标但无任何更改)/labels"

# 创建输出文件夹（如果不存在）
os.makedirs(output_img_folder, exist_ok=True)
os.makedirs(output_lab_folder, exist_ok=True)
os.makedirs(os.path.join(output_img_folder, "train"), exist_ok=True)
os.makedirs(os.path.join(output_img_folder, "test"), exist_ok=True)
os.makedirs(os.path.join(output_img_folder, "val"), exist_ok=True)
os.makedirs(os.path.join(output_lab_folder, "train"), exist_ok=True)
os.makedirs(os.path.join(output_lab_folder, "test"), exist_ok=True)
os.makedirs(os.path.join(output_lab_folder, "val"), exist_ok=True)

# 获取图片文件和标签文件的列表
image_files = os.listdir(image_folder)
label_files = os.listdir(label_folder)

# 随机打乱文件列表
random.shuffle(image_files)

# 计算划分比例
total_samples = len(image_files)
train_ratio = 0.8
val_ratio = 0.15
test_ratio = 0.05

# 计算划分点
train_split = int(total_samples * train_ratio)
val_split = int(total_samples * (train_ratio + val_ratio))

# 划分数据集
train_set = image_files[:train_split]
val_set = image_files[train_split:val_split]
test_set = image_files[val_split:]

# 将文件拷贝到对应的文件夹
def copy_files(file_list, src_img_folder, src_lab_folder, dst_img_folder, dst_lab_folder):
    for filename in file_list:
        src_image = os.path.join(src_img_folder, filename)
        src_label = os.path.join(src_lab_folder, filename.replace(".jpg", ".txt"))
        dst_image = os.path.join(dst_img_folder, filename)
        dst_label = os.path.join(dst_lab_folder, filename.replace(".jpg", ".txt"))
        shutil.copyfile(src_image, dst_image)
        shutil.copyfile(src_label, dst_label)

"""
image_folder = "datasets/images"
label_folder = "datasets/label"
output_img_folder = "datasets_new/images"
output_lab_folder = "datasets_new/label"
"""

# 拷贝训练集文件
copy_files(train_set, image_folder, label_folder, 
           os.path.join(output_img_folder, "train"),
           os.path.join(output_lab_folder, "train"))

# 拷贝验证集文件
copy_files(val_set, image_folder, label_folder, 
           os.path.join(output_img_folder, "val"),
           os.path.join(output_lab_folder, "val"))

# 拷贝测试集文件
copy_files(test_set, image_folder, label_folder, 
           os.path.join(output_img_folder, "test"),
           os.path.join(output_lab_folder, "test"))