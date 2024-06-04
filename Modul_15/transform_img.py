
import cv2
import numpy as np

my_photo = cv2.imread('color_text.jpg')
new_img = np.zeros(my_photo.shape, dtype='uint8')

img = cv2.cvtColor(my_photo, cv2.COLOR_BGRA2GRAY)
img = cv2.GaussianBlur(img, (3,3),0)
img = cv2.Canny(img,30,30)

con, hir = cv2.findContours(img,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

sel_countours=[]
for i in range(377):
    sel_countours.append(con[i])
cv2.drawContours(new_img, sel_countours, -1, (250,125,200),2)

i = 377
sel_countours=[]
while i < 815:
    i += 1
    sel_countours.append(con[i])
cv2.drawContours(new_img, sel_countours, -1, (0,0,255),2)

i = 815
sel_countours=[]
while i < len(con):
    sel_countours.append(con[i])
    i += 1

cv2.drawContours(new_img, sel_countours, -1, (0,255,0),2)
cv2.imshow('Result', new_img)
cv2.waitKey(0)
