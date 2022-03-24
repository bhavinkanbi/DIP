import cv2
import numpy as np

img = cv2.imread('image.jpg')
fil = np.ones((3,3),np.float32)/9
smooth = cv2.filter2D(img,-1,fil)

cv2.imwrite('smoothen.jpg', smooth)
#cv2.imshow('', smooth)
cv2.waitKey(0)
cv2.destroyAllWindows()

# When the filter size is increased, image gets more diffused 
