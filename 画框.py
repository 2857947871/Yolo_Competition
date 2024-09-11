import cv2
import os

# 设置图像和标签文件夹路径
image_folder = 'A/images'
label_folder = 'A/491'
output_folder = 'A\outputTmp'

# 获取所有图像文件
image_files = os.listdir(image_folder)

# 处理每张图像
for image_file in image_files:
    # 构建图像文件路径
    image_path = os.path.join(image_folder, image_file)

    # 读取图像
    image = cv2.imread(image_path)

    # 构建相应的标签文件路径
    label_file = os.path.splitext(image_file)[0] + '.txt'
    label_path = os.path.join(label_folder, label_file)

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
