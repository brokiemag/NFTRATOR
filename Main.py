#import the necessary module
from PIL import Image  

#grab image source

img1 = Image.open(#path of image ex hat)
img2 = Image.open(#path of image ex face)

#combines the images
 
intermediate = Image.alpha_composite(imgl, img2) 
img3 = Image.open(#path of image ex mask) 
final = Image.alpha_composite(intermediate, img3) 

#save the final png (image)

final.save('final.png')