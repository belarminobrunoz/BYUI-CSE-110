# This line imports or includes the library we will need
from PIL import Image

print("\nWelcome to the image combinator!\n")
chosen_image_object_number = int(input("Type the number corresponding to the object that you want to place in a image: \n1 - Cactus \n2 - Hiker \n3 - Penguin \n4 - Spaceshuttle\n"))

# This line opens the image that we will use as personage and loads it into a variable called "image_object"
if chosen_image_object_number == 1:
    image_object = Image.open("week 07\cse110_images\cactus.jpg")
elif chosen_image_object_number == 2:
    image_object = Image.open("week 07\cse110_images\hiker.jpg")
elif chosen_image_object_number == 3:
    image_object = Image.open("week 07\cse110_images\penguin.jpg")
elif chosen_image_object_number == 4:
    image_object = Image.open("week 07\cse110_images\spaceshuttle.jpg")

print()
chosen_image_background_number = int(input("Type the number corresponding to the background that you want to use: \n1 - Earth \n2 - Desert \n3 - Snowscape \n4 - Sunset\n"))

# This line opens the image that we will use as background and loads it into a variable called "image_background"
if chosen_image_background_number == 1:
    image_background = Image.open("week 07\cse110_images\earth.jpg")
elif chosen_image_background_number == 2:
    image_background = Image.open("week 07\cse110_images\desert.jpg")
elif chosen_image_background_number == 3:
    image_background = Image.open("week 07\cse110_images\snowscape.jpg")
elif chosen_image_background_number == 4:
    image_background = Image.open("week 07\cse110_images\sunset.jpg")



# This line attempts to open a new window to display the image.
image_object.show()

#Here we get the size of the image. This will help us with the loop
width, height = image_object.size

#Here we print the height and the width just to know exactly what is this information



#Here we get the pixels from both images
pixels_from_object = image_object.load()
pixels_from_background = image_background.load()

print("Creating the image....")

# We begin with a vertical loop within the image
for index1 in range(0,width):

    #Then we begin a vertical loop inside the vertical loop within the image
    for index2 in range(0,height):   
    
        # We save the pixels in a variable to compare on the if statement below
        r, g, b = pixels_from_object[index1, index2]

        # I compare many images with diferents grades of green and I found out that most of the types of green have this pattern: 
        # The red usually are lower than 120, The green usually are greater than 190 and the blue are usually lower than 100
        if r < 120 and g > 190 and b < 100:
            # Change the pixel from green to the pixel of the background image
            r, g, b = pixels_from_background[index1, index2]
            pixels_from_object[index1, index2] = (r, g, b)


print("Image created!")
#After do all the necessary changes, we can save the file
image_object.save("new_file.jpg")
image_object.show()
