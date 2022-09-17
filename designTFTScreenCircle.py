from PIL import Image
im = Image.open(".\\testImage9.png").convert('RGB')

def main():

    circles = []
    width, height = im.size
    originalWidth = 0
    
    for h in range(height):
        w = 0
        while w<width:
            r,g,b = im.getpixel((w,h))
            rgb = [str(r),str(g),str(b)]
            for i in range(len(rgb)):
                rgb[i] = rgb[i].zfill(3)

            if ([r,g,b].count(100) == 3):
                
                w += 1
                r,g,b = im.getpixel((w,h))
                originalWidth = w
                
                while([r,g,b].count(000) == 3):
                    
                    if(w<(width-1)):
                        w += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,h))

                circles.append([originalWidth-1,h,w-originalWidth])
                originalWidth = w-originalWidth
            w += 1
    print(circles)

    for circle in circles:
        print("tft.fillCircle("+str(circle[0])+", "+str(circle[1])+", "+str(circle[2])+");")
main()

