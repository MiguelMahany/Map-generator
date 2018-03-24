from PIL import Image

class ColorMap:

    def __init__(self,whi,greylow,greyhi,greenlow,greenhi,bluelow,bluehi):
        self.whi=whi
        self.greylow=greylow
        self.greyhi=greyhi
        self.greenlow=greenlow
        self.greenhi=greenhi
        self.bluelow = bluelow
        self.bluehi = bluehi

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
                if R < self.whi:
                    img.putpixel((x,y),WHITE)
                elif self.greylow< R < self.greyhi:
                    img.putpixel((x,y),GREY)
                elif self.greenlow<R<self.greenhi:
                    img.putpixel((x,y),GREEN)
                elif self.bluelow<R<self.bluehi:
                    img.putpixel((x,y),BLUE)
        img.save("ColorMap.png")