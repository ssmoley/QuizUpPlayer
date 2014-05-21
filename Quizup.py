from numpy import *  # import numpy
from scipy import misc
from VideoCapture import Device
import Image
import matplotlib.pyplot as pyplot
import PIL
import PIL.ImageOps
import pytesser
import scipy
import cv2
import numpy

testImg = 17
debugImage = False
debugImgCrop = True


def getImage():
    if testImg == False:
        cam = Device()
        img = cam.getImage()
        img = array(img)
    else:
        img = cv2.imread('16.jpg',0)
        img = rotateImage(img, 270)
        # img = Image.open(str(testImg) + '.jpg')
        # img = img.rotate(270)

    # img = PIL.ImageOps.fit(img, (1500,3000))
    # img = PIL.ImageOps.solarize(img,128)
    # img = PIL.ImageOps.autocontrast(img)
    # img = PIL.ImageOps.grayscale(img)
    # img = PILa2rray(img)
    # img = cv2.medianBlur(img,5)
    # img = img.mean(img, -1)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
            cv2.THRESH_BINARY, 11, 3)

    if debugImage == True:
        pyplot.imshow(img)
        pyplot.show()

    return img


#text = pytesser.image_to_string(img)
#print text
class Question:
    def __init__(self, img):
        self.img = img
        img = Image.fromarray(img)
        iQuestion = img.crop((0, 90, 360, 220))
        # iAnswerA = img.crop((40, 215, 330, 300))
        # iAnswerB = img.crop((40, 310, 330, 400))
        # iAnswerC = img.crop((40, 410, 330, 500))
        # iAnswerD = img.crop((40, 510, 330, 600))
        # iQuestion = img.crop((0, 500, 1500, 900))
        iAnswerA = img.crop((510, 280, 780, 350))
        iAnswerB = img.crop((510, 380, 780, 450))
        iAnswerC = img.crop((510, 480, 780, 550))
        iAnswerD = img.crop((510, 580, 780, 650))
        # img = PIL.ImageOps.autocontrast(iAnswerA)
        # img = PIL.ImageOps.autocontrast(iAnswerB)
        # img = PIL.ImageOps.autocontrast(iAnswerC)
        # img = PIL.ImageOps.autocontrast(iAnswerD)

        self.tQuestion = pytesser.image_to_string(iQuestion)
        self.tAnswerA = pytesser.image_to_string(iAnswerA)
        self.tAnswerB = pytesser.image_to_string(iAnswerB)
        self.tAnswerC = pytesser.image_to_string(iAnswerC)
        self.tAnswerD = pytesser.image_to_string(iAnswerD)

        if debugImgCrop == True:
            pyplot.imshow(iQuestion)
            print self.tQuestion
            pyplot.show()
            pyplot.imshow(iAnswerA)
            print self.tAnswerA
            pyplot.show()
            pyplot.imshow(iAnswerB)
            print self.tAnswerB
            pyplot.show()
            pyplot.imshow(iAnswerC)
            print self.tAnswerC
            pyplot.show()
            pyplot.imshow(iAnswerD)
            print self.tAnswerD
            pyplot.show()


def rotateImage(image, angle):  # parameter angel in degrees
    rows, cols = image.shape
    # print image.shape
    image_big = cv2.resize(image, (cols * 2, rows * 2))
    rot_mat = cv2.getRotationMatrix2D((cols, rows), angle, 0.5)
    result = cv2.warpAffine(image_big, rot_mat, (cols * 2, rows * 2), flags=cv2.INTER_LINEAR)
    # result = result[rows / 2: - rows / 2, cols / 2: - cols / 2]
    # print cols/1, rows/1
    # print result.shape, rows, cols
    # result = ndimage.rotate(image, 270)
    return result


img = getImage()
x = Question(img)

print x.tQuestion
print x.tAnswerA
print x.tAnswerB
print x.tAnswerC
print x.tAnswerD


