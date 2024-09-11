import os
import shutil

# 指定包含数据集图像和标签的文件夹路径
dataset_dir = "D:\DeepLearning\YOLO\Competition\A\labels_best_0.413"
class_counts = {}
# 创建一个空列表用于存储文件名信息
class023457_names = []

# 源文件夹和目标文件夹路径
source_folder_images = ' '
destination_folder_images = ' '
source_folder_labels = ' '
destination_folder_labels = ' '

# 遍历文件夹中的所有图像和标签文件
for filename in os.listdir(dataset_dir):
    if filename.endswith(".txt"):
        # 构建相应的标签文件名
        label_filename = filename
        print(filename)
        # 检查标签文件是否存在
        if label_filename in os.listdir(dataset_dir):
            with open(os.path.join(dataset_dir, label_filename), "r") as f:
                lines = f.readlines()
                for line in lines:
                    # 每行的格式通常为 "class_id x_center y_center width height"
                    parts = line.split()
                    if len(parts) > 0:
                        class_id = int(parts[0])
                        # 统计实例数量
                        if class_id in class_counts:
                            class_counts[class_id] += 1
                        else:
                            class_counts[class_id] = 1
                        if class_id == 3 or class_id == 4:
                                print(filename)
                                class023457_names.append(filename)
                                # 统计实例数量
                                if class_id in class_counts:
                                    class_counts[class_id] += 1
                                else:
                                    class_counts[class_id] = 1
                                break

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