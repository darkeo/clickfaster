import kivy
import random
from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainWidget(BoxLayout):
    pos_x = NumericProperty()
    pos_y = NumericProperty()
    score = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = 0.45
        self.pos_y = 0.45
        self.score = 0

    def on_button_press(self):
        print("pouet")
        self.score += 1
        self.pos_x = random.randint(0, 100) / 100
        self.pos_y = random.randint(0, 100) / 100


class ClickMeButton(Button):
    pass
    #
    # def on_press(self):
    #     print("pouet")
    #     MainWidget.pos_x = random.randint(0, 1265)
    #     MainWidget.pos_y = random.randint(0, 605)

class ScoreLabel(Label):
    pass

class ClickFaster(App):
    def build(self):
        return MainWidget()


ClickFaster().run()
