import kivy
import random
from kivy.app import App
from kivy.properties import NumericProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class MainWidget(BoxLayout):
    pos_x = NumericProperty()
    pos_y = NumericProperty()
    score = NumericProperty()
    hourglass = NumericProperty()
    max_hourglass = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos_x = 0.45
        self.pos_y = 0.45
        self.score = 0
        self.time_to_click = 100000
        self.time_ticking = 0
        self.hourglass = 0
        self.max_hourglass = 100
        self.loop = 0
        self.time_left = 0
        self.one_percent_decrease_threshold = 0
        self.one_percent_decrease = 0
        Clock.schedule_interval(self.update, 1.0 / 60)

    def on_button_press(self):
        self.hourglass = 0
        self.score += 1
        self.pos_x = random.randint(0, 100) / 100
        self.pos_y = random.randint(0, 100) / 100
        self.time_to_click = self.timer()
        print("pouet")

    def timer(self):
        # A IMPLEMENTER : TIMER POUR CLIQUER DE PLUS EN PLUS COURT
        self.time_ticking = 0
        self.one_percent_decrease_threshold = 0
        self.one_percent_decrease = 0
        self.loop = 0
        return 5

    def update(self, dt):
        time_factor = dt * 60
        self.time_ticking += dt
        self.time_left = self.time_to_click - self.time_ticking
        self.one_percent_decrease_threshold = self.time_to_click / 100
        self.one_percent_decrease = self.time_ticking - self.one_percent_decrease_threshold * self.loop
        if self.one_percent_decrease >= self.one_percent_decrease_threshold:
            self.hourglass += 1
            one_percent_decrease = 0
            self.loop += 1

        if self.time_left <= 0:
            print("game over")
            self.pos_x = 0.45
            self.pos_y = 0.45
            self.score = 0
            self.time_to_click = 100000
            self.time_ticking = 0
            self.hourglass = 0
            self.max_hourglass = 100
            self.loop = 0
            self.time_left = 0
            self.one_percent_decrease_threshold = 0
            self.one_percent_decrease = 0
            # game over


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
