import cv2
import numpy as np

#import image
image = cv2.imread("test.png")

#grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
cv2.waitKey(0)

#binary
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('second',thresh)
cv2.waitKey(0)

#dilation
kernel = np.ones((12,12), np.uint8)

img_dilation = cv2.dilate(thresh, kernel, iterations=1)
cv2.imshow('dilated',img_dilation)
cv2.waitKey(0)

#find contours
ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = thresh[y:y+h, x:x+w]

    #resizing
    re_size = cv2.resize(roi,(28,28))
        #saving ROI
    cv2.imwrite('test.png', re_size)

    # show ROI
    cv2.imshow('segment no:'+str(i),re_size);
    cv2.rectangle(image,(x,y),( x + w, y + h ),(90,0,255),2);

