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

path_file = 'E:\\ganesh\\python_training_git\\python_training\\algos\\stacks\\nice.png'
path =  'E:\\ganesh\\python_training_git\\python_training\\algos\\stacks\\'   


prob = 0.2

im = Image.open(path_file,'r') # 20170123185233_IMG_9108.JPG  myfile.png
pix_val = list(im.getdata())
print(im.mode)
print(im.getbands())
#print(len(pix_val))
width,height = im.size
#pix_val_flat = [x for sets in pix_val for x in sets]
#f = open(path+'image.txt','w')
#g= open(path+'imagedim.txt','w')

#f.close()
new_image_list_R = []
new_image_list_G = []
new_image_list_B = []

print(im.getpixel((10,11)))

'''
for y in range(height):
    for x in range(width):
        RGB = im.getpixel((x,y))

        print(RGB)

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
'''       
#f.close()
#g.close()

os.chdir(path)
#string_filename = 'image.txt'
#count_lines(string_filename)
#string_filename = 'imagedim.txt'
#count_lines(string_filename)

im2 = Image.new(im.mode,im.size)
#im2.putdata(pix_val)
im2.putdata(new_image_list_R)
#print(tempR)
print(new_image_list_R == pix_val)
os.chdir(path)
#im2.save('parrots_green.png',format='PNG')

#gs_image = im2.convert(mode='L')
#gs_image.save('koala_grayscale.jpg')

'''
Algorithms
The mean and variance parameters for 'gaussian', 'localvar', and 'speckle' noise types are always specified as if the 
image were of class double in the range [0, 1]. If the input image is a different class, the imnoise
 function converts the image to double, adds noise according to the specified type and parameters, clips pixel values to the range 
 [0, 1], and then converts the noisy image back to the same class as the input.

The Poisson distribution depends on the data type of input image I:
If I is double precision, then input pixel values are interpreted as means of Poisson distributions scaled up by 1e12. For example, if an input pixel has the value 5.5e-12, then the corresponding output pixel will be generated from a Poisson distribution with mean of 5.5 and then scaled down by 1e12.
If I is single precision, the scale factor used is 1e6.
If I is uint8 or uint16, then input pixel values are used directly without scaling. For example, 
if a pixel in a uint8 input has the value 10, then the corresponding output pixel will be generated from a Poisson distribution with mean 10.

To add 'salt & pepper' noise with density d to an image, imnoise first assigns each pixel a 
random probability value from a standard uniform distribution on the open interval (0, 1).
For pixels with probability value in the range (0, d/2), the pixel value is set to 0. 
The number of pixels that are set to 0 is approximately d*numel(I)/2.
For pixels with probability value in the range [d/2, d), the pixel value is set to the maximum value of the image data type. The number of pixels that are set to the maximum value is approximately d*numel(I)/2.
For pixels with probability value in the range [d, 1), the pixel value is unchanged.

J = imnoise(I,'gaussian')
J = imnoise(I,'gaussian',m)
J = imnoise(I,'gaussian',m,var_gauss)
J = imnoise(I,'localvar',var_local)
J = imnoise(I,'localvar',intensity_map,var_local)
J = imnoise(I,'poisson')
J = imnoise(I,'salt & pepper')
J = imnoise(I,'salt & pepper',d)
J = imnoise(I,'speckle')
J = imnoise(I,'speckle',var_speckle)
'''
