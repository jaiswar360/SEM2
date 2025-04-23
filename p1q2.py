import cv2
cv2.imread
import matplotlib.pyplot as plot

myImg = cv2.imread("OIP.jpg")

greyImg = cv2.cvtColor(myImg, cv2.COLOR_BGR2GRAY)

cv2.imshow("og image", myImg)
cv2.imshow("Gray image", greyImg)

img3 = cv2.imread("OIP.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("img3", img3)



