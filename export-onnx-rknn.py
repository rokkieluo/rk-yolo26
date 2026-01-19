from ultralytics import YOLO
import sys
# 选择类型：det, seg, pose, obb
model_type= sys.argv[1]
# 权重位置
input_model = sys.argv[2]

output_model = sys.argv[3]

if model_type == 'det':
    # 转为onnx：注意需要修改为对应的模型配置文件
    model = YOLO(input_model)
    results = model(task='detect', mode='predict', source='./test.jpg', imgsz=640, line_width=3, show=True, save=True, device='cpu')
elif model_type == 'seg':
    model = YOLO(input_model)
    print(model.model)
    results = model(task='detect', mode='predict', source='./test.jpg', imgsz=640, line_width=3, show=True, save=True, device='cpu')
elif model_type == 'pose':
    model = YOLO(input_model)
    results = model(task='detect', mode='predict', source='./test.jpg', imgsz=640, line_width=3, show=True, save=True, device='cpu')
elif model_type == 'obb':
    model = YOLO(input_model)
    results = model(task='detect', mode='predict', source='./test.jpg', imgsz=640, line_width=3, show=True, save=True, device='cpu')
