from PIL import Image, ImageOps, ImageDraw

def ellipse(x, y, offset):
    image = Image.open(imgpath)
    inverted = ImageOps.invert(image)
    draw = ImageDraw.Draw(inverted)
    w1, h1 = inverted.size

    step = 10
    for n in range(step, w1, step):
        for p in range(step, h1 - step, step):
            draw.point((n, p))

    draw.line((x, y, x + offset, y), fill="yellow", width=40)
    return inverted


def make_gif():
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

    frame_one = frames[0]
    frame_one.save("circle.gif", format="GIF", append_images=frames,
                   save_all=True, duration=200, quality=70)


if __name__ == "__main__":
    make_gif()
