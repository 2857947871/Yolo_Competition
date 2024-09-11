import cv2
import numpy as np
import os
import shutil

# 读取图像
image = cv2.imread('D:/DeepLearning/YOLO/Competition/jsai_data/output/22997-out_ori.jpg')

# 膨胀
# 分离图像通道
b, g, r = cv2.split(image)
# 定义膨胀核
kernel_dila = np.ones((3, 3), np.uint8)
# 分别对每个通道执行膨胀操作
dila_b = cv2.dilate(b, kernel_dila, iterations=2)
dila_g = cv2.dilate(g, kernel_dila, iterations=2)
dila_r = cv2.dilate(r, kernel_dila, iterations=2)
# 合并膨胀后的通道
dila_image = cv2.merge((dila_b, dila_g, dila_r))
# 显示膨胀后的彩色图像
cv2.imwrite('Dila Image.jpg', dila_image)


# 腐蚀
# 分离图像通道
b, g, r = cv2.split(image)
# 定义腐蚀核
kernel_erode = np.ones((3, 3), np.uint8)
# 分别对每个通道执行腐蚀操作
eroded_b = cv2.erode(b, kernel_erode, iterations=2)
eroded_g = cv2.erode(g, kernel_erode, iterations=2)
eroded_r = cv2.erode(r, kernel_erode, iterations=2)
# 合并腐蚀后的通道
eroded_image = cv2.merge((eroded_b, eroded_g, eroded_r))
# 显示腐蚀后的彩色图像
cv2.imwrite('Erode Image.jpg', eroded_image)


# 锐化
# 分离图像通道
b, g, r = cv2.split(eroded_image)
# 创建锐化核
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
# 分别应用卷积操作到每个通道
sharpened_b = cv2.filter2D(b, -1, kernel)
sharpened_g = cv2.filter2D(g, -1, kernel)
sharpened_r = cv2.filter2D(r, -1, kernel)
sharpened_b = cv2.dilate(sharpened_b, kernel_dila, iterations=1)
sharpened_g = cv2.dilate(sharpened_g, kernel_dila, iterations=1)
sharpened_r = cv2.dilate(sharpened_r, kernel_dila, iterations=1)
# 合并锐化后的通道
sharpened_image = cv2.merge((sharpened_b, sharpened_g, sharpened_r))
# 显示锐化后的图像
cv2.imwrite('Sharpened Image.jpg', sharpened_image)


# 开运算 开运算=腐蚀+膨胀
# 分离图像通道
b, g, r = cv2.split(image)
kernel_erode = np.ones((3, 3), np.uint8)
# dilate erode
Open_b = cv2.erode(b, kernel_erode, iterations=3)
Open_g = cv2.erode(g, kernel_erode, iterations=3)
Open_r = cv2.erode(r, kernel_erode, iterations=3)
Open_b = cv2.dilate(Open_b, kernel_erode, iterations=1)
Open_g = cv2.dilate(Open_g, kernel_erode, iterations=1)
Open_r = cv2.dilate(Open_r, kernel_erode, iterations=1)
# 合并腐蚀后的通道
Open_image = cv2.merge((Open_b, Open_g, Open_r))
# 显示腐蚀后的彩色图像
cv2.imwrite('Open Image.jpg', Open_image)

# 闭运算 闭运算=膨胀+腐蚀
# 分离图像通道
b, g, r = cv2.split(image)
kernel_erode = np.ones((3, 3), np.uint8)
# dilate erode
Close_b = cv2.dilate(b, kernel_erode, iterations=2)
Close_g = cv2.dilate(g, kernel_erode, iterations=2)
Close_r = cv2.dilate(r, kernel_erode, iterations=2)
Close_b = cv2.erode(Close_b, kernel_erode, iterations=1)
Close_g = cv2.erode(Close_g, kernel_erode, iterations=1)
Close_r = cv2.erode(Close_r, kernel_erode, iterations=1)
# 合并腐蚀后的通道
Close_image = cv2.merge((Close_b, Close_g, Close_r))
# 显示腐蚀后的彩色图像
cv2.imwrite('Close Image.jpg', Close_image)


# 中值滤波
kernel_size = 3
median_blurred = cv2.medianBlur(eroded_image, kernel_size)
# 保存滤波后的图像（可选）
cv2.imwrite('median_blurred_image.jpg', median_blurred)


output_path = 'D:/DeepLearning/YOLO/Competition/datasetsV4/images/train_new'
source_folder_images = 'D:/DeepLearning/YOLO/Competition/datasetsV4/images/train'
for filename in os.listdir(source_folder_images):
    image = cv2.imread(os.path.join(source_folder_images, filename))
    # 腐蚀
    # 分离图像通道
    b, g, r = cv2.split(image)
    # 定义腐蚀核
    kernel_erode = np.ones((3, 3), np.uint8)
    # 分别对每个通道执行腐蚀操作
    eroded_b = cv2.erode(b, kernel_erode, iterations=1)
    eroded_g = cv2.erode(g, kernel_erode, iterations=1)
    eroded_r = cv2.erode(r, kernel_erode, iterations=1)
    # 合并腐蚀后的通道
    eroded_image = cv2.merge((eroded_b, eroded_g, eroded_r))
    # 保存到指定文件夹
    cv2.imwrite(os.path.join(output_path, filename), eroded_image) 