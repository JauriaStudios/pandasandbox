# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Start Menu

import sys

from pandac.PandaModules import *

from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage

from pandac.PandaModules import AntialiasAttrib

class Inventory(DirectObject.DirectObject):
	def __init__( self, app ):
		
		self.app = app
		
		self.inventoryShown = False
		
		self.frame = DirectFrame()
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/startMenu.png"
		self.frame['image_scale'] = (1.0, 1.0, 1.0)
		self.frame.setPos(-0.6, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		self.hide()
		
	def toggle(self):
		
		if self.inventoryShown == False:
			self.show()
		else:
			self.hide()
		
	def show(self): 
		self.frame.show()
		self.inventoryShown = True
		
	def hide(self): 
		self.frame.hide()
		self.inventoryShown = False

class Status(DirectObject.DirectObject):
	def __init__( self, app):
		self.app = app
		
		self.frame = DirectFrame()
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/statuspanel.png"
		self.frame['image_scale'] = (0.5, 0.5, 0.7)
		self.frame.setPos(0.6, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		mapsTittle = loader.loadModel('hud/mainMenu/buttons_start_maps.egg')
		self.tittleLabel = DirectLabel(
											parent=self.frame,
											pos=(0,0,0.7),
											image = (
												mapsTittle.find('**/startready'),
											),
											scale=0.2,
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.2, 0.2),  
											frameColor=(0.8,0.8,0.8,0)
										)
		
		mapsClose = loader.loadModel('hud/mainMenu/buttons_close_maps.egg')
		self.closeButton = DirectButton(
											parent=self.frame,
											pos=(0.43,0,0.64),
											image = (
												mapsClose.find('**/closeready'),
												mapsClose.find('**/closeclicked'),
												mapsClose.find('**/closerollover'),
												mapsClose.find('**/closedisable')
											),
											command=self.hide,
											scale=(0.1,0.1,0.21),
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.2, 0.2),  
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.hide()
		
	def toggle(self):
		
		if self.inventoryShown == False:
			self.show()
		else:
			self.hide()
		
	def show(self): 
		self.frame.show()
		self.inventoryShown = True
		
	def hide(self): 
		self.frame.hide()
		self.inventoryShown = False

class Skills(DirectObject.DirectObject):
	def __init__( self, app):
		self.app = app
		
		self.frame = DirectFrame()
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/startMenu.png"
		self.frame['image_scale'] = (1.0, 1.0, 1.0)
		self.frame.setPos(0.6, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		self.hide()
		
	def toggle(self):
		
		if self.inventoryShown == False:
			self.show()
		else:
			self.hide()
		
	def show(self): 
		self.frame.show()
		self.inventoryShown = True
		
	def hide(self): 
		self.frame.hide()
		self.inventoryShown = False
