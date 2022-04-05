import kivy
import random
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainWidget(FloatLayout):
    pos_x = NumericProperty()
    pos_y = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = random.randint(0, 100) / 100
        self.pos_y = random.randint(0, 100) / 100

    def on_button_press(self):
        print("pouet")
        self.pos_x = random.randint(0, 100) / 100
        self.pos_y = random.randint(0, 100) / 100


class ClickMeButton(Button):
    pass
    #
    # def on_press(self):
    #     print("pouet")
    #     MainWidget.pos_x = random.randint(0, 1265)
    #     MainWidget.pos_y = random.randint(0, 605)


class ClickFaster(App):
    def build(self):
        return MainWidget()


ClickFaster().run()
