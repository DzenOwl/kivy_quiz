from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.properties import ObjectProperty, StringProperty

from random import shuffle

from .const import *


class TestScr(Screen):
    def __init__(self, name='test'):
        super().__init__(name=name)

        self.user = ObjectProperty()
        self.answer = StringProperty()

        self.timer_txt = Label(text='0 s')
        self.counter_txt = Label(text='0 / ?')

        self.question_txt = Label(text='Question')
        # self.username_txt = Label(text=f'User: {self.user.username}')
        ans_1_btn = Button(text='1')
        ans_2_btn = Button(text='2')
        ans_3_btn = Button(text='3')
        ans_4_btn = Button(text='4')
        self.answers = [ans_1_btn, ans_2_btn, ans_3_btn, ans_4_btn]
        for btn in self.answers:
            btn.bind(on_press=self.callback)

        next_btn = Button(text='Next question')
        next_btn.on_press = self.next

        stats_line = BoxLayout()
        stats_line.add_widget(self.timer_txt)
        stats_line.add_widget(self.counter_txt)

        h_line_1 = BoxLayout()
        h_line_1.add_widget(ans_1_btn)
        h_line_1.add_widget(ans_2_btn)
        h_line_2 = BoxLayout()
        h_line_2.add_widget(ans_3_btn)
        h_line_2.add_widget(ans_4_btn)

        main_line = BoxLayout(orientation='vertical')
        main_line.add_widget(stats_line)
        main_line.add_widget(self.question_txt)
        main_line.add_widget(h_line_1)
        main_line.add_widget(h_line_2)
        main_line.add_widget(next_btn)
        self.add_widget(main_line)
    
    def set_question(self):
        self.question_txt.text = self.user.qs[self.user.current][TEXT]
        shuffle(self.answers)
        self.answers[0].text = self.user.qs[self.user.current][RIGHT]
        self.answers[1].text = self.user.qs[self.user.current][WRONG][0]
        self.answers[2].text = self.user.qs[self.user.current][WRONG][1]
        self.answers[3].text = self.user.qs[self.user.current][WRONG][2]

    def on_enter(self):
        if self.user:
            self.set_question()
    
    def callback(self, instance):
        for btn in self.answers:
            btn.background_color = BTN_DEFAULT
        self.answer = instance.text
        print('The button <%s> is being pressed' % instance.text)
        instance.background_color = GREEN
    
    def check_answer(self):
        if self.answer == self.answers[0].text:
            self.user.right += 1

    def next(self):
        next_scr = 'test'
        self.check_answer()
        self.user.next_question()
        for btn in self.answers:
            btn.background_color = BTN_DEFAULT
        if self.user.current == -1:
            next_scr = 'result'
            self.manager.get_screen(next_scr).user = self.user
            self.manager.transition.direction = 'left'
            self.manager.current = next_scr
        else:
            self.set_question()

