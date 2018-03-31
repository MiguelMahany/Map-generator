from PIL import Image,ImageDraw
import colormap


origin = [0, 0]
resolution = [100, 100]
image = Image.new('RGB', resolution, (255, 255, 255))
image.save("test.png", "PNG")


def grid(res, gridres):
    res = res
    tile_size = gridres
    origin = [0, 0]
    x = 0
    y = 0
    im = Image.open("test.png")

    while origin[1] < res[1]:
        while origin[0] < res[0]:
            if origin[0] < res[0]:
                a = [origin[0], origin[1]]
                b = [x+tile_size, y+2*tile_size]
                c = [x, y+4*tile_size]
                d = [x+4*tile_size, y]
                e = [x+3*tile_size, y+2*tile_size]
                f = [x+4*tile_size, y+4*tile_size]
                g = [x+6*tile_size, y]
                h = [x+6*tile_size, y+4*tile_size]
                center0 = [x, y+1.5*tile_size]
                center1 = [x+2*tile_size, y+1.5*tile_size]
                pointa = (a[0]), (a[1])
                pointb = (origin[0]+b[0]), (origin[1]+b[1])
                pointc = (origin[0]+c[0]), (origin[1]+c[1])
                pointd = (origin[0]+d[0]), (origin[1]+d[1])
                pointe = (origin[0]+e[0]), (origin[1]+e[1])
                pointf = (origin[0]+f[0]), (origin[1]+f[1])
                pointg = (origin[0]+g[0]), (origin[1]+g[1])
                pointh = ((origin[0]+h[0]), (origin[1]+h[1]))
                pointcenter1 = (origin[0] + center1[0], (origin[1] + center1[1]))
                pointcenter0 = (origin[0] + center0[0], (origin[1] + center0[1]))
                lines = [pointa, pointb, pointc, pointb, pointe, pointd,
                         pointg, pointd, pointe, pointf, pointh]

                draw = ImageDraw.Draw(im)
                draw.line(lines, fill="Black", width=1)
                ImageDraw.floodfill(im, xy=pointcenter1, value=(255, 255, 255, 255))
                ImageDraw.floodfill(im, xy=pointcenter0, value=(0, 0, 0, 255))

                origin = pointg

        else:
            z = origin[1]
            z += 4*tile_size
            origin = [0, z]
    else:

        im.save("test.png", "PNG")
        print("Done")


grid(resolution, 5)
