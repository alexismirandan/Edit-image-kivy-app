# -*- coding: utf-8 -*
from kivy.app import App
from layout.edit_image_layout import EditImageLayout
from kivy.uix.screenmanager import ScreenManager, Screen

__version__ = '0.1'

sm = ScreenManager()
BaseLayaout = Screen

class EditImageScreen(BaseLayaout):
    NAME_SCREEN = 'crop'

    def __init__(self, **kwargs):
        kwargs.update({'name': self.NAME_SCREEN})
        super(EditImageScreen, self).__init__(**kwargs)
        self.layout = None

    def on_pre_enter(self):
        self.layout = EditImageLayout(sm=sm)
        self.add_widget(self.layout)


class EditImageApp(App):

    screns = [EditImageScreen]

    def build(self):
        for class_screen in self.screns:
            sm.add_widget(class_screen())
        return sm

    def on_start(self):
        return True

    def on_pause(self):
        return True

    def on_resume(self):
        return True

    def on_stop(self):
        return True

if __name__ == '__main__':
    EditImageApp().run()
