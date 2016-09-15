from kivy.app import App
from kivy.lang import Builder


class convert(App):

    def build(self):
        self.title = "convert m to km"
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root
    def handle_calculate_positive(self, value):
        result = value + 1
        self.root.ids.input_number.text = str(result)
    def handle_calculate_negative(self, value):
        result = value - 1
        self.root.ids.input_number.text = str(result)
    def handle_convert(self,value):
        result = value *1.609344
        self.root.ids.output_label.text = str(result)
convert().run()