# -*- coding: utf-8 -*
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty, ObjectProperty
from components.touch_selector import TouchSelector
from components.bubble_buttons import BubbleButtons
from layout.image_layout import ImageLayout
from kivy.uix.button import Button

class EditImageLayout(FloatLayout):
    color_button = ListProperty([1, .3, .4, 1])
    button_color = ListProperty([0, 0, 0, 1])

    rectangle_selector = ObjectProperty()
    image_layout = ObjectProperty()
    bubble_buttons = ObjectProperty()
    bubble_buttons_undo_confirm = ObjectProperty()

    def __init__(self, **kwargs):
        self.sm = kwargs.pop('sm', None)
        self.crop_image_screen = kwargs.pop('crop_image_screen', None)
        super(EditImageLayout, self).__init__(**kwargs)
        self.rectangle_selector.bind(on_change_size=self.on_change_size_rectangle_selector)
        self.bind(on_touch_down=self.bubble_buttons.hide)

        self.bubble_buttons.resize_button.bind(on_press=self.on_press_resize_button)
        self.bubble_buttons_undo_confirm.undo_button.bind(on_press=self.on_press_undo_button)
        self.bubble_buttons_undo_confirm.confirm_button.bind(on_press=self.on_press_confirm_button)

    def on_change_size_rectangle_selector(self, instance):
        if not self.rectangle_selector.tap_not_draw_a_line():
            self.bubble_buttons.show()

    def on_press_resize_button(self, instance):
        width = int(self.rectangle_selector.width_selected)
        height = int(self.rectangle_selector.height_selected)
        self.image_layout.resize_image(width, height)

        self.rectangle_selector.delete_line()

        self.bubble_buttons_undo_confirm.show()

    def on_press_undo_button(self, instance):
        size = self.image_layout.old_size
        self.image_layout.resize_image(width=size[0], height=size[1])
        self.bubble_buttons_undo_confirm.hide()

    def on_press_confirm_button(self, instance):
        self.bubble_buttons_undo_confirm.hide()
