# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from direct.task import Task

from panda3d.core import Point3
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode

from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape

from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence

from panda3d.ai import *

class Enemy():
	def __init__(self, app, hp, mana, speed, attackSpeed):
		
		
		self.app = app
		
		self.shape = BulletBoxShape(Vec3(1.5, 1.5, 1.5))
 
		self.node = BulletRigidBodyNode('Box')
		self.node.setMass(1.0)
		self.node.addShape(self.shape)
		 
		self.np = render.attachNewNode(self.node)
		self.np.setPos(10, 0, 0)
		self.np.setCollideMask(BitMask32.allOn())
		self.np.show()
		
		self.app.world.attachRigidBody(self.node)
		
		self.hp = hp
		self.mana = mana
		self.speed = speed
		self.attackSpeed = attackSpeed
		
		self.enemyActor = Actor({	"body":"models/bug",},
							{"body":{"walk":"models/bug-walk"},
						})
		self.enemyActor.setHpr(0,0,0)
		self.enemyActor.setPos(10,0,0)
		self.enemyActor.setScale(0.5)
		self.enemyActor.reparentTo(self.np)
		
		self.setupAI()
		
	def setupAI(self):
		
		
		self.enemyActor.loop("walk")
		#Creating AI World
		self.AIworld = AIWorld(render)

		self.AIchar = AICharacter("enemy",self.enemyActor, 60, 0.05, 5)
		self.AIworld.addAiChar(self.AIchar)
		self.AIbehaviors = self.AIchar.getAiBehaviors()

		#Path follow (note the order is reveresed)
		self.AIbehaviors.pathFollow(1)
		self.AIbehaviors.addToPath((0,-10,0))
		self.AIbehaviors.addToPath((0,10,0))
		self.AIbehaviors.addToPath((10,-10,0))
		self.AIbehaviors.addToPath((10,-10,0))

		self.AIbehaviors.startFollow()
		
	def update(self, Task):
		
		self.AIworld.update()
		return Task.cont
