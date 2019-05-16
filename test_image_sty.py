import cv2
import numpy as np

# call the build-in camera, so the parameter is 0, if there are other cameras, can adjust the parameter to 1,2
cap=cv2.VideoCapture(0)

while True:
    #从摄像头读取图片
    sucess,img=cap.read()
    #转为灰度图片
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #显示摄像头，背景是灰度。
    cv2.imshow("img",gray)
    #保持画面的持续。
    k=cv2.waitKey(1)
    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):
        #通过s键保存图片，并退出。
        cv2.imwrite("image2.jpg",img)
        cv2.destroyAllWindows()
        break
#关闭摄像头
cap.release()

