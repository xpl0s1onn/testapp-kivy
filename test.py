from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=16, spacing=12)
        self.input = TextInput(hint_text="Введите текст", size_hint_y=None, height=48)
        btn = Button(text="Показать", size_hint_y=None, height=48)
        btn.bind(on_press=self.show_text)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        layout.add_widget(Label(text="Нижняя панель", size_hint_y=None, height=30))
        self.add_widget(layout)

    def show_text(self, instance):
        self.manager.current = "result"
        self.manager.get_screen("result").set_text(self.input.text)

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=16, spacing=12)
        self.lbl = Label(text="", halign="center")
        btn_back = Button(text="Назад", size_hint_y=None, height=48)
        btn_back.bind(on_press=lambda *_: setattr(self.manager, "current", "home"))
        layout.add_widget(self.lbl)
        layout.add_widget(btn_back)
        self.add_widget(layout)

    def set_text(self, txt):
        self.lbl.text = f"Вы ввели: {txt}"

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ResultScreen(name="result"))
        return sm

if __name__ == "__main__":
    TestApp().run()
