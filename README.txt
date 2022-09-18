|This is currently unfinished|
This program will read image files then turn them into commands used on tft screens for arduino
Currently if you change the path inside designTFTScreenRect.py and run it, it will output commands along the lines of tft.fillRect(x, y, width, height);
Same thing for designTFTScreenCircleMain.py
Same thing for designTFTScreenStraightLine.py (only works for straight lines, can overlap as much as you want)
designTFTScreenCircleMain.py needs you to add a pixel colored(100,100,100) in the top left of the middle of the circle, but this was just for testing, the main one does the same without the hassle.
designTFTScreenTriangle.py needs you to add one pixel colored(100,100,100) to each of the points, and only works for one triangle per image, however you can rotate it as much as you would like.

You cannot overlap most shapes, you can just export them as two different images.
