## Color Inversion Optical Illusion


Color inversion, as the name suggests, is the process of inverting the RGB values of an image, an array of pixels.

If:
Value of initial Red = X
Value of initial Blue = Y
Value of initial Green = Z

Then:
Value of final Red = 255-X
Value of final Blue = 255-Y
Value of final Green = 255-Z

As shown and well described [here](https://t3hz0r.com/post/colour-afterimage-optical-illusion-tutorial/), we noticed that an illusion is produced by consistently showing the viewer a chromatic-inverted image and suddenly flashing the image in greyscale. This gives the viewer an illusion of seeing the real image, which was never shown to him/her.

In the file main.py, we present a fully automated method to produce this illusion using PILLOW.


Install the following dependancies to get started:
```
from PIL import Image, ImageOps, ImageDraw
```

