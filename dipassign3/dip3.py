import cv2
import numpy as np

rect = cv2.imread("C:\\Users\\Itesha\\DIP\\dipassign3\\rec.png")
circle = cv2.imread("C:\\Users\\Itesha\\DIP\\dipassign3\\cir.png")

And = cv2.bitwise_and(rect, circle)    # Bitwise AND
Nand = cv2.bitwise_not(And)            # Bitwise NAND

Or = cv2.bitwise_or(rect, circle)      # Bitwise OR
Nor = cv2.bitwise_not(Or)              # Bitwise Nor

notRect = cv2.bitwise_not(rect)        # Bitwise NOT
notCircle = cv2.bitwise_not(circle)

Xor = cv2.bitwise_xor(rect,circle)     # Bitwise XOR
Xnor = cv2.bitwise_not(Xor)            # Bitwise XNOR

cv2.imwrite("AND.jpg", And)
cv2.imwrite("NAND.jpg", Nand)
cv2.imwrite("OR.jpg", Or)
cv2.imwrite("NOR.jpg", Nor)
cv2.imwrite("NOTRectangle.jpg", notRect)
cv2.imwrite("NotCircle.jpg", notCircle)
cv2.imwrite("XOR.jpg", Xor)
cv2.imwrite("XNOR.jpg", Xnor)
cv2.waitKey(0)
cv2.destroyAllWindows()