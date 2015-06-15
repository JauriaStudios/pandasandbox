# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from direct.task import Task

from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletCylinderShape
from panda3d.bullet import BulletCapsuleShape
from panda3d.bullet import BulletCharacterControllerNode
from panda3d.bullet import ZUp

from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode
from panda3d.core import PandaNode,NodePath
from panda3d.core import TransformState
from panda3d.core import OrthographicLens

from direct.actor.Actor import Actor

class Player():
	def __init__(self, app, hp, mana, speed, dex):
		
		self.app = app
		
		self.ori = 0.0
		self.zoomLevel = 5.0
		self.nextAttack = 0.0
		
		height = 2.5
		radius = 0.4
		
		shape = BulletCapsuleShape(radius, height - 2*radius, ZUp)
		
		self.playerNode = BulletCharacterControllerNode(shape, 0.4, 'Player')
		self.playerNP = self.app.worldNP.attachNewNode(self.playerNode)
		self.playerNP.setPos(-2, 0, 14)
		self.playerNP.setH(45)
		self.playerNP.setCollideMask(BitMask32.allOn())

		self.app.world.attachCharacter(self.playerNP.node())

		self.app.playerShape = self.playerNode
		
		self.attacked = False
		self.hp = hp
		self.mana = mana
		self.speed = speed
		self.dex = dex
		
		attackSpeedPerDex = 0.2
		attackSpeed = (attackSpeedPerDex * dex) / 60
		self.attackSpeed = attackSpeed
		
		self.floater = NodePath(PandaNode("floater"))
		self.floater.reparentTo(render)
		
		self.keyMap = {"left":0, "right":0, "forward":0, "backward":0, "cam-left":0, "cam-right":0, "jump":0, "attack":0}
		
		self.playerActor = Actor({"body":"models/dt6"}, {
							"body":{"walk":"models/dt6-walk",
							"slash":"models/dt6-slash"}
						})
		
		self.playerActor.setHpr(0,0,0)
		self.playerActor.setPos(0,0,-1)
		self.playerActor.setScale(0.1)
		
		self.playerActor.reparentTo(self.playerNP)
		
		self.playerHand = self.playerActor.exposeJoint(None, 'body', 'antebrazoder')
		#self.playerHead = self.playerActor.controlJoint(None, 'body', 'cabeza')
		
		#self.playerHead.setScale(10,10,10)
		
		self.models = []                 #A list that will store our models objects
		items = [("models/sword1", (0,5.1,-4), (0,90,0), .6),
				("models/maze", (0,5.1,-4), (0,90,0), .6)]
		
		for row in items:
			np = self.app.loader.loadModel(row[0])				#Load the model
			np.setPos(row[1][0], row[1][1], row[1][2])		#Position it
			np.setHpr(row[2][0], row[2][1], row[2][2])		#Rotate it
			np.setScale(row[3])								#Scale it
			np.reparentTo(self.playerHand)
			self.models.append(np)							#Add it to our models list
		
		
		
		self.item = 0
		self.isMoving = False
		self.isAttacking = False
		
		self.setObject(self.item)							#Make object 0 the first shown
		
		self.app.disableMouse()
		self.app.camera.setPos(self.playerActor.getPos()+45)
		
		self.lens = OrthographicLens()
		self.lens.setFilmSize(45+self.zoomLevel, 45+self.zoomLevel)  # Or whatever is appropriate for your scene

		self.app.cam.node().setLens(self.lens)
		
		self.app.camLens.setFov(120)
		
		
		self.app.accept("a", self.setKey, ["left",1])
		self.app.accept("d", self.setKey, ["right",1])
		self.app.accept("w", self.setKey, ["forward",1])
		self.app.accept("s", self.setKey, ["backward",1])
		
		self.app.accept("x", self.setKey, ["attack",1])
		
		#self.app.accept("q", self.setKey, ["cam-left",1])
		#self.app.accept("e", self.setKey, ["cam-right",1])
		
		self.app.accept("space", self.setKey, ["jump",1])
		
		self.app.accept("a-up", self.setKey, ["left",0])
		self.app.accept("d-up", self.setKey, ["right",0])
		self.app.accept("w-up", self.setKey, ["forward",0])
		self.app.accept("s-up", self.setKey, ["backward",0])
		
		self.app.accept("x-up", self.setKey, ["attack",0])
		
		#self.app.accept("q-up", self.setKey, ["cam-left",0])
		#self.app.accept("e-up", self.setKey, ["cam-right",0])
		
		self.app.accept("space-up", self.setKey, ["jump",0])
		
		
		
		self.app.accept("wheel_up", self.moveCam, [1])
		self.app.accept("wheel_down", self.moveCam, [0])
		
		self.app.accept("i", self.toggleObject)
		
		
	def moveCam(self, zoom):
		
		if zoom == 0:
			self.zoomLevel += 5
			if self.zoomLevel >= 30:
				self.zoomLevel = 30
		
		elif zoom == 1:
			self.zoomLevel -= 5
			if self.zoomLevel <= -30:
				self.zoomLevel = -30
		
		#print self.zoomLevel
		self.lens.setFilmSize(45+self.zoomLevel, 45+self.zoomLevel)  # Or whatever is appropriate for your scene
		self.app.cam.node().setLens(self.lens)
		
	def checkAttack(self):
		return self.attacked
	
	def attack(self):
		
		if self.isAttacking is False:
			self.playerActor.play("slash")
			self.isAttacking = True
		self.isAttacking = False
		
		
		
	def jump(self):
		self.playerNP.node().setMaxJumpHeight(3.0)
		self.playerNP.node().setJumpSpeed(5.0)
		self.playerNP.node().doJump()
		
	def setKey(self, key, value):
		self.keyMap[key] = value
		
		
	def setObject(self, i):
		for np in self.models: np.hide()
		self.models[i].show()
		self.item = i
	
	def toggleObject(self):
		
		if self.item == 1:
			self.item = 0
		else:
			self.item = 1
		
		for np in self.models: np.hide()
		self.models[self.item].show()
		
	def move(self, task):
		#print task.time
		
		# If a move-key is pressed, move in the specified direction.
		
		
		speed = Vec3(0, 0, 0)
		omega = 0.0
		
		
		if (self.keyMap["left"]):
			self.ori = 45
			#omega =  200.0
			speed.setY( -10.0)
		if (self.keyMap["right"]):
			self.ori = -135
			#omega = -200.0
			speed.setY( -10.0)
		if (self.keyMap["forward"]):
			self.ori = -45
			speed.setY( -10.0)
		if (self.keyMap["backward"]):
			self.ori = 135
			speed.setY( -10.0)
			
		
		if (self.keyMap["left"]) and (self.keyMap["forward"]):
			self.ori = 0
			#omega =  200.0
			speed.setY( -10.0)
			
		if (self.keyMap["right"]) and (self.keyMap["forward"]):
			self.ori = -90
			#omega =  200.0
			speed.setY( -10.0)
			
		if (self.keyMap["left"]) and (self.keyMap["backward"]):
			self.ori = 90
			#omega =  200.0
			speed.setY( -10.0)
			
		if (self.keyMap["right"]) and (self.keyMap["backward"]):
			self.ori = 180
			#omega =  200.0
			speed.setY( -10.0)
			
		if (self.keyMap["jump"]):
			self.jump()
		
		if (self.keyMap["attack"])  and (task.time > self.nextAttack):
			self.attack()
			self.nextAttack = task.time + self.attackSpeed
		self.keyMap["attack"] = 0
		
		#self.playerNP.node().setAngularMovement(omega)
		self.playerNP.setH(self.ori)
		self.playerNP.node().setLinearMovement(speed, True)
		
		# If dt6 is moving, loop the run animation.
		# If he is standing still, stop the animation.
		
		if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0) or (self.keyMap["backward"]!=0):
			if self.isMoving is False:
				self.playerActor.loop("walk")
				self.isMoving = True
		else:
			if self.isMoving:
				self.playerActor.stop()
				self.playerActor.pose("walk",1)
				self.isMoving = False
		
		
		return task.cont
		
	def updateCamera(self, task):
		
		self.app.camera.setPos(self.playerNP.getPos()+45)
		# The camera should look in dt6's direction,
		# but it should also try to stay horizontal, so look at
		# a floater which hovers above dt6's head.
		
		self.floater.setPos(self.playerNP.getPos())
		self.floater.setZ(self.playerNP.getZ() + 2.0)
		
		self.app.camera.lookAt(self.floater)
		return task.cont
