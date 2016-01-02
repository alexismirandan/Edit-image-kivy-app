# -*- coding: utf-8 -*
from kivy.uix.bubble import Bubble
from kivy.properties import NumericProperty, ListProperty, ObjectProperty

class BubbleButtons(Bubble):
    resize_button = ObjectProperty()
    cut_button = ObjectProperty()
    rotate_button = ObjectProperty()

    def hide(self, instance=None, value=None):
        self.opacity = 0

    def show(self, instance=None, value=None):
        self.opacity = 1
