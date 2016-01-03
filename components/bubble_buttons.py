# -*- coding: utf-8 -*
from kivy.uix.bubble import Bubble
from kivy.properties import NumericProperty, ListProperty, ObjectProperty

class BaseBubbleButtons(Bubble):

    def __init__(self, **kwargs):
        super(BaseBubbleButtons, self).__init__(**kwargs)

    def hide(self, instance=None, value=None):
        self.opacity = 0

    def show(self, instance=None, value=None):
        self.opacity = 1

class BubbleButtons(BaseBubbleButtons):
    resize_button = ObjectProperty()
    cut_button = ObjectProperty()
    rotate_button = ObjectProperty()

class BubbleButtonsUndoConfirm(BaseBubbleButtons):
    undo_button = ObjectProperty()
    confirm_button = ObjectProperty()
