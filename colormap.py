from PIL import Image

class ColorMap:
    print("Heeyyyy")
    img = Image.open('NoiseMap.png')
    WIDTH,HEIGHT = img.size
    GREY = (50, 50, 50)
    GREEN = (0, 158, 0)
    BLUE = (0, 30, 129)
    WHITE = (255,255,255)
    for y in range(0,HEIGHT):
        for x in range(0,WIDTH):
            R,G,B = img.getpixel((x,y))
            # print(R,G,B)
            if R <5:
                img.putpixel((x,y),WHITE)
            elif 5< R < 20:
                img.putpixel((x,y),GREY)
            elif 20<R<80:
                img.putpixel((x,y),GREEN)
            else:
                img.putpixel((x,y),BLUE)
            # R,G,B = img.getpixel((x,y))
            # print(R,G,B)
    img.save("ColorMap.png")

ColorMap()