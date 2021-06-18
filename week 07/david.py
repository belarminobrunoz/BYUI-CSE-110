# green screen proyect
from PIL import Image

image_boat = Image.open("week 07\cse110_images\john_travolta.jpg")
image_sunset = Image.open("week 07\cse110_images\sunset.jpg")
image_combined = Image.new("RGB", image_boat.size)
width, height = image_boat.size
print(f"width: {width}")
print(f"height: {height}")
#print(image_boat.size)
#print(image_boat.format)
pixel_boat = image_boat.load()
pixel_sunset = image_sunset.load()
# pixel_image_combined = image_combined.load()
print(pixel_sunset[100, 200])
for y in range (0, height):
    for x in range (0, width):
        r, g, b = pixel_boat[x, y]

        if r < 120 and g > 190 and b < 100:
            
            r, g, b = pixel_sunset[x, y]
            pixel_boat[x, y] = (r, g, b)

            # new_blue = b + 50
            # pixel_sunset[x, y] = (r, g, b)

image_boat.save("boat_sunset.jpg")
image_boat.show()
# image_combined.show()