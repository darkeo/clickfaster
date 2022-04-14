import kivy
import random
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import NumericProperty, StringProperty, ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button

Builder.load_file("menu.kv")
# temps de base, arbitraire pour l'instant

class MainWidget(RelativeLayout):
    menu_widget = ObjectProperty()
    pos_x = NumericProperty()
    pos_y = NumericProperty()
    score = NumericProperty()
    hourglass = NumericProperty()
    max_hourglass = NumericProperty()
    menu_title = StringProperty("C  L  I  C  K  F  A  S  T  E  R")
    menu_button_title = StringProperty("START")
    menu_button_title_easy = StringProperty("EASY")
    menu_button_title_medium = StringProperty("MEDIUM")
    menu_button_title_hard = StringProperty("HARD")

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
        self.timer_updated = 100
        self.base_time = 1
        Clock.schedule_interval(self.update, 1.0 / 60)

    def reset_game(self):
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
        self.timer_updated = self.base_time

    def on_menu_button_easy_pressed(self):
        #  print("bouton)
        # self.sound_music1.play()
        self.reset_game()
        self.base_time = 7
        self.timer_updated = self.base_time
        # self.state_game_has_started = True
        self.menu_widget.opacity = 0
        # if self.first_game:
        #     self.sound_begin.play()
        # else:
        #     self.sound_restart.play()

    def on_menu_button_medium_pressed(self):
        #  print("bouton)
        # self.sound_music1.play()
        self.reset_game()
        self.base_time = 5
        self.timer_updated = self.base_time
        # self.state_game_has_started = True
        self.menu_widget.opacity = 0
        # if self.first_game:
        #     self.sound_begin.play()
        # else:
        #     self.sound_restart.play()

    def on_menu_button_hard_pressed(self):
        #  print("bouton)
        # self.sound_music1.play()
        self.reset_game()
        self.base_time = 3
        self.timer_updated = self.base_time
        # self.state_game_has_started = True
        self.menu_widget.opacity = 0
        # if self.first_game:
        #     self.sound_begin.play()
        # else:
        #     self.sound_restart.play()

    def on_button_press(self):
        self.hourglass = 0
        self.score += 1
        self.pos_x = random.randint(0, 85) / 100
        self.pos_y = random.randint(0, 85) / 100
        self.time_to_click = self.timer(self.base_time)
        print("pouet")

    def timer(self, base_time):
        # A IMPLEMENTER : TIMER POUR CLIQUER DE PLUS EN PLUS COURT
        self.time_ticking = 0
        self.one_percent_decrease_threshold = 0
        self.one_percent_decrease = 0
        self.loop = 0
        if self.score == 0:
            return self.timer_updated
        else:
            self.timer_updated -= self.timer_updated / 100
            return self.timer_updated

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
            self.reset_game()
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
