import cv2
im_g=cv2.imread("smallgray.png", 0) #1 rgb
#cv2.imwrite("new.png", im_g)
for i in im_g.flat:
    print(i)
