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
            a = (origin)
            b = [1*tile_size,-2*tile_size]
            b = [sum(i) for i in zip(a,b)]
            c = [x,-4*tile_size]
            c = [sum(i) for i in zip(a,c)]
            d = [2*tile_size,y]
            d = [sum(i) for i in zip(a,d)]
            e = [2*tile_size,-4*tile_size]
            e = [sum(i) for i in zip(a,e)]
            f = [4*tile_size,-4*tile_size]
            f = [sum(i) for i in zip(a,f)]
            h = [4*tile_size,y]
            h = [sum(i) for i in zip(a,h)]
            

            lines = [(a,b),(b,c),(b,d),(b,e),(d,h),(e,f)]

            draw = ImageDraw.Draw(image)
            draw.line(lines)
            image.save("test.png","PNG")
            tile_Go(origin,res,gridres)
            # fix it yo #

tile_Go(origin,resolution,1)