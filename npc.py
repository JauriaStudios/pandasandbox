# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from direct.task import Task

from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode

from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import CollideMask

from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence

from panda3d.ai import *

class Npc():
	def __init__(self, app, hp, mana, speed, attackSpeed, name):
		
		
		self.app = app
		
		self.hp = hp
		self.mana = mana
		self.speed = speed
		self.attackSpeed = attackSpeed
		
		self.name = name
		
		
		self.model = "models/%s" % self.name
		self.modelWalk = "models/%s-walk" % self.name
		
		self.npcActor = Actor({	"body":self.model,},
							{"body":{"walk":self.modelWalk},
						})
		
		self.npcActor.setHpr(0,0,0)
		self.npcActor.setPos(0,0,-3.3)
		self.npcActor.setScale(0.5)
		self.npcActor.reparentTo(render)
		
		self.setupAI()
		
	def getName(self):
		return self.name
		
	def attacked(self, damage):
		print("man pegao")
		self.hp -= damage
		if self.hp <= 0:
			self.npcActor.detachNode()
			self.npcActor.removeNode()
			self.app.taskMgr.remove("%sTask" % self.name)
		
	def setupAI(self):
		
		
		
		#Creating AI World
		
		self.AIworld = AIWorld(render)
		
		self.AIchar = AICharacter("npc", self.npcActor, 100, 0.05, 5)
		self.AIworld.addAiChar(self.AIchar)
		
		self.AIbehaviors = self.AIchar.getAiBehaviors()
		
		
		
		self.AIbehaviors.wander(10, 0, 15, 1.0)
		
		
		#Path follow (note the order is reveresed)
		"""
		self.AIbehaviors.pathFollow(1)
		self.AIbehaviors.addToPath((0,-20,0))
		self.AIbehaviors.addToPath((0,20,0))
		self.AIbehaviors.addToPath((20,-10,0))
		self.AIbehaviors.addToPath((15,-20,0))
		
		self.AIbehaviors.startFollow()
		"""
		self.npcActor.loop("walk")
		
		
	def update(self, Task):
		
		self.AIworld.update()
		return Task.cont
