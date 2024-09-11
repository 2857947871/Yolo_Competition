import os
import shutil

# 指定包含数据集图像和标签的文件夹路径
dataset_dir = "D:/DeepLearning/YOLO/road_crack_voc/0345/labels"

# 要删除的数字
target_prefix = [1, 2, 6, 7, 8, 9]  # 例如，要删除以1开头的行

# 遍历文件夹中的所有图像和标签文件
for filename in os.listdir(dataset_dir):
    with open(os.path.join(dataset_dir, filename), 'r') as file:
    # 读取文件的所有行
        lines = file.readlines()
    # 打开标签文件以供写入，覆盖原始文件
    with open(os.path.join(dataset_dir, filename), 'w') as file:
        for line in lines:
            # 如果行不以指定数字开头，将其写回文件
            for i in range(6):
                if not line.strip().startswith(str(target_prefix[i])):
                    file.write(line)
