# yolo


after build, how to execute yolo.


IN CMD 

1. cd C:\darknet-master\darknet-master\build\darknet\x64   #Go to the directory where darknet.exe is located.

2. darknet.exe detector demo data/coco.data cfg/yolov3.cfg yolov3.weights http://192.168.0.80:8080/video?dummy=param.mjpg -i 0 
                      
                      # 192.168.0.80: you can check it in IP WEBCAM app. so befre 2 step, you should activate IP WEBCAM server.



