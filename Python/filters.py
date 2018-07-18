from PIL import Image

filename=input("Enter filename")
im = Image.open (filename)

def load_img(filename):
    im = Image.open (filename)
    show_img (im)

def show_img(im):
    im.show ()
    save_img (filename,im)
    return im

def save_img (filename,im):
    im.save ('newimage1', "jpeg")
    #show_img (im)

load_img (filename)

def obamicon(im):
    blue = (0, 0, 205)
    green = (0, 205, 0)
    purple = (102, 1, 152)
    red = (190, 38, 37)
    yellow = (217, 217, 25)
    data = list (im.getdata())
    new_img = []

    for p in data:
        r = p [0]
        g = p [1]
        b = p [2]
        intensity = r + g + b
        if intensity < 153:
            new_img.append (red)

        elif intensity >= 153 and intensity <306:
            new_img.append (purple)

        elif intensity >= 306 and intensity < 459:
            new_img.append (green)
        elif intensity >= 459 and intensity < 612:
            new_img.append (yellow)
        else:
            new_img.append (blue)
#save image new filter
    newim = Image.new("RGB", im.size)
    newim.putdata(new_img)
    return newim

show_img(obamicon (im))
