from numpy import *
import scipy
import pytesser
import Image
import ImageFilter
import PIL
import PIL.ImageOps
from scipy import misc

img = Image.open('question.png')
# img = img.rotate(180)
# img = img.resize((480,640))
#img = img.filter(ImageFilter.BLUR)
#img = img.filter(ImageFilter.MinFilter(3))
#img = PIL.ImageOps.fit(img, (480,740), Image.ANTIALIAS)
#img = img.crop((0,120,640,400))

#pyplot.imshow(img)
# pyplot.show()

#text = pytesser.image_to_string(img)
#print text


class Question:

    def __init__(self, img):
        self.img = img
        ## Screenshot Resolution
        iQuestion = img.crop((0, 120, 640, 400))
        iAnswerA = img.crop((55, 410, 585, 565))
        iAnswerB = img.crop((55, 590, 585, 745))
        iAnswerC = img.crop((55, 770, 585, 925))
        iAnswerD = img.crop((55, 950, 585, 1105))

        ## Q2
        # iQuestion = img.crop((50, 80, 480, 200))
        # img = img.filter(ImageFilter.MinFilter(3))
        # iAnswerA = img.crop((55, 200, 480, 300))
        # iAnswerB = img.crop((55, 300, 480, 400))
        # iAnswerC = img.crop((55, 400, 480, 500))
        # iAnswerD = img.crop((55, 500, 480, 600))

        self.tQuestion = pytesser.image_to_string(iQuestion)
        self.tAnswerA = pytesser.image_to_string(iAnswerA)
        self.tAnswerB = pytesser.image_to_string(iAnswerB)
        self.tAnswerC = pytesser.image_to_string(iAnswerC)
        self.tAnswerD = pytesser.image_to_string(iAnswerD)


   # def ParseImage(self, img):
        # Screenshot Resolution
        # iQuestion = img.crop((0, 120, 640, 400))
        # iAnswerA = img.crop((55, 410, 585, 565))
        # iAnswerB = img.crop((55, 590, 585, 745))
        # iAnswerC = img.crop((55, 770, 585, 925))
        # iAnswerD = img.crop((55, 950, 585, 1105))


        pyplot.imshow(iQuestion)
        pyplot.show()
        pyplot.imshow(iAnswerA)
        pyplot.show()
        pyplot.imshow(iAnswerB)
        pyplot.show()
        pyplot.imshow(iAnswerC)
        pyplot.show()
        pyplot.imshow(iAnswerD)
        pyplot.show()

        # tQuestion = pytesser.image_to_string(iQuestion)
        # self.tAnswerA = pytesser.image_to_string(iAnswerA)
        # self.tAnswerB = pytesser.image_to_string(iAnswerB)
        # self.tAnswerC = pytesser.image_to_string(iAnswerC)
        # self.tAnswerD = pytesser.image_to_string(iAnswerD)



x = Question(img)

#print x.getAnswerA()
print x.tQuestion
print x.tAnswerA
print x.tAnswerB
print x.tAnswerC
print x.tAnswerD


