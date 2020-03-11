from PIL import Image as i
im = i.open("img.jpg")
im.rotate(90).save("img1.jpg")
print(im.size())
crp = 100,100,100,100
#im.crop(crp).save("img2.jpg")