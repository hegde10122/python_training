from PIL import Image
import os
import math
import random

def count_lines(h1):
    num_lines = 0
    with open(h1, 'r') as f:
        for line in f:
                num_lines += 1
    print("Number of lines:")
    print(num_lines)

path_file = 'E:\\ganesh\\python\\parrots.JPG'
path =  'E:\\ganesh\\python\\'   
path1 =  'E:\\ganesh'       

prob = 0.2

im = Image.open(path_file,'r') # 20170123185233_IMG_9108.JPG  myfile.png
pix_val = list(im.getdata())
# print(pix_val)
#print(len(pix_val))
width,height = im.size
#pix_val_flat = [x for sets in pix_val for x in sets]
f = open(path+'image.txt','w')
g= open(path+'imagedim.txt','w')

#f.close()
new_image_list_R = []
new_image_list_G = []
new_image_list_B = []
for y in range(height):
    for x in range(width):
        RGB = im.getpixel((x,y))

        R,G,B = RGB
        G = G * 1.3
        G = math.ceil(G)

        r1 = random.random()

        if G > 255:
                G = 255

        tempR = R,G,B
        tempG = 0,G,0
        tempB = 0,0,B

        new_image_list_R.append(tempR)
        new_image_list_G.append(tempG)
        new_image_list_B.append(tempB)    

        #print(tempR)

        #print(RGB)    

       # f.write(','.join([str(i) for i in RGB]))
       # f.write("\n")
       # g.write(str(x)+","+str(y))
       # g.write("\n")      
f.close()
g.close()

os.chdir(path)
#string_filename = 'image.txt'
#count_lines(string_filename)
#string_filename = 'imagedim.txt'
#count_lines(string_filename)

im2 = Image.new(im.mode,im.size)
#im2.putdata(pix_val)
im2.putdata(new_image_list_R)
print(tempR)
print(new_image_list_R == pix_val)
os.chdir(path)
im2.save('parrots_green.png',format='PNG')

#gs_image = im2.convert(mode='L')
#gs_image.save('koala_grayscale.jpg')

'''

'''
