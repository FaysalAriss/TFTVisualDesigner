|This is currently unfinished|
This program will read image files then turn them into commands used on tft screens for arduino
Currently if you change the path inside designTFTScreenRect.py and run it, it will output commands along the lines of tft.fillRect(x, y, width, height);
Same thing for designTFTScreenCircleMain.py
designTFTScreenCircleMain.py needs you to add a pixel colored(100,100,100) in the top left of the middle of the circle, but this was just for testing, the main one does the same without the hassle.

You cannot overlap any shapes, you can just export them as two different images.
