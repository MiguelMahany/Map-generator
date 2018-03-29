from noise import pnoise2
import noise
from PIL import Image,ImageDraw


class NoiseMapGenerator:
    def __init__(self,WIDTH,HEIGHT,SCALE,OCTAVES,PERSISTANCE,LACUNARITY):
        self.WIDTH = int(WIDTH)
        self.HEIGHT = int(HEIGHT)
        self.CHECKSCALE = 0
        if int(SCALE) <=0:
            self.NEWSCALE = 1
            self.SCALE = 1/int(self.NEWSCALE)
            self.CHECKSCALE = 1
        else:
            self.SCALE=1/int(SCALE)
        self.OCTAVES = int(OCTAVES)
        self.PERSISTANCE = float(PERSISTANCE)
        self.LACUNARITY = float(LACUNARITY)


    def StartMap(self):
        if self.CHECKSCALE = 1:
            self.SCALE = 1/28
        if self.WIDTH <=0:
            self.WIDTH = 500
        if self.HEIGHT <= 0:
            self.HEIGHT = 500
        if self.OCTAVES <=0:
            self.OCTAVES = 3
        if self.PERSISTANCE <=0:
            self.PERSISTANCE = .5
        if self.LACUNARITY <=0:
            self.LACUNARITY = 2

        self.noisemap = [[0 for i in range (self.WIDTH)] for j in range(self.HEIGHT)]

        image = Image.new('RGB',(self.HEIGHT,self.WIDTH),'White')



        for y in range(0,self.HEIGHT):
            for x in range(0,self.WIDTH):
                self.noisemap[x][y] = pnoise2(x*self.SCALE,y*self.SCALE,self.OCTAVES,self.PERSISTANCE,self.LACUNARITY,1024,1024,0)

        draw = ImageDraw.Draw(image)
        for y in range(0,self.HEIGHT):
            for x in range(0,self.WIDTH):
                color = self.noisemap[x][y]
                color = int((1+(color*256))+ 128)
                if color > 256:
                    color = 256
                elif color < 0:
                    color= 0
                draw.point((x,y),fill = (color,color,color,255))
        image.save("NoiseMap.png")
        return True
