from ultralytics import YOLO

# Load a model
model = YOLO("yolo26s.pt")

# Export the model
model.export(format="onnx")