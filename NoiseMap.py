from opensimplex import OpenSimplex
from PIL import Image,ImageDraw

#This class generates a greyscale noise map 
class NoiseMapGenerator:
    def __init__(self,WIDTH,HEIGHT,SCALE,OCTAVES,PERSISTANCE,LACUNARITY,SEED):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCALE = SCALE
        self.OCTAVES = OCTAVES
        self.PERSISTANCE = PERSISTANCE
        self.LACUNARITY = LACUNARITY
        self.SEED = SEED
        self.noisemap = [[0 for i in range (self.WIDTH)] for j in range(self.HEIGHT)]
        

    def StartMap(self):
        tmp = OpenSimplex(self.SEED)
        image = Image.new('RGB',(self.HEIGHT,self.WIDTH),'White')
        if self.SCALE <=0:
            self.SCALE = 0.0001
        if self.WIDTH <=0:
            self.WIDTH = 1
        if self.HEIGHT <= 0:
            self.HEIGHT = 1

        for y in range(0,self.HEIGHT):
            for x in range(0,self.WIDTH):
                AMPLITUDE = 1
                FREQUENCY = 1
                NOISEHEIGHT = 0

                for i in range(self.OCTAVES):
                    samplex = x/self.SCALE*FREQUENCY
                    sampley = y/self.SCALE*FREQUENCY
                    simplexvalue = tmp.noise2d(samplex,sampley)
                    NOISEHEIGHT+= simplexvalue*AMPLITUDE
                    AMPLITUDE *= self.PERSISTANCE
                    FREQUENCY *= self.LACUNARITY

                self.noisemap[x][y]=NOISEHEIGHT
        draw = ImageDraw.Draw(image)
        for y in range(0,self.HEIGHT):
            for x in range(0,self.WIDTH):
                color = self.noisemap[x][y]
                color = int((color*128 )+ 128)
                draw.point((x,y),fill = (color,color,color,255))

        image.save("NoiseMap.png")
        return True

Map = NoiseMapGenerator(600,600,42,4,.5,2,5613)
Map.StartMap()