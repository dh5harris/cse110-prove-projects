# This line imports or includes the library we will need
from PIL import Image


# This line opens the image and loads it into a variable called "image_original"
image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")
image_cat_small = Image.open("cat_small.jpg")

# This line accesses the pixel data of the image
pixels_beach = image_beach.load()
pixels_cactus = image_cactus.load()
pixels_cat_small = image_cat_small.load()

(width, height) = image_cactus.size

# This for loop is to over lap two green screen images
for y in range(330, height):
    for x in range(430, width):
        r, g, b = pixels_cactus[x, y]
        pixels_cactus[x, y] = pixels_cat_small[x, y]
        
# This for loop is to add the background image to the green screen image
for y in range(0, height):
    for x in range(0, width):
        r, g, b = pixels_cactus[x, y]
#         # if r >= 40 and r <= 100 and g >= 220 and b >= 0 and b <= 50:
#         # Bro. Wilson pointed out that the above IF statement is not as clean 
#         # as it could be. The IF statement is better
#         #if r <= 76 and g >= 244 and b <= 24:  
        if r <= 100 and g >= 220 and b <= 50: 
            pixels_cactus[x, y] = pixels_beach[x, y]

# This line displays image in a new window
image_cactus.show()

# This line saves the image
# image_cactus.save("beach_cactus_cat_small.jpg")
