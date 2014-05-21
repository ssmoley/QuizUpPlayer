import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('16.jpg',0)

# global thresholding
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms
titles = ['img','histogram1','th1',
          'img','histogram2','th2',
          'blur','histogram3','th3']

for i in xrange(3):
    plt.subplot(3,3,i*3+1),plt.imshow(eval(titles[i*3]),'gray')
    plt.title(titles[i*3])
    plt.subplot(3,3,i*3+2),plt.hist(eval(titles[i*3]).ravel(),256)
    plt.title(titles[i*3+1])
    plt.subplot(3,3,i*3+3),plt.imshow(eval(titles[i*3+2]),'gray')
    plt.title(titles[i*3+2])

# img = rotateImage(img, 90)

def rotateImage(image, angle):  #parameter angel in degrees
    height = image.shape[0]
    width = image.shape[1]
    height_big = height * 2
    width_big = width * 2
    image_big = cv2.resize(image, (width_big, height_big))
    image_center = (width_big/2, height_big/2)#rotation center
    rot_mat = cv2.getRotationMatrix2D(image_center,angle, 0.5)
    result = cv2.warpAffine(image_big, rot_mat, (width_big, height_big), flags=cv2.INTER_LINEAR)
    return result


img = rotateImage(img, 90)

plt.imshow(img)
plt.show()