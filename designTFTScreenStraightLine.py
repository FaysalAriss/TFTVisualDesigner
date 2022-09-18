from PIL import Image
im = Image.open(".\\testImage20.png").convert('RGB')

def main():

    lines = []
    width, height = im.size
    originalWidth = 0
    
    for h in range(height):
        w = 0
        while w<width:
            for line in lines:
                if line[0] <= w and line[2] >= w and line[1] <= h and line[3] >= h:
                    w = line[2]+1
                    
            r,g,b = im.getpixel((w,h))
            rgb = [str(r),str(g),str(b)]
            for i in range(len(rgb)):
                rgb[i] = rgb[i].zfill(3)

            if ([r,g,b].count(000) == 3):
                line = [w,h]
                x = w
                y = h
                doubleLine = False
                
                while([r,g,b].count(000) == 3):
                    
                    if(w<(width-1)):
                        w += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,h))

                w -= 1

                if(w == x):
                    pass
                else:
                    line.append(w)
                    line.append(h)
                    doubleLine = True

                r,g,b = im.getpixel((x,h))
              
                while([r,g,b].count(000) == 3):
                    
                    if(y<(width-1)):
                        y += 1
                    else:
                        break

                    r,g,b = im.getpixel((x,y))

                y -= 1



                if(y == h):
                    pass
                else:
                    if doubleLine:
                        line.append(x)
                        line.append(h)
                    line.append(x)
                    line.append(y)

                if len(line)>4:
                    lines.append(line[:4])
                    lines.append(line[4:])
                else:
                    lines.append(line)
                
                    
            w += 1
            
    print(lines)
    for line in lines:
        print("tft.drawLine("+
              str(line[0])+ ", "+
              str(line[1])+ ", "+
              str(line[2])+ ", "+
              str(line[3])+ ", "+
              "TFT_BLACK);")
main()

