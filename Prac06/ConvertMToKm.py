
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Allan Serrurier'

class ConvertMetresToKilometres(App):
    """Convert Metres to Kilometres is a kivy App designed to Convert metres to kilometres"""
    def build(self):
        """build the Kivy file from the kv file"""
        Window.size = (200,100)
        self.title = "Convert miles to Kilometres"
        self.root = Builder.load_file('ConvertMToKm.kv')
        return self.root


ConvertMetresToKilometres().run()