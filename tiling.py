from PIL import Image,ImageDraw

origin = [0,0]
resolution = [1920,1080]
image = Image.new('RGB',resolution,(255,255,255))
image.save("test.png","PNG")


def tile_Go(res,gridres):
    res = res
    tile_size = gridres
    origin = [0,0]
    x=0
    y=0
    print("eyyy")
    im = Image.open("test.png")

    while origin[1] < res[1]:
        while origin[0]<res[0]:
            if origin[0]<res[0]:
                a = [origin[0],origin[1]]
                b = [x + tile_size,y + 2*tile_size]
                c = [x,y+4*tile_size]
                d = [x+4*tile_size,y]
                e = [x+3*tile_size,y+2*tile_size]
                f = [x+4*tile_size,y+4*tile_size]
                g = [x+6*tile_size,y]
                h = [x+6*tile_size,y+4*tile_size]
                pointa = (a[0]),(a[1])
                pointb = (origin[0]+b[0]), (origin[1]+b[1])
                pointc = (origin[0]+c[0]), (origin[1]+c[1])
                pointd = (origin[0]+d[0]), (origin[1]+d[1])
                pointe = (origin[0]+e[0]), (origin[1]+e[1])
                pointf = (origin[0]+f[0]), (origin[1]+f[1])
                pointg = (origin[0]+g[0]), (origin[1]+g[1])
                pointh=((origin[0]+h[0]), (origin[1]+h[1]))
                lines = [pointa,pointb,pointc,pointb,pointe,pointd,pointg,pointd,pointe,pointf,pointh]

                draw = ImageDraw.Draw(im)
                draw.line(lines,fill="Black", width=1)
                # draw.point(lines,fill="Black")
                # draw.text(pointa,"point a", fill="Black",)
                # draw.text(pointb,"point b", fill="Black",)
                # draw.text(pointc,"point c", fill="Black",)
                # draw.text(pointd,"point d", fill="Black",)
                # draw.text(pointe,"point e", fill="Black",)
                # draw.text(pointf,"point f", fill="Black",)
                # draw.text(pointg,"point g", fill="Black",)
                # draw.text(pointh,"point h", fill="Black",)
                # print(pointa)
                # print(pointg)
                origin = pointg

        else:
            z=origin[1]
            z+=4*tile_size
            origin=[0,z]
    else:
        im.save("test.png","PNG")
        
    

tile_Go(resolution,5)