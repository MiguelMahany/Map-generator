from PIL import Image

class ColorMap:

    def __init__(self,white,grey,green):
        self.white=int(white)
        self.grey=int(grey)
        self.green=int(green)

    def Start(self): 
        img = Image.open('NoiseMap.png')
        WIDTH,HEIGHT = img.size
        GREY = (50, 50, 50)
        GREEN = (0, 158, 0)
        BLUE = (0, 30, 129)
        WHITE = (255,255,255)
        for y in range(0,HEIGHT):
            for x in range(0,WIDTH):
                R,G,B = img.getpixel((x,y))
                if R < self.white:
                    img.putpixel((x,y),WHITE)
                elif (self.white +1 )< R < self.grey:
                    img.putpixel((x,y),GREY)
                elif (self.grey + 1)<R<self.green:
                    img.putpixel((x,y),GREEN)
                elif (self.green + 1)<R:
                    img.putpixel((x,y),BLUE)
        img.save("ColorMap.png")
