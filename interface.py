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
		self.frame['image'] = "hud/statuspanel.png"
		self.frame['image_scale'] = (0.5, 0.5, 0.5)
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
		
		# Main frame
		
		self.frame = DirectFrame(parent = aspect2d)
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/statuspanel.png"
		self.frame['image_scale'] = (0.5, 0.5, 0.5)
		self.frame.setPos(0.6, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		# Tittle Label
		
		self.tittleLabel = DirectLabel(
											parent=self.frame,
											pos=(0,0,0.44),
											text="Status",
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		mapsClose = loader.loadModel('hud/interface/buttons_close_maps.egg')
		
		# Close button
		
		self.closeButton = DirectButton(
											parent=self.frame,
											pos=(0.44,0,0.64),
											image = (
												mapsClose.find('**/close'),
											),
											command=self.hide,
											scale=0.1,
											borderWidth=(0.01,0.01),
											frameSize=(-0.55, 0.55, -0.55, 0.55),  
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Name label
		
		self.nameLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.35,0,0.34),
											text="Hero",
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Portrait 
		
		self.portraitFrame = DirectFrame(parent=self.frame)
		self.portraitFrame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.portraitFrame['image'] = "hud/interface/portrait.png"
		self.portraitFrame['image_scale'] = (0.1, 0.1, 0.1)
		self.portraitFrame.setPos(-0.35, 0, 0.22)
		
		# Stats labels
		
		self.hpLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,0.28),
											text="Life",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.manaLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,0.21),
											text="Mana",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.strLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,0.14),
											text="Strenght",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.dexLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,0.07),
											text="Dexterity",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Arrow left buttons
		
		mapsArrows = loader.loadModel('hud/interface/buttons_arrows_maps.egg')
		
		self.minusHpButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,0.30),
											image = (
												mapsArrows.find('**/arrowleft'),
												mapsArrows.find('**/arrowleftclick'),
												mapsArrows.find('**/arrowleftover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01), 
											frameColor=(0.8,0.8,0.8,0)
										)
		self.minusManaButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,0.23),
											image = (
												mapsArrows.find('**/arrowleft'),
												mapsArrows.find('**/arrowleftclick'),
												mapsArrows.find('**/arrowleftover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01),  
											frameColor=(0.8,0.8,0.8,0)
										)
		self.minusStrButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,0.16),
											image = (
												mapsArrows.find('**/arrowleft'),
												mapsArrows.find('**/arrowleftclick'),
												mapsArrows.find('**/arrowleftover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01),
											frameColor=(0.8,0.8,0.8,0)
										)
		self.minusDexButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,0.09),
											image = (
												mapsArrows.find('**/arrowleft'),
												mapsArrows.find('**/arrowleftclick'),
												mapsArrows.find('**/arrowleftover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01),
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Arrow right buttons
		
		self.plusHpButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,0.30),
											image = (
												mapsArrows.find('**/arrowright'),
												mapsArrows.find('**/arrowrightclick'),
												mapsArrows.find('**/arrowrightover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01), 
											frameColor=(0.8,0.8,0.8,0)
										)
		self.plusManaButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,0.23),
											image = (
												mapsArrows.find('**/arrowright'),
												mapsArrows.find('**/arrowrightclick'),
												mapsArrows.find('**/arrowrightover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01), 
											frameColor=(0.8,0.8,0.8,0)
										)
		self.plusStrButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,0.16),
											image = (
												mapsArrows.find('**/arrowright'),
												mapsArrows.find('**/arrowrightclick'),
												mapsArrows.find('**/arrowrightover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01), 
											frameColor=(0.8,0.8,0.8,0)
										)
		self.plusDexButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,0.09),
											image = (
												mapsArrows.find('**/arrowright'),
												mapsArrows.find('**/arrowrightclick'),
												mapsArrows.find('**/arrowrightover'),
											),
											#command=self.hide,
                                            image_scale=0.5,
											scale=0.1,
											borderWidth=(0.01,0.01), 
											frameColor=(0.8,0.8,0.8,0)
										)
		# Atribute stat labels
		
		mapsAttr = loader.loadModel('hud/interface/labels_attr_maps.egg')
		
		self.attrHpLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,0.30),
											text="20",
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.attrManaLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,0.23),
											text="10",
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.attrStrLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,0.16),
											text="25",
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.attrDexLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,0.09),
											text="15",
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
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
		self.frame['image_scale'] = (0.5, 0.5, 0.5)
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
