from requests import get
from random import randint
#from webbrowser import open
from kivymd.app import MDApp
from kivy.lang import Builder

KV = ("""
MDScreen:
		
	MDCard:
		size_hint:.95,.9
		pos_hint:{'center_x':.5,'center_y':.54}
		elevation:7
		padding:25
		spacing:25
		orientation:'vertical' 
		
		MDRectangleFlatButton:
			pos_hint:{'center_y':.94,'center_x':.5}
			size_hint:.9,.1
			text:"Mars Images [ from NASA's rover ]"
			bold:True
			font_size: self.height/2
			
		MDFloatingActionButton:
			icon: "satellite-variant"
			md_bg_color: app.theme_cls.primary_color
			pos_hint:{'center_y':.94,'center_x':.91}
			size_hint:.1,.09
			on_release:
				app.changeImg()
		
		AsyncImage:
			id:img
			size_hint:.9,.7
			source:"http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000MR0044631300503690E01_DXXX.jpg"
			
		MDLabel:
			id:imgData
			size_hint_y:.2
			
	MDRectangleFlatButton:
		text:'D   e   v   e   l   o   p   e   d       B   y       O   m   a   n   s   h   u' 
		pos_hint:{'center_x':.5,'center_y':0.035}
		size_hint:.8,.02
		font_size: self.height/2
		bold:True
			
""")

class MainApp(MDApp):
	
	def build(self):
		#Loader.loading_image = ""
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "Lime"
		return Builder.load_string(KV)
		
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

if __name__=='__main__':
	MainApp().run()