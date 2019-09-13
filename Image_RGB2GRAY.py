import cv2
img=cv2.imread('1.jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("orginal",img)
cv2.imshow("gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()