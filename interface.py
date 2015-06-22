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
		self.vigorLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,0),
											text="Vigor",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.magicLabel = DirectLabel(
											parent=self.frame,
											pos=(-0.12,0,-0.07),
											text="Magic",
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
		self.minusVigorButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,0.02),
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
		self.minusMagicButton = DirectButton(
											parent=self.frame,
											pos=(0.2,0,-0.05),
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
		self.plusVigorButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,0.02),
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
		self.plusMagicButton = DirectButton(
											parent=self.frame,
											pos=(0.4,0,-0.05),
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
											text=str(self.app.player.hp),
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
											text=str(self.app.player.mana),
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
											text=str(self.app.player.strength),
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
											text=str(self.app.player.dexterity),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.attrVigorLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,0.02),
											text=str(self.app.player.vigor),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		self.attrMagicLabel = DirectLabel(
											parent=self.frame,
											pos=(0.3,0,-0.05),
											text=str(self.app.player.magic),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Attr Results
		
		
		
		self.scrollFrame = DirectScrolledFrame(
											parent = self.frame,
											canvasSize = (-0.4,0.4,-0.3,0.3),
											frameSize = (-0.486,0.486,-0.193,0.193)
											) 
		self.scrollFrame.setPos(0.0, 0.0, -0.3)
		
		self.scrollNP = self.scrollFrame.getCanvas()
		
		# Total damage
		
		self.damageLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,0.23),
											text="Damage",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrDamageLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,0.25),
											text=str(self.app.player.attackDamage),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total magic damage
		
		self.magicDamageLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,0.16),
											text="Magic Damage",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrMagicDamageLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,0.18),
											text=str(self.app.player.magicDamage),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total speed
		
		self.speedLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,0.09),
											text="Speed",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrSpeedLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,0.11),
											text=str(self.app.player.speed),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total attack speed
		
		self.attackSpeedLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,0.02),
											text="Attack Speed",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrAttackSpeedLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,0.04),
											text=str("%0.2f" % self.app.player.attackSpeed),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total defense
		
		self.defenseLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,-0.05),
											text="Defense",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrDefenseLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,-0.03),
											text=str(self.app.player.defense),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total critical chanse
		
		self.criticalChanceLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,-0.12),
											text="Critical",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrCriticalChanceLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,-0.10),
											text=str(self.app.player.criticalChance),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total critical multiplier
		
		self.criticalMultiplierLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,-0.19),
											text="Critical Multi",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrCriticalMultiplierLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,-0.17),
											text=str(self.app.player.criticalMultiplier),
											text_pos=(0,-0.23),
											text_scale=(0.8,0.8),
											image = (
												mapsAttr.find('**/attr'),
											),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		# Total magical defense
		
		self.magicDefenseLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(-0.3,0,-0.26),
											text="Magic Defense",
											text_align = TextNode.ALeft,
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
		
		self.attrMagicDefenseLabel = DirectLabel(
											parent=self.scrollNP,
											pos=(0.3,0,-0.24),
											text=str(self.app.player.magicDefense),
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
