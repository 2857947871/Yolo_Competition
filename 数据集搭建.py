import os
import cv2
import shutil

# 将 images 和 labels 分开至不同文件夹
# 原始文件夹路径
source_folder = 'C:/Users/a2857/Desktop/jsai_data'

# 目标文件夹
images_folder = 'C:/Users/a2857/Desktop/DeepLearning/YOLO/Competition/datasets/images'
labels_folder = 'C:/Users/a2857/Desktop/DeepLearning/YOLO/Competition/datasets/labels'
output_folder = 'C:/Users/a2857/Desktop/DeepLearning/YOLO/Competition/datasets/output_img'

# 创建目标文件夹（如果它们不存在）
os.makedirs(images_folder, exist_ok=True)
os.makedirs(labels_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)
    # 判断文件类型（通过文件扩展名）
    if filename.endswith('.jpg'):
        # 图像文件，复制到图像文件夹
        destination_path = os.path.join(images_folder, filename)
        shutil.copy(source_path, destination_path)
    elif filename.endswith('.txt'):
        # 标注文件，复制到标注文件夹
        destination_path = os.path.join(labels_folder, filename)
        shutil.copy(source_path, destination_path)

# 标注
# 获取所有图像文件
image_files = os.listdir(images_folder)
# 处理每张图像
for image_file in image_files:
    # 构建图像文件路径
    image_path = os.path.join(images_folder, image_file)

    # 读取图像
    print(image_path)
    image = cv2.imread(image_path)
    # print(image) # None

    # 构建相应的标签文件路径
    label_file = os.path.splitext(image_file)[0] + '.txt'
    label_path = os.path.join(labels_folder, label_file)

    if os.path.exists(label_path):
        # 读取标签文件并解析坐标信息
        with open(label_path, 'r') as f:
            label_data = f.read().split('\n')
        
        for label_info in label_data:
            if label_info:
                # 解析坐标信息（通常包括类别、中心坐标、宽度、高度）
                class_id, x, y, width, height = map(float, label_info.split())
                
                # 计算检测框的四个角的坐标
                x1 = int((x - width / 2) * image.shape[1])
                y1 = int((y - height / 2) * image.shape[0])
                x2 = int((x + width / 2) * image.shape[1])
                y2 = int((y + height / 2) * image.shape[0])

                # 绘制检测框
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 设置框的颜色和线宽
                cv2.putText(image, str(int(class_id)), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # 标注类别

        # 保存带有检测框的图像
        output_image_path = os.path.join(output_folder, image_file)
        cv2.imwrite(output_image_path, image)