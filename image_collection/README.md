# บันทึกรูปภาพจากกล้อง webcam
โปรเจ็คนี้ถูกออกแบบมาเพื่อใช้ฝึก AI ตรวจจับวัตถุ(YOLO) โดยการรัน webcam_capture.py เพื่อบันทึกรูปถาพจากกล้องเว็ปแคมลงบนคอมพิวเตอร์
<br/>
<br/>
## สิงที่ต้องมี
 - เว็ปแคม
 - คอมพิวเตอร์
 - ภาษา python 3.9-3.12 และไลบรารี่ OpenCV 4.10
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
## วิธีใช้งาน
 - เปิดไฟล์ webcam_capture.py และรัน script
 - เมื่อมีกล้อง webcam โชว์บนหน้าจอแล้ว เราสามารถกด space เพื่อเรื่มการบันทึกรูปภาพ
<br/>
<br/>
