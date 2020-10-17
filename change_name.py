import os
import sys
import cv2

path ='./img/origin_photo/'
for idx, filename in enumerate(os.listdir(path)):
    im = cv2.imread(path + filename)
    cv2.imwrite(path +'cc_'+str(idx+1)+'.jpg', im)
