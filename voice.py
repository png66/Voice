import pyttsx3
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
engine = pyttsx3.init()

ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', ru_voice_id)
red = [1, 0, 0, 1]
purple = [1, 0, 1, 1]
blue = [0, 0, 1, 1]

class PersonalScr(Screen):
	def __init__(self, name = 'Personal'):
		super().__init__(name=name)
		vl = BoxLayout(orientation = 'vertical')
		self.txt = TextInput()
		btn = Button(text = 'Озвучить', background_color = red)
		btn.on_press = self.Voice
		vl.add_widget(self.txt)
		vl.add_widget(btn)
		cr = Button(text="Переключиться на другой экран", background_color = purple)
		cr.on_press = self.ToBase
		vl.add_widget(cr)
		self.add_widget(vl)
	def Voice(self):
		global engine
		t = self.txt.text
		engine.say(t)
		engine.runAndWait()
	def ToBase(self):
		self.manager.transition.direction = 'left'
		self.manager.current = 'Base'


class BaseScr(Screen):
	def __init__(self, name = 'Base'):
		super().__init__(name=name)
		vl = BoxLayout(orientation = 'vertical')
		
		btnWC = Button(text = 'Хочу в туалет', background_color = blue)
		btnWC.on_press = lambda : self.Say('Хочу в туалет')
		vl.add_widget(btnWC)
		btnDrink = Button(text = 'Хочу Пить', background_color = blue)
		btnDrink.on_press = lambda : self.Say('Хочу Пить')
		vl.add_widget(btnDrink)
		btnEat = Button(text = 'Хочу Кушать', background_color = blue)
		btnEat.on_press = lambda : self.Say('Хочу Кушать')
		vl.add_widget(btnEat)
		cr = Button(text="Переключиться на другой экран", background_color = purple)
		cr.on_press = self.ToPersonal
		vl.add_widget(cr)
		self.add_widget(vl)
	def Say(self, text):
		global engine
		engine.say(text)
		engine.runAndWait()
	def ToPersonal(self):
		self.manager.transition.direction = 'right'
		self.manager.current = 'Personal'


class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(PersonalScr())
		sm.add_widget(BaseScr())
		return sm

app = MyApp()
app.run()
