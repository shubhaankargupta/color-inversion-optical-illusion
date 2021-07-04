from PIL import Image, ImageOps, ImageDraw

def ellipse(x, y, offset):
    image = Image.open(imgpath)
    inverted = ImageOps.invert(image)
    draw = ImageDraw.Draw(inverted)
    w1, h1 = inverted.size

    widthofbar = h1//40

    step = 10
    for n in range(step, w1, step):
        for p in range(step, h1 - step, step):
            draw.point((n, p))
    draw.ellipse((w1/2-5, h1/2-5, w1/2+5, h1/2+5), fill=(0, 0, 0))
    draw.line((x, y, x + offset, y), fill="white", width=widthofbar)
    return inverted


def make_gif(imgpath):
    frames = []
    image = Image.open(imgpath)
    imgGray = image.convert('L')
    draw2 = ImageDraw.Draw(imgGray)

    wbw, hbw = imgGray.size
    x = 0
    y = hbw/1.1
    offset = 0
    for number in range(wbw//30):
        offset += 30
        frames.append(ellipse(x, y, offset))
        x += 00
        y += 00
    step = 10
    for n in range(step, wbw, step):
        for x in range(step, hbw - step, step):
            draw2.point((n, x), fill="yellow")
    frames.append(imgGray)

    duration = 240000/wbw
    frame_one = frames[0]
    frame_one.save("circle.gif", format="GIF", append_images=frames,
                   save_all=True, duration=duration, quality=70)

imgpath = 'imgpath.jpeg'
if __name__ == "__main__":
    make_gif(imgpath)
