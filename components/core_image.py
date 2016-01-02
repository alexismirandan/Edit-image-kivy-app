# -*- coding: utf-8 -*
import io
from kivy.core.image import Image as CoreImageKivy
from PIL import Image

class CoreImage(CoreImageKivy):

    def __init__(self, arg, **kwargs):
        super(CoreImage, self).__init__(arg, **kwargs)

    def resize(self, fname, fname_scaled, width, height):
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
