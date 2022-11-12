import torch
from glob import glob

img_path = r"./original"

img_list = glob(img_path + "/*.jpg")
img_list.extend(glob(img_path + "/*.png"))

print(img_list)

model = torch.hub.load(
    "ultralytics/yolov5",
    "yolov5s",
    pretrained=True,
)

print(model)

for img_path in img_list:
    results = model(img_path)
    print(img_path)
    results.save(r"./checking")
    for pred in results.pred[0]:
        tag = results.names[int(pred[-1])]
        print(tag)
