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

class StartMenu(DirectObject.DirectObject):
	def __init__( self, app):
		self.app = app
		
		self.frame = DirectFrame()
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/startMenu.png"
		self.frame['image_scale'] = (1.0, 1.0, 1.0)
		self.frame.setPos(0, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		mapsStart = loader.loadModel('hud/mainMenu/buttons_start_maps.egg')        
		self.startButton = DirectButton(
											parent=self.frame,
											pos=(0,0,0),
											image = (
												mapsStart.find('**/startready'),
												mapsStart.find('**/startclicked'),
												mapsStart.find('**/startrollover'),
												mapsStart.find('**/startdisable')
											),
											command=self.doStartGame,
											scale=0.2,
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.2, 0.2),  
											frameColor=(0.8,0.8,0.8,0)
										)
										#rolloverSound=self.soundManager.over,
										#clickSound=self.soundManager.click))
		
		mapsCredits = loader.loadModel('hud/mainMenu/buttons_credits_maps.egg')
		self.creditsButton = DirectButton(
											parent=self.frame,
											pos=(0,0,-0.1),
											image = (
												mapsCredits.find('**/creditsready'),
												mapsCredits.find('**/creditsclicked'),
												mapsCredits.find('**/creditsrollover'),
												mapsCredits.find('**/creditsdisable')
											),
											#,command=self.showCredits,
											scale=0.2,
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.2, 0.2),  
											frameColor=(0.8,0.8,0.8,0)
										)
										#rolloverSound=self.soundManager.over,
										#clickSound=self.soundManager.click))
		
		
		mapsQuit = loader.loadModel('hud/mainMenu/buttons_quit_maps.egg')
		self.quitButton = DirectButton(
											parent=self.frame,
											pos=(0,0,-0.2),
											image = (
												mapsQuit.find('**/quitready'),
												mapsQuit.find('**/quitclicked'),
												mapsQuit.find('**/quitrollover'),
												mapsQuit.find('**/quitdisable')
											),
											command=self.endGame,
											scale=0.2,
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.2, 0.2),  
											frameColor=(0.8,0.8,0.8,0)
										)
										#rolloverSound=self.soundManager.over,
										#clickSound=self.soundManager.click))
		
		
		self.accept("escape", sys.exit)
		
	def show(self): 
		self.frame.show()        
		
	def hide(self): 
		self.frame.hide()
	
	def doStartGame(self):
		self.hide()
		self.app.setup()
		
	def endGame(self):
		sys.exit()
