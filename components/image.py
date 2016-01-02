# -*- coding: utf-8 -*
import io
from kivy.core.image import Image as CoreImage
from PIL import Image

def scale(fname, fname_scaled, width, height):
    """
    reduces the size of an image.
    """
    try:
        img = Image.open(fname)
    except Exception as e:
        print('Exception: ', e)
        return

    img = img.resize((width, height), Image.ANTIALIAS)
    try:
        img.save(fname_scaled)
    except Exception as e:
        print('Exception: ', e)
        return

path_image = 'image.jpg'
data = io.BytesIO(open(path_image, "rb").read())
im = CoreImage(data, ext="jpg", filename="image.jpg")
filename = im.image.filename
filename_tmp = 'image_tmp.jpg'
