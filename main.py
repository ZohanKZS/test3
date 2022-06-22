import kivy
from kivy.app import App
from kivy.uix.button import Button
import _ctypes


class My(App):
    def build(self):
        return Button(text='Hello ZZZ 33')


if __name__ == '__main__':
    My().run()