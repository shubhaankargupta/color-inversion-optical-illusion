# Color Inversion Optical Illusion


Color inversion, as the name suggests, is the process of inverting the RGB values of an image, an array of pixels.
```
If:
1. Value of initial Red = X
2. Value of initial Blue = Y
3. Value of initial Green = Z

Then:
1. Value of final Red = 255-X
2. Value of final Blue = 255-Y
3. Value of final Green = 255-Z
```
As shown and well described [here](https://t3hz0r.com/post/colour-afterimage-optical-illusion-tutorial/), we noticed that an illusion is produced by consistently showing the viewer a chromatic-inverted image and suddenly flashing the image in greyscale. This gives the viewer an illusion of seeing the real image, which was never shown to him/her. The code adds textures to the image so that the illusion is more effective and a loading bar which self-caliberates to each image's dimensions. **To use the illusion, stare at the black dot until the progress bar finishes - at which point the image should give the *perception* of being colored.**

In the file main.py, we present a fully automated method to produce this illusion using PILLOW.

![WhatsApp Image 2021-07-09 at 6 39 47 PM](https://user-images.githubusercontent.com/63454581/125087880-81d32680-e0ea-11eb-8516-5b1446f77941.jpeg)


## Install the following dependancies to get started:
```
from PIL import Image, ImageOps, ImageDraw
```

## Step 1
Invert the colors of the image
```
inverted = ImageOps.invert(img)
```
![inverted](https://user-images.githubusercontent.com/63454581/125088078-b2b35b80-e0ea-11eb-853f-a7f9ecc4ddda.jpeg)

## Step 2
Convert the image to greyscale
```
imgGray = img.convert('L')
```
![grey](https://user-images.githubusercontent.com/63454581/125088051-afb86b00-e0ea-11eb-8b28-2b2751d9e61e.jpeg)

## Step 3
Add the loading bar and concatenate inverted the greyscale images
![circle copy](https://user-images.githubusercontent.com/63454581/125088166-cbbc0c80-e0ea-11eb-96fb-caf22fb9a8d8.gif)
