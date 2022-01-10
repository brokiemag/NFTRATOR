# NFT-GENERATOR

Python application to generate NFT's using PIL module.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pillow.

```bash
pip install Pillow
```

## Usage

```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Brokiemag](https://Brokiemag.me)
