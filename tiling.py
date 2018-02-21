from PIL import Image,ImageDraw

origin = [0,0]
resolution = [100,100]
image = Image.new('RGB',resolution,(255,255,255))


def tile_Go(origin,res,gridres):
    res = res
    tile_size = gridres
    if origin >= res:
        return print("Done")
    else:
        if res[0]<=origin[0]&res[1]&res[1]:
            origin[0]=0
            origin[1]+=-4*tile_size
        else:
            #fix it yo#
            x=origin[0]
            y=origin[1]
            a = origin
            b = [1*tile_size,-2*tile_size]
            c = [x,-4*tile_size]
            d = [2*tile_size,y]
            e = [2*tile_size,-4*tile_size]
            f = [4*tile_size,-4*tile_size]
            g = [4*tile_size,y]
            pointa = (origin[0]),(origin[1])
            pointb = (origin[0]+b[0]), (origin[1]+b[1])
            pointc = (origin[0]+c[0]), (origin[1]+c[1])
            pointd = (origin[0]+d[0]), (origin[1]+d[1])
            pointe = (origin[0]+e[0]), (origin[1]+e[1])
            pointf = (origin[0]+f[0]), (origin[1]+f[1])
            pointg = (origin[0]+g[0]), (origin[1]+g[1])
            

            lines = (pointa,pointb),(pointb,pointc),(pointb,pointd),(pointb,pointe),(pointd,pointg),(pointe,pointf)

            draw = ImageDraw.Draw(image)
            draw.line(lines)
            image.save("test.png","PNG")
            tile_Go(origin,res,gridres)
            # fix it yo #

tile_Go(origin,resolution,1)