import os

# 输入文件夹和输出文件夹的路径
input_folder = 'D:/DeepLearning/YOLO/Competition/datasets_BVN/ALL_train_new/txt'  # 输入文件夹包含YOLO格式的标签文件
output_folder = 'D:/DeepLearning/YOLO/Competition/datasets_BVN/ALL_train_new/new_txt'  # 输出文件夹将包含四边形坐标的标签文件

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的每个标签文件
for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r') as input_file:
            with open(output_path, 'w') as output_file:
                lines = input_file.readlines()
                for line in lines:
                    # 解析YOLO格式的标签
                    class_id, center_x, center_y, width, height = map(float, line.strip().split())

                    # 计算四边形坐标
                    x1 = center_x - width / 2
                    y1 = center_y - height / 2
                    x2 = center_x + width / 2
                    y2 = center_y - height / 2
                    x3 = center_x + width / 2
                    y3 = center_y + height / 2
                    x4 = center_x - width / 2
                    y4 = center_y + height / 2

                    # 写入四边形坐标格式的标签
                    output_file.write(f"{class_id} {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n")

print("标签文件转换完成。")
