from PIL import Image
im = Image.open(".\\testImage12.png").convert('RGB')

def main():

    avoid = []
    circles = []
    width, height = im.size
    circleWidth = 0
    circleHeight = 0
    isEven = False
    
    for h in range(height):
        w = 0
        while w<width:
            for circle in avoid:
                if circle[0] <= w and circle[2] >= w and circle[1] <= h and circle[3] >= h:
                    w = circle[2]+1
            r,g,b = im.getpixel((w,h))
            rgb = [str(r),str(g),str(b)]
            for i in range(len(rgb)):
                rgb[i] = rgb[i].zfill(3)

            if ([r,g,b].count(000) == 3):
                circleWidth = w
                circleHeight = h
                while([r,g,b].count(000) == 3):
                    
                    if(w<(width-1)):
                        w += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,h))

                if((w-circleWidth) % 2 == 0):
                    w = w - ((w-circleWidth)/2) - 1
                    isEven = True
                else:
                    w = w - ((w-circleWidth-1)/2) - 1
                    isEven = False

                r,g,b = im.getpixel((w,circleHeight))
                    
                while([r,g,b].count(000) == 3):
                    
                    if(circleHeight<(height-1)):
                        circleHeight += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,circleHeight))
                    
                circleHeight -= h
                if isEven:
                    circleHeight /= 2
                else:
                    circleHeight = (circleHeight-1)/2

                w += 1
                r,g,b = im.getpixel((w,circleHeight+h-1))
                originalWidth = w
                
                while([r,g,b].count(000) == 3):
                    
                    if(w<(width-1)):
                        w += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,circleHeight+h-1))

                middleW = originalWidth-1
                if isEven:
                    middleH = circleHeight+h-1
                else:
                    middleH = circleHeight+h
                radius = w-originalWidth
                circles.append([middleW,middleH,radius])
                if isEven:
                    avoid.append([middleW-radius+1, middleH-radius+1, middleW+radius, middleH+radius])
                else:
                    avoid.append([middleW-radius, middleH-radius+1, middleW+radius, middleH+radius+1])
                    
            w += 1
    print(circles)
    print(avoid)

    for circle in circles:
        print("tft.fillCircle("+str(circle[0])+", "+str(circle[1])+", "+str(circle[2])+", "+"TFT_BLACK"+");")
main()
