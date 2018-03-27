from noise import pnoise2
import noise
from PIL import Image,ImageDraw


class NoiseMapGenerator:
    def __init__(self,WIDTH,HEIGHT,SCALE,OCTAVES,PERSISTANCE,LACUNARITY):
        self.WIDTH = int(WIDTH)
        self.HEIGHT = int(HEIGHT)
        self.SCALE = int(SCALE)
        self.OCTAVES = int(OCTAVES)
        self.PERSISTANCE = float(PERSISTANCE)
        self.LACUNARITY = float(LACUNARITY)
        self.noisemap = [[0 for i in range (self.WIDTH)] for j in range(self.HEIGHT)]
        

    def StartMap(self):
        image = Image.new('RGB',(self.HEIGHT,self.WIDTH),'White')
        if self.SCALE <=0:
            self.SCALE = 0.0001
        if self.WIDTH <=0:
            self.WIDTH = 1
        if self.HEIGHT <= 0:
            self.HEIGHT = 1

        for y in range(0,self.HEIGHT):
            for x in range(0,self.WIDTH):
                self.noisemap[x][y] = pnoise2(x*.07,y*.07,self.OCTAVES,self.PERSISTANCE,self.LACUNARITY,1024,1024,3)
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