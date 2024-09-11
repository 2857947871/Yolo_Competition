import os
import sys
import cv2
import glob
import ntpath
from tqdm import tqdm
from ultralytics import YOLO
from class34Onnx import class34Pre
from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

list_of_arguments = sys.argv

#path = list_of_arguments[1]
#savepath = list_of_arguments[2]

path = "datasetsB"
savepath = "outputBV3"

Image_glob = os.path.join(path, "*.jpg")
Image_name_list = []
Image_name_list.extend(glob.glob(Image_glob))

model2  = YOLO('weights/yst_2.pt')
model5  = YOLO('weights/yst_5.pt')
model7  = YOLO('weights/yst_7.pt')

def convert(size, box): # xyxy2xywh
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]
    # round函数确定(xmin, ymin, xmax, ymax)的小数位数
    x = round(x * dw, 6)
    w = round(w * dw, 6)
    y = round(y * dh, 6)
    h = round(h * dh, 6)
    return x, y, w, h

def trans(data, savepath, filename, img_width, img_height):

    if not os.path.exists(savepath):
        os.makedirs(savepath)

    head, tail = os.path.splitext(filename)
    ana_txt_name = head + ".txt"  # 对应的txt名字，与jpg一致
    f_txt = open(os.path.join(savepath, ana_txt_name), 'a')
    for id in data:
        box = convert((img_width, img_height), id["bbox"])
        if float(box[1]) < 0.30:
            continue
        if id["category_id"] == 0:
            f_txt.write("%s %s %s %s %s\n" % (0, box[0], box[1], box[2], box[3]))
        elif id["category_id"] == 1:
            f_txt.write("%s %s %s %s %s\n" % (1, box[0], box[1], box[2], box[3]))
        elif id["category_id"] == 2:
            f_txt.write("%s %s %s %s %s\n" % (6, box[0], box[1], box[2], box[3]))
    f_txt.close()

detection_model = AutoDetectionModel.from_pretrained(
    model_type='yolov8',
    # YOLOv8模型的路径
    model_path="weights/yst_016.pt",
    # YOLOv8模型的路径
    confidence_threshold=0.20,
    # 设备类型。
    # 如果您的计算机配备 NVIDIA GPU，则可以通过将 'device' 标志更改为'cuda:0'来启用 CUDA 加速；否则，将其保留为'cpu'
    device="cuda:0",  # or 'cuda:0'
)

for imgpath in tqdm(Image_name_list):
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    head, tail = os.path.splitext(ntpath.basename(imgpath))
    ana_txt_name = head + ".txt"  # 对应的txt名字，与jpg一致
    f_txt = open(os.path.join(savepath, ana_txt_name), 'a+')

    #016
    result = get_sliced_prediction(
        imgpath,
        detection_model,
        slice_height=680,
        slice_width=680,
        overlap_height_ratio=0.15, # 宽度重叠
        overlap_width_ratio=0.15,
        postprocess_type='NMS',
        postprocess_match_threshold=0.01
    )

    data = result.to_coco_annotations()
    if len(data) > 0:
        src = cv2.imread(imgpath)
        image = src.shape
        height = image[0]
        width = image[1]
        trans(data, savepath, ntpath.basename(imgpath), width, height)

    #2
    result2=model2(imgpath)

    for r in result2:
        if len(r.boxes.cls)==0:
            break
        if r.boxes.xywhn[0][1] < 0.40:
            continue
        f_txt.write(f"2 {r.boxes.xywhn[0][0]} {r.boxes.xywhn[0][1]} {r.boxes.xywhn[0][2]} {r.boxes.xywhn[0][3]}\n")

    #34
    class34Pre(imgpath,savepath)

    #5
    result5=model5(imgpath, conf=0.2)

    for r in result5:
        if len(r.boxes.cls)==0:
            break
        if r.boxes.xywhn[0][1] < 0.40:
            continue
        f_txt.write(f"5 {r.boxes.xywhn[0][0]} {r.boxes.xywhn[0][1]} {r.boxes.xywhn[0][2]} {r.boxes.xywhn[0][3]}\n")

    #7
    result7=model7(imgpath)

    for r in result7:
        if len(r.boxes.cls)==0:
            break
        if r.boxes.xywhn[0][1] < 0.45:
            continue
        f_txt.write(f"7 {r.boxes.xywhn[0][0]} {r.boxes.xywhn[0][1]} {r.boxes.xywhn[0][2]} {r.boxes.xywhn[0][3]}\n")