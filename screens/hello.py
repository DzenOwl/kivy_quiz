from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty

from .user import User



class HelloScr(Screen):
    def __init__(self, name='hello'):
        super().__init__(name=name)

        hello_txt = Label(text='Welcome!')
        username_txt = Label(text='Your login:')
        self.username_input = TextInput(hint_text='John Doe')
        next_btn = Button(text='Proceed')
        next_btn.on_press = self.next

        input_line = BoxLayout()
        input_line.add_widget(username_txt)
        input_line.add_widget(self.username_input)

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(hello_txt)
        main_line.add_widget(input_line)
        main_line.add_widget(next_btn)
        self.add_widget(main_line)

    def next(self):
        next_scr = 'main'
        username = self.username_input.text
        
        if username.strip():  # Check if login is not empty
            user = User(username)
            print('\n', user.username, '\n')
            self.manager.get_screen(next_scr).user = user
            self.manager.transition.direction = 'left'
            self.manager.current = next_scr

