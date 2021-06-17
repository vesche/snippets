#!/usr/bin/env python

import requests

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

url = 'http://192.168.1.150:54880/'
buttons = [
    'Power', 'Left', 'Right', 'Down', 'Up', 'Vol Down', 'Vol Up', 'Mute',
    'Ok', 'Back', 'Play', 'Pause', 'Home'
]


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Image(source='baetv.png'))

        for text in buttons:
            self.add_button(text)

    def add_button(self, text):
        self.add_widget(
            Button(
                text=text,
                font_size=80,
                on_press=self.press_button,
                background_color=(0, 0, 0, 0)
            )
        )

    def press_button(self, instance):
        endpoint = '_'.join(instance.text.lower().split())
        requests.get(url + endpoint)


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
