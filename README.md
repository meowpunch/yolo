# YOLO PROJECT

window 10 base

1) YOLO
2) CCTV (Android IP webcam)  
3) Server (WAMP & python)



# 1. YOLO

1. Visual studio 2017
2. CUDA 10.0
3. cudnn 7.4.1
* you must install VS 2017 first as CUDA is installed in accordance with VS environment installed.
4. opencv3.4.0

5. git clone https://github.com/AlexeyAB/darknet.git
6. modify source code. 
* image_opencv.cpp ( func: draw_detections_cv_v3, save_mat_jpg )
* check demo.c that call fuction in image_opencv.cpp  
7. build darknet.sln


rf ) 
https://github.com/AlexeyAB/darknet#yolo-v3-in-other-frameworks


# 2. CCTV

1. install IP webcam in google store on android.
2. check IP:8080.


# 3. Server

1. Bitnami wamp (localhost server)
2. python 3.7
*import cgi,os
3. google map api


rf ) 
python web programming: https://opentutorials.org/course/3256
google map: https://cloud.google.com/maps-platform/?hl=ko
