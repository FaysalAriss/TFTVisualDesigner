from PIL import Image
im = Image.open(".\\testImage6.png").convert('RGB')

def main():

    avoid = []
    rectangles = []
    rectW = 0
    rectH = 0
    width, height = im.size
    
    for h in range(height):
        w = 0
        while w<width:
            for rectangle in avoid:
                if rectangle[0] <= w and rectangle[2] >= w and rectangle[1] <= h and rectangle[3] >= h:
                    w = rectangle[2]+1
            r,g,b = im.getpixel((w,h))
            rgb = [str(r),str(g),str(b)]
            for i in range(len(rgb)):
                rgb[i] = rgb[i].zfill(3)
                
            #print("("+rgb[0]+" "+rgb[1]+" "+rgb[2]+")", end =" ")
            #print("h "+str(h)+" w "+str(w), end=" ")
            
            if [r,g,b].count(000) == 3:
                rectH = h
                rectW = w
                while([r,g,b].count(000) == 3):
                    
                    if(w<(width-1)):
                        w += 1
                    else:
                        break

                    r,g,b = im.getpixel((w,rectH))

                rectW = w-rectW
                rectH += 1
                r,g,b = im.getpixel((w-1,rectH))
                
                    
                while([r,g,b].count(000) == 3):
                    
                    #print("im.getpixel(("+str(w-1)+","+str(rectH)+"))", end= " ")
                    #print(" ("+str(r)+" "+str(g)+" "+str(b)+")")

                    if(rectH<(height-1)):
                        rectH += 1
                    else:
                        break
                    r,g,b = im.getpixel((w-1,rectH))
                
                rectH -= h
                    
                print("The rectangle is "+str(rectW)+" wide and "+str(rectH)+" tall.", end=" ")
                print("The rectangle starts at w: "+str(w-rectW)+" and h: "+str(h))
                rectangles.append([w-rectW, h, rectW, rectH])
                avoid.append([w-rectW, h, w-1, h+rectH-1])
            w += 1
        #print("")
    print(rectangles)
    print(avoid)

    for rectangle in rectangles:
        print("tft.fillRect("+str(rectangle[0])+", "+str(rectangle[1])+", "+str(rectangle[2])+", "+str(rectangle[3])+");")
    
main()

