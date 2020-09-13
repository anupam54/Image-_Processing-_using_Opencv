import cv2
import numpy as np

def sharpen(image):
    kernel =np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    new_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow('sharpened', new_image)
    cv2.waitKey(0)
    return new_image
image = cv2.imread('nemo4.jpg')
sharpen(image)