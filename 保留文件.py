import os
import shutil

# 指定包含数据集图像和标签的文件夹路径
dataset_dir = "D:/DeepLearning/YOLO/Competition/yolov5-masterV11(BiFPN+image_weights+label_smooth)/datasets/train/labels"
# 创建一个空字典用于存储类别统计信息
class_counts = {}
# 创建一个空列表用于存储文件名信息
class023457_names = []

# 源文件夹和目标文件夹路径
source_folder_images = 'D:/DeepLearning/YOLO/Competition/yolov5-masterV11(BiFPN+image_weights+label_smooth)/datasets/train/images'
destination_folder_images = 'D:/DeepLearning/YOLO/Competition/yolov5-masterV11(BiFPN+image_weights+label_smooth)/datasetsV10/images'
source_folder_labels = 'D:/DeepLearning/YOLO/Competition/yolov5-masterV11(BiFPN+image_weights+label_smooth)/datasets/train/labels'
destination_folder_labels = 'D:/DeepLearning/YOLO/Competition/yolov5-masterV11(BiFPN+image_weights+label_smooth)/datasetsV10/labels'

# 遍历文件夹中的所有图像和标签文件
for filename in os.listdir(dataset_dir):
    class023457_names.append(filename)

# 复制标签文件
for file_name_labels in class023457_names:
    source_path = os.path.join(source_folder_labels, file_name_labels)
    destination_path = os.path.join(destination_folder_labels, file_name_labels)

    # 使用shutil复制文件
    shutil.copy2(source_path, destination_path)

# 复制图像文件
for file_name_images in class023457_names:
    file_name_images = file_name_images.replace(".txt", ".jpg")
    source_path = os.path.join(source_folder_images, file_name_images)
    destination_path = os.path.join(destination_folder_images, file_name_images)

    # 使用shutil复制文件
    shutil.copy2(source_path, destination_path)

# 打印类别统计信息
for class_id, count in class_counts.items():
    print(f"Class {class_id}: {count} instances")
