import os

# 源文件夹和目标文件夹路径
folder_labels_new = 'C:/Users/a2857\Downloads\datasetsV11.19_china.v1i.yolov5pytorch/train/labels'
folder_labels = 'D:/DeepLearning\YOLO\Competition\datastesV11.19_CW34/valid\labels'

for filename in os.listdir(folder_labels):
    # 打开标签文件以供读取和写入
    with open(os.path.join(folder_labels, filename), 'r+') as file:
    # 逐行读取文件内容
        lines = file.readlines()

        # 将文件指针移动到文件开头，以便写入更改后的内容
        file.seek(0)

        for line in lines:
            # 使用split方法分割每一行，以空格或其他分隔符为准
            parts = line.strip().split()
            
            # 将第一个数字替换为新的类别标识
            if parts[0] == '3':
                new_class_id = 0
                parts[0] = str(new_class_id)
            if parts[0] == '4':
                new_class_id = 1
                parts[0] = str(new_class_id)

            # 重新构建每一行
            new_line = ' '.join(parts)
            
            # 写入更改后的内容到文件
            file.write(new_line + '\n')

        # 如果新内容比原内容短，删除多余的行
        file.truncate()