'''
MIT License

Copyright (c) 2021 Shubhaankar Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

#importing dependancies
from PIL import Image, ImageOps, ImageDraw


def make_gif(imgpath):
    frames = []
    image = Image.open(imgpath)
    
    #converting image to greyscale
    imgGray = image.convert('L')
    draw2 = ImageDraw.Draw(imgGray)
    
    wbw, hbw = imgGray.size
    x = 0
    y = hbw/1.1
    offset = 0
    for number in range(wbw//30):
        offset += 30
        image = Image.open(imgpath)
        #inverting colors of image
        inverted = ImageOps.invert(image)
        draw = ImageDraw.Draw(inverted)
        w1, h1 = inverted.size

        widthofbar = h1 // 40
        step = 10
        #adding texture for more effective illusion
        for n in range(step, w1, step):
            for p in range(step, h1 - step, step):
                draw.point((n, p))
        draw.ellipse((w1 / 2 - 5, h1 / 2 - 5, w1 / 2 + 5, h1 / 2 + 5), fill=(0, 0, 0))
        draw.line((x, y, x + offset, y), fill="white", width=widthofbar)
        frames.append(inverted)
        x += 00
        y += 00

    step = 10
    for n in range(step, wbw, step):
        for x in range(step, hbw - step, step):
            draw2.point((n, x), fill="yellow")
    frames.append(imgGray)

    duration = 240000/wbw
    frame_one = frames[0]
    frame_one.save("illusion.gif", format="GIF", append_images=frames,
                   save_all=True, duration=duration, quality=70, loop = 0)

imgpath = 'imgpath' #enter image path

make_gif(imgpath)
