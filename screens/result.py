from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty


class ResultScr(Screen):
    def __init__(self, name='result'):
        super().__init__(name=name)

        self.user = ObjectProperty()

        title_txt = Label(text='Result')
        # self.username_txt = Label(text=f'User: {self.user.username}')
        self.username_txt = Label(text='User: ')
        self.result_txt = Label(text='Right:')
        self.time_txt = Label(text='Total time:')

        next_btn = Button(text='Main menu')
        next_btn.on_press = self.next

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(title_txt)
        main_line.add_widget(self.username_txt)
        main_line.add_widget(self.result_txt)
        main_line.add_widget(self.time_txt)
        main_line.add_widget(next_btn)
        self.add_widget(main_line)

    def on_enter(self):  # Этот метод вызывается при переходе на экран
        username = self.user.username if self.user else 'None'
        right = self.user.right if self.user else '0'
        total = self.user.total if self.user else '0'
        time = round(self.user.end_time - self.user.start_time, 2) if self.user else '0'

        self.username_txt.text = 'User: ' + username
        self.result_txt.text = f'Right: {right}/{total}'
        self.time_txt.text = f'Total time: {time}'

    def next(self):
        next_scr = 'main'
        self.user.check_best()
        self.manager.get_screen(next_scr).user = self.user
        self.manager.transition.direction = 'right'
        self.manager.current = next_scr

