import cv2
import glob
i = 1;
for img in glob.glob("online_data/character_04_gha/*.png"):
    image = cv2.imread(img);
    re_size = cv2.resize(image, (64, 64))
    # saving ROI
    cv2.imwrite('resizedTo64/gha/gha_'+str(i)+'.png', re_size)
    i= i+1;


