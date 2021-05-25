from PIL import Image, ImageFilter
import sys
import os

#taking arguments from command line
image_folder = sys.argv[1]
image_file = sys.argv[2]
#print(f'{image_folder}{image_file}')

#checking if the folder exists or not
if (not os.path.exists(image_file)):
    os.makedirs(image_file)

#looping through the pokedesk for each file
i = 1
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    name = os.path.splitext(filename)
    img.save(f'{image_file}{name[0]}.png')
    i+=1
    print('done!')
   
