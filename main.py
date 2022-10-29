from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import requests

layout = FloatLayout()
response = requests.get("https://api.nasa.gov/planetary/apod?api_key=API_KEY") #Visit the NASA API website to get an API key
image = AsyncImage(source=str(response.json()["url"]), size_hint=(1, .5), pos_hint={"center_y": .5})
layout.add_widget(image)


label = Label(text=response.json()["title"], size_hint=(1, .4))
layout.add_widget(label)

button = Button(text="Press for more info", size_hint=(1, .1), pos_hint={"center_y": .1})
layout.add_widget(button)

def load_info(instance):
    popup = Popup(title=response.json()["title"] + "\n(Press anywhere outside of popup screen to return to image)", content=WrappedLabel(text=response.json()["explanation"]), size_hint=(1, .8))
    popup.open()
    
button.bind(on_press=load_info)

class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))


class AIODApp(App):
    def build(self):
        return layout 

if __name__ == "__main__":
    AIODApp().run()
