# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Inventory Status Skills

import sys

from pandac.PandaModules import *

from direct.showbase import DirectObject
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage

from pandac.PandaModules import AntialiasAttrib

class Inventory(DirectObject.DirectObject):
	def __init__( self, game ):
		
		self.game = game
		self.tooltip = None
		self.inventoryShown = False
		
		self.itemOnHand = None
		
		self.previousItemOnHand = None
		
		self.previousEquipedArmour = None
		self.previousEquipedWeaponr = None
		self.previousEquipedHelmet = None
		self.previousEquipedGloves = None
		self.previousEquipedCloack = None
		self.previousEquipedBoots = None
		self.previousEquipedRingLeft = None
		self.previousEquipedRingRight = None
		self.previousEquipedTrinket = None
		self.previousEquipedShield = None
		
		self.previousItems = [["0" for x in range(10)] for x in range(5)]
		self.inventoryCell = [["0" for x in range(10)] for x in range(5)]
		
		self.frame = DirectFrame()
		self.frame['frameColor']=(0.8, 0.8, 0.8, 0)
		self.frame['image'] = "hud/statuspanel.png"
		self.frame['image_scale'] = (0.5, 0.5, 0.5)
		self.frame.setPos(-0.6, 0, 0)
		
		self.frame.setTransparency(TransparencyAttrib.MAlpha)
		
		mapsInventory = loader.loadModel('hud/interface/buttons_inventory_maps.egg')
		
		# Helmet
		
		self.equipHelmetCell = DirectButton(
																parent=self.frame,
																pos=(-0.40, 0 ,0.45),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["helmets"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Trinket
		
		self.equipTrinketCell = DirectButton(
																parent=self.frame,
																pos=(-0.40, 0 ,0.35),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["trinkets"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Weapon
		
		self.equipWeaponCell = DirectButton(
																parent=self.frame,
																pos=(-0.40, 0 ,0.25),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["weapons"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Ring Left
		
		self.equipRingLeftCell = DirectButton(
																parent=self.frame,
																pos=(-0.40, 0 ,0.15),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["ringLeft"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Gloves
		
		self.equipGlovesCell = DirectButton(
																parent=self.frame,
																pos=(-0.40, 0 ,0.05),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["gloves"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Cloack
		
		self.equipCloackCell = DirectButton(
																parent=self.frame,
																pos=(0.40, 0 ,0.45),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["cloacks"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Shield
		
		self.equipShieldCell = DirectButton(
																parent=self.frame,
																pos=(0.40, 0 ,0.35),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["shields"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Armour
		
		self.equipArmourCell = DirectButton(
																parent=self.frame,
																pos=(0.40, 0 ,0.25),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["armours"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Ring Right
		
		self.equipRingRightCell = DirectButton(
																parent=self.frame,
																pos=(0.40, 0 ,0.15),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["ringRight"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Boots
		
		self.equipBootsCell = DirectButton(
																parent=self.frame,
																pos=(0.40, 0 ,0.05),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.equipCellClick,
																extraArgs=["boots"],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
		
		# Inventory Cells
		
		for row in range(len(self.game.player.inventory)):
			posY = 0.1*row
			for col in range(len(self.game.player.inventory[row])):
				posX = 0.1*col
				self.inventoryCell[row][col] = DirectButton(
																parent=self.frame,
																pos=(-0.45+posX, 0 ,-0.45+posY),
																image = (
																	mapsInventory.find('**/inventory'),
																),
																command=self.cellClick,
																extraArgs=[row,col],
																scale=0.1,
																borderWidth=(0.01,0.01),
																frameSize=(-0.50, 0.50, -0.50, 0.50),  
																frameColor=(0.8,0.8,0.8,0),
																pressEffect=0,
															)
				self.inventoryCell[row][col].bind(DGG.WITHIN, self.mouseOver, [col,row])
				self.inventoryCell[row][col].bind(DGG.WITHOUT, self.mouseOut)
		
		# Temporal Cell
		
		self.toggleCell = DirectButton(
										parent=self.frame,
										pos=(-0.45, 0 ,-0.55),
										image = (
											mapsInventory.find('**/inventory'),
										),
										scale=0.1,
										borderWidth=(0.01,0.01),
										frameSize=(-0.50, 0.50, -0.50, 0.50),  
										frameColor=(0.8,0.8,0.8,0),
										pressEffect=0,
									)
		
		self.hide()
		
	def mouseOver(self, col, row, guiEvent=None ):
		
		if self.tooltip:
			self.tooltip.destroy()
			
		self.drawTooltip(col, row)
		
	def mouseOut(self, arg):
		if self.tooltip:
			self.tooltip.destroy()
		
		
	def drawTooltip(self, col, row):
		
		if self.game.player.inventory[row][col] != "0":
			mpos = self.game.mouseWatcherNode.getMouse()
			x = mpos.getX()
			y = mpos.getY()
			
			self.tooltip = DirectFrame()
			self.tooltip['frameColor']=(0.8, 0.8, 0.8, 0)
			self.tooltip['image'] = "hud/interface/tooltip.png"
			self.tooltip['image_scale'] = (0.3, 0.0, 0.3)
			self.tooltip.setPos(x, 0, y)
			
			self.tooltip.setTransparency(TransparencyAttrib.MAlpha)
			
			self.tooltipNameLabel = DirectLabel(
											parent=self.tooltip,
											pos=(0,0,0.23),
											text=self.game.player.inventory[row][col]["name"],
											text_scale=(0.8,0.8),
											scale=0.065,
											frameColor=(0.8,0.8,0.8,0)
										)
			if "armor" in self.game.player.inventory[row][col]:
				self.tooltipNameLabel = DirectLabel(
												parent=self.tooltip,
												pos=(0,0,0.10),
												text="Armor : %s" % self.game.player.inventory[row][col]["armor"],
												text_scale=(0.8,0.8),
												scale=0.065,
												frameColor=(0.8,0.8,0.8,0)
											)
			
			if ("mindamage" in self.game.player.inventory[row][col]) and ("maxdamage" in self.game.player.inventory[row][col]):
				self.tooltipNameLabel = DirectLabel(
												parent=self.tooltip,
												pos=(0,0,0.10),
												text="Damage : %s - %s" % (self.game.player.inventory[row][col]["mindamage"], self.game.player.inventory[row][col]["maxdamage"]),
												text_scale=(0.8,0.8),
												scale=0.065,
												frameColor=(0.8,0.8,0.8,0)
											)
											
		
	def checkPlayerInventory(self, task):
		
		# Check Inventory
		
		if self.previousItems != self.game.player.inventory:
			for row in range(len(self.game.player.inventory)):
				for col in range(len(self.game.player.inventory[row])):
					self.previousItems[row][col] = self.game.player.inventory[row][col]
					if self.game.player.inventory[row][col] != "0":
						
						self.inventoryCell[row][col]["image"] = "hud/interface/%s.png" % self.game.player.inventory[row][col]["model"]
					elif self.game.player.inventory[row][col] == "0":
						self.inventoryCell[row][col]["image"] = "hud/interface/inventory.png"
						
					self.inventoryCell[row][col]['image_scale'] = (0.5, 0.5, 0.5)
		
		# Check Player Hand
		
		if self.previousItemOnHand != self.itemOnHand:
			self.previousItemOnHand = self.itemOnHand
			if self.itemOnHand != None:
				self.toggleCell["image"] = "hud/interface/%s.png" % self.itemOnHand["model"]
			else:
				self.toggleCell["image"] = "hud/interface/inventory.png"
			
			self.toggleCell['image_scale'] = (0.5, 0.5, 0.5)
		
		# Check Equiped Rings
		
		if self.previousEquipedRingLeft != self.game.player.equip["ringLeft"]:
			self.previousEquipedRingLeft = self.game.player.equip["ringLeft"]
			if self.game.player.equip["ringLeft"] != None:
				self.equipRingLeftCell["image"] = "hud/interface/%s.png" % self.game.player.equip["ringLeft"]["model"]
			else:
				self.equipRingLeftCell["image"] = "hud/interface/inventory.png"
			
			self.equipRingLeftCell['image_scale'] = (0.5, 0.5, 0.5)
			
		if self.previousEquipedRingRight != self.game.player.equip["ringRight"]:
			self.previousEquipedRingRight = self.game.player.equip["ringRight"]
			if self.game.player.equip["ringRight"] != None:
				self.equipRingRightCell["image"] = "hud/interface/%s.png" % self.game.player.equip["ringRight"]["model"]
			else:
				self.equipRingRightCell["image"] = "hud/interface/inventory.png"
			
			self.equipRingRightCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped trinket
		
		if self.previousEquipedTrinket != self.game.player.equip["trinket"]:
			self.previousEquipedTrinket = self.game.player.equip["trinket"]
			if self.game.player.equip["trinket"] != None:
				self.equipTrinketCell["image"] = "hud/interface/%s.png" % self.game.player.equip["trinket"]["model"]
			else:
				self.equipTrinketCell["image"] = "hud/interface/inventory.png"
			
			self.equipTrinketCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped shield
		
		if self.previousEquipedShield != self.game.player.equip["shield"]:
			self.previousEquipedShield = self.game.player.equip["shield"]
			if self.game.player.equip["shield"] != None:
				self.equipShieldCell["image"] = "hud/interface/%s.png" % self.game.player.equip["shield"]["model"]
			else:
				self.equipShieldCell["image"] = "hud/interface/inventory.png"
			
			self.equipShieldCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped Armour
		
		if self.previousEquipedArmour != self.game.player.equip["armour"]:
			self.previousEquipedArmour = self.game.player.equip["armour"]
			if self.game.player.equip["armour"] != None:
				self.equipArmourCell["image"] = "hud/interface/%s.png" % self.game.player.equip["armour"]["model"]
			else:
				self.equipArmourCell["image"] = "hud/interface/inventory.png"
			
			self.equipArmourCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped weapon
		
		if self.previousEquipedWeaponr != self.game.player.equip["weapon"]:
			self.previousEquipedWeaponr = self.game.player.equip["weapon"]
			if self.game.player.equip["weapon"] != None:
				self.equipWeaponCell["image"] = "hud/interface/%s.png" % self.game.player.equip["weapon"]["model"]
			else:
				self.equipWeaponCell["image"] = "hud/interface/inventory.png"
			
			self.equipWeaponCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped helmet
		
		if self.previousEquipedHelmet != self.game.player.equip["helmet"]:
			self.previousEquipedHelmet = self.game.player.equip["helmet"]
			if self.game.player.equip["helmet"] != None:
				self.equipHelmetCell["image"] = "hud/interface/%s.png" % self.game.player.equip["helmet"]["model"]
			else:
				self.equipHelmetCell["image"] = "hud/interface/inventory.png"
			
			self.equipHelmetCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped gloves
		
		if self.previousEquipedGloves != self.game.player.equip["gloves"]:
			self.previousEquipedGloves = self.game.player.equip["gloves"]
			if self.game.player.equip["gloves"] != None:
				self.equipGlovesCell["image"] = "hud/interface/%s.png" % self.game.player.equip["gloves"]["model"]
			else:
				self.equipGlovesCell["image"] = "hud/interface/inventory.png"
			
			self.equipGlovesCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped cloack
		
		if self.previousEquipedCloack != self.game.player.equip["cloack"]:
			self.previousEquipedCloack = self.game.player.equip["cloack"]
			if self.game.player.equip["cloack"] != None:
				self.equipCloackCell["image"] = "hud/interface/%s.png" % self.game.player.equip["cloack"]["model"]
			else:
				self.equipCloackCell["image"] = "hud/interface/inventory.png"
			
			self.equipCloackCell['image_scale'] = (0.5, 0.5, 0.5)
			
		# Check Equiped boots
		
		if self.previousEquipedBoots != self.game.player.equip["boots"]:
			self.previousEquipedBoots = self.game.player.equip["boots"]
			if self.game.player.equip["boots"] != None:
				self.equipBootsCell["image"] = "hud/interface/%s.png" % self.game.player.equip["boots"]["model"]
			else:
				self.equipBootsCell["image"] = "hud/interface/inventory.png"
			
			self.equipBootsCell['image_scale'] = (0.5, 0.5, 0.5)
			
		return task.cont
		
	def equipCellClick(self, equipPart):
		print(equipPart)
		
		# Rings
		
		if equipPart == "ringLeft":
			if (self.itemOnHand != None) and (self.game.player.equip["ringLeft"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["rings"]):
					self.game.player.equip["ringLeft"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["ringLeft"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["rings"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["ringLeft"] 
					self.game.player.equip["ringLeft"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["ringLeft"] != None):
					self.itemOnHand = self.game.player.equip["ringLeft"] 
					self.game.player.equip["ringLeft"]  = None
			
		if equipPart == "ringRight":
			if (self.itemOnHand != None) and (self.game.player.equip["ringRight"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["rings"]):
					self.game.player.equip["ringRight"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["ringRight"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["rings"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["ringRight"] 
					self.game.player.equip["ringRight"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["ringRight"] != None):
					self.itemOnHand = self.game.player.equip["ringRight"] 
					self.game.player.equip["ringRight"]  = None
			
		# Trinkets
		
		if equipPart == "trinkets":
			if (self.itemOnHand != None) and (self.game.player.equip["trinket"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["trinkets"]):
					self.game.player.equip["trinket"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["trinket"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["accesories"]["trinkets"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["trinket"] 
					self.game.player.equip["trinket"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["trinket"] != None):
					self.itemOnHand = self.game.player.equip["trinket"] 
					self.game.player.equip["trinket"]  = None
			
		# Shields
		
		if equipPart == "shields":
			if (self.itemOnHand != None) and (self.game.player.equip["shield"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["shields"]):
					self.game.player.equip["shield"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["shield"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["shields"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["shield"] 
					self.game.player.equip["shield"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["shield"] != None):
					self.itemOnHand = self.game.player.equip["shield"] 
					self.game.player.equip["shield"]  = None
			
		# Armours
		
		if equipPart == "armours":
			if (self.itemOnHand != None) and (self.game.player.equip["armour"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["lightarmours"]) or (self.itemOnHand["model"] in self.game.items["items"]["armours"]["midarmours"]) or (self.itemOnHand["model"] in self.game.items["items"]["armours"]["heavyarmours"]) :
					self.game.player.equip["armour"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["armour"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["lightarmours"]) or (self.itemOnHand["model"] in self.game.items["items"]["armours"]["midarmours"]) or (self.itemOnHand["model"] in self.game.items["items"]["armours"]["heavyarmours"]) :
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["armour"] 
					self.game.player.equip["armour"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["armour"] != None):
					self.itemOnHand = self.game.player.equip["armour"] 
					self.game.player.equip["armour"]  = None
		
		# Weapons
		
		if equipPart == "weapons":
			if (self.itemOnHand != None) and (self.game.player.equip["weapon"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["swords"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["axes"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["spears"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["fists"]) :
					self.game.player.equip["weapon"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["weapon"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["swords"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["axes"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["spears"]) or (self.itemOnHand["model"] in self.game.items["items"]["weapons"]["fists"]) :
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["weapon"] 
					self.game.player.equip["weapon"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["weapon"] != None):
					self.itemOnHand = self.game.player.equip["weapon"] 
					self.game.player.equip["weapon"]  = None
		
		# Helmets
		
		if equipPart == "helmets":
			if (self.itemOnHand != None) and (self.game.player.equip["helmet"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["helmets"]): 
					self.game.player.equip["helmet"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["helmet"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["helmets"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["helmet"] 
					self.game.player.equip["helmet"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["helmet"] != None):
					self.itemOnHand = self.game.player.equip["helmet"] 
					self.game.player.equip["helmet"]  = None
		
		# Gloves
		
		if equipPart == "gloves":
			if (self.itemOnHand != None) and (self.game.player.equip["gloves"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["gloves"]): 
					self.game.player.equip["gloves"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["gloves"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["gloves"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["gloves"] 
					self.game.player.equip["gloves"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["gloves"] != None):
					self.itemOnHand = self.game.player.equip["gloves"] 
					self.game.player.equip["gloves"]  = None
		
		# Cloack
		
		if equipPart == "cloacks":
			if (self.itemOnHand != None) and (self.game.player.equip["cloack"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["cloacks"]): 
					self.game.player.equip["cloack"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["cloack"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["cloacks"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["cloack"] 
					self.game.player.equip["cloack"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["cloack"] != None):
					self.itemOnHand = self.game.player.equip["cloack"] 
					self.game.player.equip["cloack"]  = None
		
		# Boots
		
		if equipPart == "boots":
			if (self.itemOnHand != None) and (self.game.player.equip["boots"] == None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["boots"]): 
					self.game.player.equip["boots"] = self.itemOnHand
					self.itemOnHand = None
			
			elif (self.itemOnHand != None) and (self.game.player.equip["boots"] != None):
				if (self.itemOnHand["model"] in self.game.items["items"]["armours"]["boots"]):
					toggleItem = self.itemOnHand
					self.itemOnHand = self.game.player.equip["boots"] 
					self.game.player.equip["boots"]  = toggleItem
			
			elif (self.itemOnHand == None) and (self.game.player.equip["boots"] != None):
					self.itemOnHand = self.game.player.equip["boots"] 
					self.game.player.equip["boots"]  = None
		
	def cellClick(self, row, col):
		
		if self.game.player.inventory[row][col] != "0" and self.itemOnHand == None:
			
			self.itemOnHand = self.game.player.inventory[row][col]
			self.game.player.inventory[row][col] = "0"
			
			if self.tooltip:
				self.tooltip.destroy()
				
		elif self.game.player.inventory[row][col] == "0" and self.itemOnHand != None:
			
			self.game.player.inventory[row][col] = self.itemOnHand
			self.itemOnHand = None
			
			
		elif self.game.player.inventory[row][col] != "0" and self.itemOnHand != None:
			
			toogleItem = self.itemOnHand
			self.itemOnHand = self.game.player.inventory[row][col]
			self.game.player.inventory[row][col] = toogleItem 
			
			
	def toggle(self):
		
		if self.inventoryShown == False:
			self.show()
			self.game.taskMgr.add(self.checkPlayerInventory, "playerInventoryTask")
			
		else:
			self.hide()
			self.game.taskMgr.remove("playerInventoryTask")
		
	def show(self): 
		self.frame.show()
		self.inventoryShown = True
		
	def hide(self): 
		self.frame.hide()
		self.inventoryShown = False

class Status(DirectObject.DirectObject):
	def __init__( self, game):
		self.game = game
		
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
											text=str(self.game.player.hp),
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
											text=str(self.game.player.mana),
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
											text=str(self.game.player.strength),
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
											text=str(self.game.player.dexterity),
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
											text=str(self.game.player.vigor),
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
											text=str(self.game.player.magic),
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
											text=str(self.game.player.attackDamage),
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
											text=str(self.game.player.magicDamage),
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
											text=str(self.game.player.speed),
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
											text=str("%0.2f" % self.game.player.attackSpeed),
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
											text=str(self.game.player.defense),
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
											text=str(self.game.player.criticalChance),
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
											text=str(self.game.player.criticalMultiplier),
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
											text=str(self.game.player.magicDefense),
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
	def __init__( self, game):
		self.game = game
		
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
