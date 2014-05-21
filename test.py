from PIL import Image
import matplotlib.pyplot as pyplot
import time

# im = Image.open("question.png")
# im.show()



from VideoCapture import Device
cam = Device()
x = cam.getImage()
# pyplot.imshow(x)
# pyplot.show()

# for i in range(1, 20):
#     name = str(i) + '.jpg'
#     cam.saveSnapshot(name)
#     time.sleep(5)

img = Image.open('17.jpg')
img = img.rotate(270)


if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
    #create a threshold value
    threshold = 128
    #Create a reference to the alpha channel using the split function
    alpha = img.split()[3]
    #Apply the threshold using the point function
    alpha = alpha.point(lambda p: p > threshold and 255)
    #Paste a copy of the alpha object that has had the threshold applied.
    img.putalpha(alpha)

print img.size


pyplot.imshow(img)
# pyplot.show()