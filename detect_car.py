from yolo import *
import os
yolo = YOLO_np(**{'dump_model':False, 'image':True, 'input':'./path2your_video', 'model_image_size':(416, 416), 'output':'', 'pruning_model':False})
print(os.getcwd())

def car_on_image(path):
    img = Image.open('/home/misho/Uni/Vision/YOLO/keras-YOLOv3-model-set/example/dog.jpg')

    out_boxes, out_classes, out_scores = yolo.detect_image(img, True) 

    print(model_output[0])
    print(model_output[1])
    print(model_output[2])

    for i in range(len(out_classes)):
        if out_classes[i] == 2:
            box = out_boxes[i]
            box_area = (box[2]-box[0]) * (box[3]-box[1]) / (275*350)
            if box_area > 0.25:
                return True
    return False

