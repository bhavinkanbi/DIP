# Binarization of Image
# Pixel having value greater than equal to threshold, pixel value = 255 (white)
# else pixel value equal to 0 (black)
import cv2
import numpy as np

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(np.shape(gray))      #Output (183, 275)

cv2.imwrite('gray.jpg', gray)
cv2.waitKey(0)

T = 100      # Threshold
for i in range(0,183):
    for j in range(0, 275):
        if(gray[i][j] >= T):
            gray[i][j] = 255
        else:
            gray[i][j] = 0

cv2.imwrite('binary.jpg', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()