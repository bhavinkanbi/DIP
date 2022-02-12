import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Itesha\\DIP\\dipassign1\\bk.jpg")
print(np.shape(img))
print(type(img[0][0][0]))
#shape [1091, 838, 3]

gray = np.zeros([1091, 838], dtype=np.uint8)
for i in range(0,1091):
    for j in range(0, 838):
        s = 0
        for k in range(0,3):
            s += img[i][j][k]
        gray[i][j] = s/3
        
cv2.imwrite('img_gray.jpg',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
