# RK3588的yolo26模型转换(pt->onnx)

本教程适用于6个输出头的onnx目标检测/10个输出头的分割/9个输出头的姿态/9个输出头的旋转模型

**在此感谢橘子的开源转换代码([li2390893](https://github.com/li2390893))**

第一步：获取本仓库代码

```bash
git clone https://github.com/rokkieluo/rk-yolo26.git
```

第二步：填写参数

一共有3个参数

参数1：det/seg/pose/obb（对应四种类型的模型）

参数2：./weights/xxx.pt（自己的pt模型路径）

参数3：./weights/xxx.onnx（生成的onnx模型路径）

以目标检测为例：

```bash
python export-onnx.py det ./weights/yolo26s.pt ./weights/yolov26s.onnx
```

其他模型依次类推

运行可能会报错，但是不影响onnx模型生成，只要能生成onnx模型，不必理会报错

至此就可以得到6个输出头的onnx目标检测/10个输出头的分割/9个输出头的姿态/9个输出头的旋转的onnx模型，可在netron中自行检查
