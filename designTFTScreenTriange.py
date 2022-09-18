from PIL import Image
im = Image.open(".\\testImage14.png").convert('RGB')

def main():

    triangle = []
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
                triangle.append([w,h])
                
            w += 1
            
    print(triangle)
    print("tft.fillTriangle("+str(triangle[0][0])+", "+str(triangle[0][1])+", "+str(triangle[1][0])+", "+str(triangle[1][1])+", "+str(triangle[2][0])+", "+str(triangle[2][1])+", "+"TFT_BLACK"+");")
main()

