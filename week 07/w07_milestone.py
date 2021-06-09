
# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("C:\Users\bruno\Documents\GitHub\BYUI-CSE-110\week 07\cse110_images\beach.jpg")

# This line attempts to open a new window to display the image.
image_original.show()