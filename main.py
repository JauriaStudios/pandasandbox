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

from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode
from panda3d.core import Filename,AmbientLight,DirectionalLight, PointLight, Spotlight

from pandac.PandaModules import WindowProperties

from panda3d.bullet import BulletWorld
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletDebugNode

from startmenu import StartMenu

from collision_geom import Entity
from utils import Crono, CursorPos, PlayerPos
from player import Player
from enemy import Enemy


class World(ShowBase):
	
	def __init__(self):
		ShowBase.__init__(self)
		
		self.menu = StartMenu(self)
		
		self.menu.show()
		
		#self.messenger.toggleVerbose()
		
		
		#sys.exit()
		#pdb.set_trace()
		
		# Window change event handler
		#self.windowEventSetup()
		
		
		#self.setup()
		
	def setup(self):
		
		
		self.initGui()
		self.initWorld()
		self.initLights()
		
		self.player = Player(self, 100, 50, 5, 10) #(self, app, hp, mana, speed, dex):
		
		self.foe1 = Enemy(self, 100, 50, 5, 2, "bug") #(self, app, hp, mana, speed, attackSpeed, name):
		self.nasgul = Enemy(self, 100, 50, 5, 2, "nasgul")
		
		self.initTasks()
		
		# Accept the control keys
		self.accept("escape", sys.exit)
		
		self.accept("c", self.crono.start)
		
	def initGui(self):
		
		# Load the models.
		
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
	
	def initTasks(self):
		
		self.taskMgr.add(self.player.move, "moveTask")
		
		self.taskMgr.add(self.crono.task, "cronoTask")
		self.taskMgr.add(self.cursorpos.task, "cursorposTask")
		#self.taskMgr.add(self.playerpos.task, "playerposTask")
		
		self.taskMgr.add(self.player.updateCamera, "playerCameraTask",priority=1)
		
		self.taskMgr.add(self.foe1.update, "bugTask",priority=1)
		self.taskMgr.add(self.nasgul.update, "nasgulTask",priority=1)
		
		self.taskMgr.add(self.update, 'update')
	
	def initLights(self):
		# Create some lighting
		
		ambientLight = AmbientLight("ambientLight")
		ambientLight.setColor(Vec4(0.1, 0.1, 0.1, 1.8))
		
		directionalLight = DirectionalLight("directionalLight")
		directionalLight.setDirection(Vec3(-10, -10, 5))
		directionalLight.showFrustum()
		directionalLight.setColor(Vec4(1, 1, 1, 1))
		directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
		dirnp = render.attachNewNode(directionalLight)
		dirnp.setPos(10, 0, 6)
		
		plight1 = PointLight('plight1')
		plight1.setColor(VBase4(1, 1, 1, 1))
		plight1.showFrustum()
		plight1.setShadowCaster(True)
		plnp1 = render.attachNewNode(plight1)
		plnp1.setPos(26.71, -33.2, 6)
		
		plight2 = PointLight('plight2')
		plight2.setColor(VBase4(0.2, 1.5, 1, 1))
		plight2.showFrustum()
		plight2.setShadowCaster(True)
		plnp2 = render.attachNewNode(plight2)
		plnp2.setPos(-25, 25, 5)
		
		render.setLight(plnp1)
		render.setLight(plnp2)
		render.setLight(render.attachNewNode(ambientLight))

		render.setLight(dirnp)
		
		#self.environ.setShaderAuto()
		
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
		
		self.converter = Entity()
		
		self.worldNP = render.attachNewNode('World')
		
		# World
		self.debugNP = self.worldNP.attachNewNode(BulletDebugNode('Debug'))
		
		self.debugNP.show()
		self.debugNP.node().showWireframe(True)
		self.debugNP.node().showConstraints(False)
		self.debugNP.node().showBoundingBoxes(True)
		self.debugNP.node().showNormals(False)
		
		#self.debugNP.hide()
		
		self.world = BulletWorld()
		self.world.setGravity(Vec3(0, 0, -9.81))
		self.world.setDebugNode(self.debugNP.node())
		
		
		self.environ = self.loader.loadModel("models/piso")
		#self.environ.setScale(20, 20, 20)
		#self.environ.setHpr(0, 0, 0)
		self.environ.setPos(0, 0, 0)
		
		i = 0
		self.testNP = []
		for models in self.converter.calcCollisionShape("mesh", self.environ):
			for shape in models:
				self.testNP.append(self.worldNP.attachNewNode(BulletRigidBodyNode('worldShapes%s' % i)))
				self.testNP[i].node().addShape(shape[0], shape[1])
				i += 1
		
		
		i = 0
		for model in self.environ.findAllMatches('**/+GeomNode'):
			
			self.testNP[i].setScale(model.getScale())
			self.testNP[i].setHpr(model.getHpr())
			self.testNP[i].setPos(model.getPos())
			self.world.attachRigidBody(self.testNP[i].node())
			i += 1
		
		
		# Plane
		"""
		shape = BulletPlaneShape(Vec3(0, 0, -1), 0)
		
		self.np = self.worldNP.attachNewNode(BulletRigidBodyNode('Ground'))
		self.np.node().addShape(shape)
		self.np.setPos(0, 0, -2)
		self.np.setCollideMask(BitMask32.allOn())
		self.world.attachRigidBody(self.np.node())
		"""
		
		# Reparent the model to NodePath.
		self.environ.reparentTo(render)
		
	def update(self, task):
		dt = globalClock.getDt()
		
		self.world.doPhysics(dt, 10, 0.008)
		self.processContacts()
		return task.cont
	
	def processContacts(self):
		if not self.playerShape: 
			return
		
		result = self.world.contactTest(self.playerShape)
		
		#print '-->', result.getNumContacts()
		for contact in result.getContacts():
			cp = contact.getManifoldPoint()
			node0 = contact.getNode0()
			node1 = contact.getNode1()
			#if node1.getName() != "Ground":
				#print node0.getName(), node1.getName(), cp.getLocalPointA()
			
			if self.nasgul:
				if node1.getName() == "nasgul":
					if self.player.checkAttack():
						self.nasgul.attacked(10)
			#print contact.getNode0(), cp.getPositionWorldOnA()
			#print contact.getIdx0(), contact.getIdx1(), \
			#      contact.getPartId0(), contact.getPartId1()
			
			#self.updateNode(node1)
	
	
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
		

def main():
	props = WindowProperties( )
	
	props.setTitle( 'El Juego Loco' )
	props.setCursorFilename(Filename.binaryFilename("cursor.ico"))
	props.setFullscreen(0)
	props.setSize(1024, 768)
	
	app = World()
	
	app.win.requestProperties( props )
	app.setFrameRateMeter(True)
	
	app.run()

if __name__ == "__main__": main()
