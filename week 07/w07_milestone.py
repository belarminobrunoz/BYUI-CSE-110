
# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("cse110_images\cat.jpg")
image_beach = Image.open("cse110_images\praia.jpg")

# This line attempts to open a new window to display the image.
# image_original.show()

width, height = image_original.size

print(f"height {height} | width {width}")


pixels_original = image_original.load()
pixels_beach = image_beach.load()

r, g, b = pixels_original[0, 0]
print(f"chroma color: {r} - {g} - {b}")

# cor verde chroma: 76 - 244 - 24

for index1 in range(0,width):
    for index2 in range(0,height):   
        # if index1 % 100 == 0: 
        #     print(f"Loop: {index1} - {index2} <---")

        r, g, b = pixels_original[index1, index2]
        # print(f"{r} - {g} - {b}")

        if r < 120 and g > 210 and b < 60:
            # Mudar o pixel
            r, g, b = pixels_beach[index1, index2]
            pixels_original[index1, index2] = (r, g, b)

#Salvar o arquivo
image_original.save("the_file_goes_here.jpg")
image_original.show()
