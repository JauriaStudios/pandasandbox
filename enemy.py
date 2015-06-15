# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from direct.task import Task

from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode

from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletCylinderShape
from panda3d.bullet import BulletCapsuleShape
from panda3d.bullet import BulletCharacterControllerNode
from panda3d.bullet import ZUp

from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence

from panda3d.ai import *

class Enemy():
	def __init__(self, app, hp, mana, speed, attackSpeed, name):
		
		
		self.app = app
		
		self.name = name
		height = 1
		radius = 1
		
		shape = BulletCapsuleShape(radius, height - 2*radius, ZUp)
		
		self.enemyNode = BulletCharacterControllerNode(shape, 0.4, self.name)
		self.enemyNP = self.app.worldNP.attachNewNode(self.enemyNode)
		self.enemyNP.setPos(-2, 0, 0.22)
		self.enemyNP.setH(45)
		self.enemyNP.setCollideMask(BitMask32.allOn())

		self.app.world.attachCharacter(self.enemyNP.node())

		self.app.enemyShape = self.enemyNode
		
		self.model = "models/%s" % self.name
		self.modelWalk = "models/%s-walk" % self.name
		self.hp = hp
		self.mana = mana
		self.speed = speed
		self.attackSpeed = attackSpeed
		
		self.enemyActor = Actor({	"body":self.model,},
							{"body":{"walk":self.modelWalk},
						})
		self.enemyActor.setHpr(0,0,0)
		self.enemyActor.setPos(0,0,-0.5)
		self.enemyActor.setScale(0.5)
		self.enemyActor.reparentTo(self.enemyNP)
		
		self.setupAI()
		
	def getName(self):
		return self.name
		
	def attacked(self, damage):
		print("man pegao")
		self.hp -= damage
		if self.hp <= 0:
			self.enemyNP.removeNode()
		
	def setupAI(self):
		
		
		self.enemyActor.loop("walk")
		
		#Creating AI World
		
		self.AIworld = AIWorld(render)

		self.AIchar = AICharacter("enemy",self.enemyNP, 60, 0.05, 5)
		self.AIworld.addAiChar(self.AIchar)
		self.AIbehaviors = self.AIchar.getAiBehaviors()

		self.AIbehaviors.wander(10, 0, 15, 1.0)
		
		#Path follow (note the order is reveresed)
		"""self.AIbehaviors.pathFollow(1)
		self.AIbehaviors.addToPath((0,-20,0))
		self.AIbehaviors.addToPath((0,20,0))
		self.AIbehaviors.addToPath((20,-10,0))
		self.AIbehaviors.addToPath((15,-20,0))
		
		
		self.AIbehaviors.startFollow()"""
		
	def update(self, Task):
		
		self.AIworld.update()
		return Task.cont
