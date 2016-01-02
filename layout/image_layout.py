from kivy.uix.image import Image
from components.image import CoreImage
from kivy.properties import ObjectProperty, StringProperty
import io

class ImageLayout(Image):

    image = ObjectProperty()
    path_image = StringProperty('image.jpg')
    path_image_tmp = StringProperty('image_tmp.jpg')

    def __init__(self, **kwargs):
        super(ImageLayout, self).__init__(**kwargs)

        self.image = CoreImage(self.path_image,
                               data=io.BytesIO(open(self.path_image, "rb").read()),
                               ext=self.path_image[self.path_image.rfind('.') + 1::])
        self.source = self.path_image

    def scale_image(self, width, height, pos_x, pos_y):
        try:
            self.image.scale(self.path_image,
                             self.path_image_tmp,
                             int(width),
                             int(height))

            self.source = self.path_image_tmp
            self.pos = pos_x, pos_y
            self.size = width, height
            self.reload()
        except: pass
