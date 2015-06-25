#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

#import pdb

import sys, os, time
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import CollideMask

from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode
from panda3d.core import Filename,AmbientLight,DirectionalLight, PointLight, Spotlight
from panda3d.core import PerspectiveLens

from pandac.PandaModules import WindowProperties

from loadbar import Bar
from startmenu import StartMenu
from interface import Inventory, Status, Skills

from utils import Crono, CursorPos, PlayerPos
from player import Player
from enemy import Enemy
from npc import Npc


class World(ShowBase):
	
	def __init__(self):
		ShowBase.__init__(self)
		
		self.menu = StartMenu(self)
		self.bar = Bar()
		
		#self.messenger.toggleVerbose()
		
		
		#sys.exit()
		#pdb.set_trace()
		
		# Window change event handler
		#self.windowEventSetup()
		
		
	def loading(self):
		self.bar.show()
		
	def setup(self):
		
		
		self.bar.show()
		
		print("Init World ...")
		self.bar.incBar(15)
		self.initWorld()
		
		print("Init Actors ...")
		self.bar.incBar(30)
		self.initActors()
		
		print("Init GUI ...")
		self.bar.incBar(45)
		self.initGui()
		
		print("Init Lights ...")
		self.bar.incBar(60)
		self.initLights()
		
		print("Init Collisions ...")
		self.bar.incBar(75)
		self.initCollision()
		
		print("Init Tasks ...")
		self.bar.incBar(95)
		self.initTasks()
		
		print("Launching World")
		self.bar.incBar(100)
		
		self.bar.hide()
		# Accept the control keys
		
		self.accept("h", self.crono.start)
		
	def initActors(self):
		
		self.player = Player(self, 20, 10, 10, 10, 10, 10) #app, hp, mana, strength, dexterity, vigor, magic):
		
		self.enemies = []
		self.npcs = []
		
		self.foe1 = Enemy(self, 100, 50, 5, 2, "bug") #(self, app, hp, mana, speed, attackSpeed, name):
		self.nasgul = Enemy(self, 100, 50, 5, 2, "nasgul")
		
		self.enemies.append(self.foe1)
		self.enemies.append(self.nasgul)
		
		self.npc1 = Npc(self, 100, 50, 5, 2, "guy2")
		self.npc2 = Npc(self, 100, 50, 5, 2, "ralph")
		
		self.npcs.append(self.npc1)
		self.npcs.append(self.npc2)
		
		
	def initGui(self):
		
		# Load the models.
		
		self.inventory = Inventory(self)
		self.status = Status(self)
		self.skills = Skills(self)
		
		self.statusBar = self.loader.loadModel("models/statusbar")
		
		
		self.statusBar.setDepthTest(True)
		self.statusBar.setDepthWrite(True)
		
		
		# Reparent the model to render2d.
		self.statusBar.reparentTo(self.render2d)
		
		
		self.statusBar.setScale(0.15, 0.15, 0.15)
		self.statusBar.setPos(-0.95, 0, 0.65)
		
		
		self.crono = Crono(self)
		self.cursorpos = CursorPos(self)
		self.playerpos = PlayerPos(self)
		
		self.crono.draw(0.7, -0.85)
		self.cursorpos.draw(0.0, -0.85)
		self.playerpos.draw(-0.7, -0.85)
		
		
		self.accept("i", self.inventory.toggle)
		self.accept("c", self.status.toggle)
		self.accept("k", self.skills.toggle)
	
	def initTasks(self):
		
		self.taskMgr.add(self.crono.task, "cronoTask")
		self.taskMgr.add(self.cursorpos.task, "cursorposTask")
		
		#self.taskMgr.add(self.playerpos.task, "playerposTask")
		
		self.taskMgr.add(self.checkCollision, "collisionTask")
		
		self.taskMgr.add(self.player.move, "moveTask")
		self.taskMgr.add(self.player.updateCamera, "playerCameraTask",priority=1)
		
		self.taskMgr.add(self.foe1.update, "bugTask",priority=1)
		self.taskMgr.add(self.nasgul.update, "nasgulTask",priority=1)
		
		self.taskMgr.add(self.npc1.update, "npc1Task",priority=1)
		self.taskMgr.add(self.npc2.update, "npc2Task",priority=1)
		
		self.taskMgr.add(self.inventory.checkPlayerInventory, "playerInventoryTask")
		
		self.taskMgr.add(self.update, 'update')
	
	def initLights(self):
		# Create some lighting
		
		#ambientLight = AmbientLight("ambientLight")
		#ambientLight.setColor(Vec4(0.1, 0.1, 0.1, 1.8))
		
		"""
		directionalLight = DirectionalLight("directionalLight")
		directionalLight.setDirection(Vec3(-10, -10, 5))
		directionalLight.showFrustum()
		directionalLight.setColor(Vec4(1, 1, 1, 1))
		directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
		dirnp = render.attachNewNode(directionalLight)
		dirnp.setPos(10, 0, 6)
		"""
		
		plight1 = PointLight('plight1')
		plight1.setColor(VBase4(1, 1, 1, 1))
		plight1.showFrustum()
		#plight1.setShadowCaster(True)
		plnp1 = render.attachNewNode(plight1)
		plnp1.setPos(26.71, -33.2, 26)
		
		plight2 = PointLight('plight2')
		plight2.setColor(VBase4(0.2, 1.5, 1, 1))
		plight2.showFrustum()
		plnp2 = render.attachNewNode(plight2)
		plnp2.setPos(-25, 25, 25)
		
		slight = Spotlight('slight')
		slight.setColor(VBase4(1, 1, 1, 1))
		lens = PerspectiveLens()
		lens.setFilmSize(1, 1)  # Or whatever is appropriate for your scene
		slight.setLens(lens)
		slight.setShadowCaster(True, 512, 512)
		slight.showFrustum()
		slnp = render.attachNewNode(slight)
		slnp.setPos(0, 0, 25)
		
		slnp.lookAt(Vec3(0,0,0))
		
		render.setLight(slnp)
		render.setLight(plnp1)
		render.setLight(plnp2)
		#render.setLight(render.attachNewNode(ambientLight))

		#render.setLight(dirnp)
		
		render.setShaderAuto()
		
		#render.setLight(render.attachNewNode(directionalLight))
		
		"""
		self.light = render.attachNewNode(Spotlight("Spot"))
		self.light.node().setScene(render)
		self.light.node().setShadowCaster(True)
		self.light.node().showFrustum()
		self.light.node().getLens().setFov(40)
		self.light.node().getLens().setNearFar(10,100)
		render.setLight(self.light)
		"""
		
	def initWorld(self):
		
		self.environ = self.loader.loadModel("models/entradacastillo")
		#self.environ.setScale(20, 20, 20)
		#self.environ.setHpr(0, 0, 0)
		self.environ.setPos(0, 0, 0)
		
		self.playerStartPos = self.environ.find("**/startPos").getPos()
		
		# Reparent the model to render
		
		self.environ.reparentTo(render)
		
	def update(self, task):
		dt = globalClock.getDt()
		
		return task.cont
	
	def setKey(self, key, value):
		self.keyMap[key] = value
		
	def windowEventSetup( self ):
		# accept the window event's
		self.accept( 'window-event', self.windowEventHandler)
		# create a window event yourself
		#messenger.send( 'window-event', [self.win] )
		
	def windowEventHandler( self, window=None ):
		wp = window.getProperties()
		
		print("Window changed")
		print("X = %s" % wp.getXSize())
		print("Y = %s" % wp.getYSize())
		self.setResolution( wp.getXSize(), wp.getYSize() )
		
	def setResolution( self, w, h ):
		wp = WindowProperties()
		wp.setSize( w, h )
		
		if os.name == 'posix':
			self.openMainWindow()
			self.graphicsEngine.openWindows()
		self.win.requestProperties( wp )
		
	# Define a procedure to move the camera.
	def spinCameraTask(self, task):
		angleDegrees = task.time * 6.0
		angleRadians = angleDegrees * (pi / 180.0)
		self.camera.setPos(40 * sin(angleRadians), -10.0 * cos(angleRadians), 3)
		self.camera.setHpr(angleDegrees, 0, 0)
		return Task.cont
		
	def initCollision(self):
		
		# We will detect the height of the terrain by creating a collision
		# ray and casting it downward toward the terrain.  One ray will
		# start above ralph's head, and the other will start above the camera.
		# A ray may hit the terrain, or it may hit a rock or a tree.  If it
		# hits the terrain, we can detect the height.  If it hits anything
		# else, we rule that the move is illegal.
		
		self.cTrav = CollisionTraverser()
		
		self.playerGroundRay = CollisionRay()
		self.playerGroundRay.setOrigin(0, 0, 9)
		self.playerGroundRay.setDirection(0, 0, -1)
		
		self.playerGroundCol = CollisionNode('playerRay')
		self.playerGroundCol.addSolid(self.playerGroundRay)
		self.playerGroundCol.setFromCollideMask(CollideMask.bit(0))
		self.playerGroundCol.setIntoCollideMask(CollideMask.allOff())
		
		self.playerGroundColNp = self.player.playerActor.attachNewNode(self.playerGroundCol)
		
		self.playerGroundHandler = CollisionHandlerQueue()
		
		self.cTrav.addCollider(self.playerGroundColNp, self.playerGroundHandler)
		
		# Uncomment this line to see the collision rays
		#self.playerGroundColNp.show()
		
		
		for enemy in self.enemies:
			
			self.enemyGroundRay = CollisionRay()
			self.enemyGroundRay.setOrigin(0, 0, 9)
			self.enemyGroundRay.setDirection(0, 0, -1)
			
			self.enemyGroundCol = CollisionNode('%sRay' % enemy.name)
			self.enemyGroundCol.addSolid(self.playerGroundRay)
			self.enemyGroundCol.setFromCollideMask(CollideMask.bit(0))
			self.enemyGroundCol.setIntoCollideMask(CollideMask.allOff())
			
			self.enemyGroundColNp = enemy.enemyActor.attachNewNode(self.enemyGroundCol)
			
			self.enemyGroundHandler = CollisionHandlerQueue()
			
			self.cTrav.addCollider(self.enemyGroundColNp, self.enemyGroundHandler)
			
			#self.enemyGroundColNp.show()
		
		
		for npc in self.npcs:
			
			self.npcGroundRay = CollisionRay()
			self.npcGroundRay.setOrigin(0, 0, 9)
			self.npcGroundRay.setDirection(0, 0, -1)
			
			self.npcGroundCol = CollisionNode('%sRay' % npc.name)
			self.npcGroundCol.addSolid(self.playerGroundRay)
			self.npcGroundCol.setFromCollideMask(CollideMask.bit(0))
			self.npcGroundCol.setIntoCollideMask(CollideMask.allOff())
			
			self.npcGroundColNp = npc.npcActor.attachNewNode(self.npcGroundCol)
			
			self.npcGroundHandler = CollisionHandlerQueue()
			
			self.cTrav.addCollider(self.npcGroundColNp, self.npcGroundHandler)
			
			#self.npcGroundColNp.show()
			
		# Uncomment this line to show a visual representation of the
		# collisions occuring
		#self.cTrav.showCollisions(render)
		
	def checkCollision(self, task):
		
		startpos = self.player.playerActor.getPos()
		
		entries = list(self.playerGroundHandler.getEntries())
		entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
		
		for entry in entries:
			if entry > 0: # and entries[0].getIntoNode().getName() == "Ground":
				self.player.playerActor.setZ(entry.getSurfacePoint(render).getZ())
			else:
				self.player.playerActor.setPos(startpos)
		
		for enemy in self.enemies:
			startpos = enemy.enemyActor.getPos()
			
			entries = list(self.enemyGroundHandler.getEntries())
			entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
			
			for entry in entries:
				if entry > 0: # and entries[0].getIntoNode().getName() == "Ground":
					enemy.enemyActor.setZ(entry.getSurfacePoint(render).getZ())
				else:
					enemy.enemyActor.setPos(startpos)
		
		for npc in self.npcs:
			startpos = npc.npcActor.getPos()
			
			entries = list(self.npcGroundHandler.getEntries())
			entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
			
			for entry in entries:
				if entry > 0: # and entries[0].getIntoNode().getName() == "Ground":
					npc.npcActor.setZ(entry.getSurfacePoint(render).getZ())
				else:
					npc.npcActor.setPos(startpos)
		return task.cont

def main():
	props = WindowProperties( )
	
	props.setTitle( 'El Juego Loco' )
	props.setCursorFilename(Filename.binaryFilename("cursor.ico"))
	props.setFullscreen(0)
	props.setSize(1024, 768)
	
	app = World()
	
	app.win.setClearColor((0, 0, 0, 1))
	app.win.requestProperties( props )
	app.setFrameRateMeter(True)
	
	app.run()

if __name__ == "__main__": main()
