import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Itesha\\DIP\\RBG\\image3.jpg")
blue=img
blue[:,:,0]=img[:,:,1]

cv2.imwrite('blue.jpg', blue)
cv2.waitKey(0)
cv2.destroyAllWindows()
