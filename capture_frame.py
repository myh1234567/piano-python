import cv2

cap=cv2.VideoCapture(0)
i=0
while(1):
    ret ,frame = cap.read()
    k=cv2.waitKey(1)
    cropImg = frame[20:400, 20:400]
    if k==27:
        break
    elif k==ord('s'):
        cv2.imwrite('/Users/yuhaomao/Desktop/lu_dianzan/'+str(i)+'.jpg',cropImg)
        i+=1
    cv2.rectangle(frame, (20,20), (400, 400), (0, 255, 0), 1)
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()