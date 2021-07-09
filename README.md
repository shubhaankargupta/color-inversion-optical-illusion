# Color Inversion Optical Illusion


Color inversion, as the name suggests, is the process of inverting the RGB values of an image, an array of pixels.

If:
1. Value of initial Red = X
2. Value of initial Blue = Y
3. Value of initial Green = Z

Then:
1. Value of final Red = 255-X
2. Value of final Blue = 255-Y
3. Value of final Green = 255-Z

As shown and well described [here](https://t3hz0r.com/post/colour-afterimage-optical-illusion-tutorial/), we noticed that an illusion is produced by consistently showing the viewer a chromatic-inverted image and suddenly flashing the image in greyscale. This gives the viewer an illusion of seeing the real image, which was never shown to him/her. The code adds textures to the image so that the illusion is more effective and a loading bar which self-caliberates to each image's dimensions.

In the file main.py, we present a fully automated method to produce this illusion using PILLOW.



## Install the following dependancies to get started:
```
from PIL import Image, ImageOps, ImageDraw
```

## Step 1
Invert the colors of the image
```
inverted = ImageOps.invert(img)
```

## Step 2
Convert the image to greyscale
```
imgGray = img.convert('L')
```

## Step 3
Add the loading bar and concatenate inverted the greyscale images
