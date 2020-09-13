import cv2
def resize(fname,width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)
resize('nemo0.jpg',1280, 960)
