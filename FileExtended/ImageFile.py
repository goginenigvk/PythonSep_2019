
""" 
imagefile=open('/Users/SRIRAMAPADMAPRABHA/Desktop/dolphins.png','rb')
print(imagefile.read())


imagewritemode=open('FileExtended/imagedoc.doc','wb')
print(imagewritemode.write('/Users/SRIRAMAPADMAPRABHA/Desktop/Penguin.png')) """
#pip install pillow 

from PIL import Image

dolphinsimage=Image.open('/Users/SRIRAMAPADMAPRABHA/Desktop/dolphins.png')
print(dolphinsimage)

dolphinsimage_roatate=dolphinsimage.rotate(180)
dolphinsimage_roatate.save('FileExtended/dolphinsimage_roatate.png')
print('done')


