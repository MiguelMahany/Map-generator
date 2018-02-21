from PIL import Image,ImageDraw

origin = [0,0]
resolution = [1920,1080]
image = Image.new('RGB',resolution,(255,255,255))
image.save("test.png","PNG")


def tile_Go(origin,res,gridres):
    res = res
    tile_size = gridres
    tile_size = 40
    if origin[0]>=res[0]:
        return True
    else:
        if origin[0] >= res[0]:
            origin[0]=0
            origin[1]+=-4*tile_size
        else:
            x=origin[0]
            y=origin[1]
            a = origin
            b = [1*tile_size,2*tile_size]
            c = [x,4*tile_size]
            d = [2*tile_size,y]
            e = [2*tile_size,4*tile_size]
            f = [4*tile_size,4*tile_size]
            g = [4*tile_size,y]
            pointa = (origin[0]),(origin[1])
            pointb = (origin[0]+b[0]), (origin[1]+b[1])
            pointc = (origin[0]+c[0]), (origin[1]+c[1])
            pointd = (origin[0]+d[0]), (origin[1]+d[1])
            pointe = (origin[0]+e[0]), (origin[1]+e[1])
            pointf = (origin[0]+f[0]), (origin[1]+f[1])
            pointg = (origin[0]+g[0]), (origin[1]+g[1])
            
            im = Image.open("test.png")
            

            lines = [pointa,pointb,pointc,pointb,pointd,pointg,pointd,pointb,pointe,pointf]

            draw = ImageDraw.Draw(im)
            draw.line(lines,fill="Black", width=1)
            draw.point(lines,fill="Black")
            draw.text(pointa,"point a", fill="Black",)
            draw.text(pointb,"point b", fill="Black",)
            draw.text(pointc,"point c", fill="Black",)
            draw.text(pointd,"point d", fill="Black",)
            draw.text(pointe,"point e", fill="Black",)
            draw.text(pointf,"point f", fill="Black",)
            draw.text(pointg,"point g", fill="Black",)
            print(pointa)
            print(pointg)
            origin = pointg
            im.save("test.png","PNG")

tile_Go(origin,resolution,1)