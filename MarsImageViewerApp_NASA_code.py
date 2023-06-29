from requests import get
from random import randint
from kivymd.app import MDApp
from kivy.lang import Builder

class MainApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Lime"
		return Builder.load_file("Design.kv")
		
	def on_start(self):
		self.root.ids.imgData.text = "Rover : Curosity\nSOL(Solar Day On Mars) : 1000\nCamera : Mast Camera\nDate Photo Taken : 2015-05-30"
		
	def changeImg(self):
		sol = randint(0,3000)
		imgLinks = get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=QVLUx9giutj30rwXYX9UmJxS0PMhfsgKk9X5hkri").json()
		
		while(len(imgLinks["photos"]) == 0):
			sol = randint(0,3000)
			imgLinks = get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key=QVLUx9giutj30rwXYX9UmJxS0PMhfsgKk9X5hkri").json()
			
		imgNumber = randint(0,len(imgLinks["photos"])-1)
		imgLink = imgLinks["photos"][imgNumber]["img_src"]
		self.root.ids.img.source = imgLink
		self.root.ids.imgData.text = f"Rover : Curosity\nSOL(Solar Day On Mars) : {sol}\nCamera : {imgLinks['photos'][imgNumber]['camera']['full_name']}\nDate Photo Taken : {imgLinks['photos'][imgNumber]['earth_date']}"

if __name__ == '__main__':
	MainApp().run()