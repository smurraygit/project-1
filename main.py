from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Interface(FloatLayout):
    def display_information(self):
        data = self.ids.text_input.text  # Accessing the TextInput using its ID
        self.ids.label.text = data  # Accessing the Label using its ID


class ProjectApp(App):
    pass


ProjectApp().run()
