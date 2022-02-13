import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Itesha\\DIP\\RBG\\image3.jpg")
red=img
red[:,:,1]=img[:,:,0]
cv2.imwrite('red.jpg', red)
cv2.waitKey(0)
cv2.destroyAllWindows()