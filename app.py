from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.hello import HelloScr
from screens.main import MainScr
from screens.test import TestScr
from screens.result import ResultScr


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelloScr())
        sm.add_widget(MainScr())
        sm.add_widget(TestScr())
        sm.add_widget(ResultScr())
        return sm
    
if __name__ == '__main__':
    app = MyApp()
    app.run()