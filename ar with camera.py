import cv2
import numpy as np
import time
import aruco_detection as ar
import camera 
import matplotlib.pyplot as plt

cam1 = camera.camera(0,1280,720)
# cam2 = camera.camera(1,1280,720)

x=0

while True:
    print(f'count:{x}')
    img = cam1.getImage()
    # img2 = cam2.getImage()
    cv_img=cv2.imshow("cameara",img)
    # cv_img2=cv2.imshow("cameara2",img2)
    # plt.imshow(img)
    # # plt.imshow(img2)
    # plt.show()
    # plt.close()
    # cv2.imshow("full",ar.arcode(img))
    if cv2.waitKey(1) == ord('q'):
        break
    x=x+1

cam1.release()   
cv2.destroyAllWindows()
