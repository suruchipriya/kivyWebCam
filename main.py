from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScreen(Screen):
    def searchImage(self):
        pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


class N:
    pass


class Prince:
    pass


class Review:
    pass


MainApp().run()
