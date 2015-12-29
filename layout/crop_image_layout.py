# -*- coding: utf-8 -*
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, ObjectProperty
from components.touch_selector import TouchSelector

class CropImageLayout(FloatLayout):
    color_button = ListProperty([1, .3, .4, 1])
    button_color = ListProperty([0, 0, 0, 1])

    rectangle_selector = ObjectProperty()
    image_layout = ObjectProperty()

    def __init__(self, **kwargs):
        self.sm = kwargs.pop('sm', None)
        self.crop_image_screen = kwargs.pop('crop_image_screen', None)
        super(CropImageLayout, self).__init__(**kwargs)
