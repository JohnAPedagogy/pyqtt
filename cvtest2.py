import cv2

print('imported')

img = cv2.imread('aio.png')

cv2.imshow('Output',img)
cv2.waitKey(0)