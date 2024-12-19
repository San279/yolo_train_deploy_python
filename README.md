# ฝึก/รัน Yolov11 AI ตรวจจับวัตถุ
โปรเจ็คนี้ถูกออกแบบมาสำหรับการฝึกและรัน Yolo v11 AI ตรวจจับวัตถุบนคอมพิวเตอร์ของเรา โดยเราจะมี 3 ขั้นตอนสำหรับการฝึก AI ขึ้นมาเอง
- รวบรวมรูปภาพ
- label image หรือ วาดกรอบวัตถุในรูปภาพ เพื่อเริ่มการฝึก AI
- รันโมเดลของเรา

## สิงที่ต้องมี
 - เว็ปแคม
 - คอมพิวเตอร์
 - ภาษา python 3.9-3.12 และไลบรารี่ OpenCV 4.10 และะ ultralytics
<br/>
<br/>

## หากไม่มี OpenCV หรือ Python 
  - เปิด cmd บน windows หรือ terminal บน linux/Mac OS และรัน command ตามด้านล่าง
### ดาวโหลด Python
  - สำหรับโปรเจ็คนี้ควรมี python 3.9 - 3.12
  - เช็ค python บนคอมพิวเตอว์ของเรา
```text1
  python
```
  - ถ้าเวอร์ชั่นต่ำกว่าที่กำหนด [ดาวโหลดใหม่](https://www.python.org/downloads/)
  - สำหรับ windows เมื่อ download เสร็จแล้ว เปลี่ยน path บนคอมพิวเตอร์เราเพื่อเริ่มการใช้งาน
### ดาวโหลด OpenCV
```text1
pip install --force-reinstall numpy==1.26.4
```
```text1
pip install --force-reinstall scipy==1.13.1
```
```text1
pip install --force-reinstall opencv-python==4.10.0
```

### ดาวโหลด Ultralytics 
```text1
pip install ultralytics supervision roboflow
```

## วิธีใช้งาน
- ดาวโหลดโปรเจ็คนี้ลงบนคอมพิวเตอร์ของเรา
### รันโมเดล มาตฐานของ Yolo v11 
  - เปิดแฟ้ม [deploy](https://github.com/San279/yolo_train_deploy_python/tree/main/deploy) และรันไฟล์ yolo_deploy.py
### รันโมเดลที่เราสร้างขึ้นเอง
  - [รวบรวมรูปภาพ](https://github.com/San279/yolo_train_deploy_python/tree/main/image_collection)
  - [วาดกรอบวัตถุในรูปภาพ/ฝึก โมเดล](https://github.com/San279/yolo_train_deploy_python/tree/main/train)
 -  [รันโมเดล](https://github.com/San279/yolo_train_deploy_python/tree/main/deploy) และรันไฟล์ yolo_deploy.py
