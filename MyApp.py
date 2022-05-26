import kivy
from kivy.app import App
from array import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.image import Image


class MyGrid(Screen):
    pass

class HeroGrid(Screen):
    pass

class Items(Screen):
    pass

class Guides(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class Hero(Screen):
    pass

class Item(Screen):
    pass

class Guide(Screen):
    pass

kv = Builder.load_file('my.kv')



class MyApp(App):
     def build(self):
        # return kv()
        sm = ScreenManager()
        sm.add_widget(MyGrid(name='menu'))
        sm.add_widget(HeroGrid(name='heroes'))
        sm.add_widget(Items(name='items'))
        sm.add_widget(Guides(name='guides'))
        sm.add_widget(Guides(name='hero'))
        sm.add_widget(Guides(name='item'))
        sm.add_widget(Guides(name='guide'))

        return sm

if __name__ == "__main__":
    MyApp().run()
