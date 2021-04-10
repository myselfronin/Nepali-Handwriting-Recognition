import cv2
import numpy as np
import glob

images = []
i=1;
print()
for img in glob.glob("CollectionScreenShot/gha/*.png"):
    # #ret, thresh = cv2.threshold(cv2.UMat(img),'', cv2.THRESH_BINARY_INV)
    image = cv2.imread(img);
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite('4_gha/gha/'+str(i)+'.png', thresh)
    i = i + 1;



