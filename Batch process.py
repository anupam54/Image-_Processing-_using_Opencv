import cv2
import os
import sys
import fnmatch


def resize(fname,width, height):
    image = cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)

    org_height, org_width = image.shape[0:2]
    print("Width: ",org_width)
    print("Height: ",org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    return fname, new_image



listoffiles = os.listdir('.')
pattern = "*.jpg"
n = len(sys.argv)
if n == 3:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
else:
    width = 1280
    height = 960

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')
    
for filename in listoffiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_image = resize(filename, width, height)
        cv2.imwrite("new_folder\\"+filename, new_image)
        