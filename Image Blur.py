import cv2

def blur(img):
    kernels = [3, 5, 9, 13, 100]
    for idx, k in enumerate(kernels):
        image_blur = cv2.blur(img, ksize = (k, k))
        cv2.imshow(str(k), image_blur)
        cv2.waitKey(0)
    return
image = cv2.imread('nemo4.jpg')
blur(image)