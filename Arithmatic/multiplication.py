import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Itesha\\DIP\\Arithmatic\\image3.jpg")
mult = np.zeros([183, 275, 3], dtype=np.uint8)

print(np.shape(img))  
for i in range(0,183):
    for j in range(0,275):
        for k in range(0,3):
            mult[i][j][k] = img[i][j][k] * 2   # Multipication
cv2.imwrite('multiply.jpg', mult)        
cv2.waitKey(0)
cv2.destroyAllWindows()