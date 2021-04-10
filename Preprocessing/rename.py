import cv2
import numpy as np
import glob

images = []
i=1;
for img in glob.glob("data/gha/12/*.png"):
    image = cv2.imread(img);
    cv2.imwrite('Dataset/character_48_ghaha/'+ str(i)+'.png', image)
    i = i + 1;
