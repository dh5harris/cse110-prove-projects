# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_beach = Image.open("beach.jpg")
image_cactus = Image.open("cactus.jpg")

# This line attempts to open a new window to display the image.
#image_original.show()

# This line accesses the pixel data of the image
pixels_beach = image_beach.load()
pixels_cactus = image_cactus.load()

(width, height) = image_cactus.size

for y in range(0, height):
    for x in range(0, width):
        r, g, b = pixels_cactus[x, y]
        # if r >= 40 and r <= 100 and g >= 220 and b >= 0 and b <= 50:
        # Bro. Wilson pointed out that the above IF statement is not the cleanest
        # The below IF statement is better 
        if r == 76 and g == 244 and b == 24:
            pixels_cactus[x, y] = pixels_beach[x, y]

# This line displays image in a new window
#image_beach.show()
image_cactus.show()

# This line saves the image
# image_cactus.save("beach_cactus.jpg")