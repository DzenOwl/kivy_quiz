from kivy.uix.button import Button


# бесполезный компонент
class ToScreenButton(Button):
    def __init__(self, screen, to_screen='main', direction='right', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.to_screen = to_screen

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.to_screen