# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from direct.task import Task

from panda3d.core import Point3
from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode

from direct.actor.Actor import Actor

from direct.interval.IntervalGlobal import Sequence

from panda3d.ai import *

class Enemy():
	def __init__(self, hp, mana, speed, attackSpeed):
		
		self.hp = hp
		self.mana = mana
		self.speed = speed
		self.attackSpeed = attackSpeed
		
		self.enemyActor = Actor({	"body":"models/bug",},
							{"body":{"walk":"models/bug-walk"},
						})
		self.enemyActor.setHpr(0,0,0)
		self.enemyActor.setPos(0,0,0)
		self.enemyActor.setScale(0.5)
		self.enemyActor.reparentTo(render)
		
		
		self.cTrav = CollisionTraverser()
		
		self.enemyGroundRay = CollisionRay()
		self.enemyGroundRay.setOrigin(0,0,1000)
		self.enemyGroundRay.setDirection(0,0,-1)
		self.enemyGroundCol = CollisionNode('enemyRay')
		self.enemyGroundCol.addSolid(self.enemyGroundRay)
		self.enemyGroundCol.setFromCollideMask(BitMask32.bit(0))
		self.enemyGroundCol.setIntoCollideMask(BitMask32.allOff())
		self.enemyGroundColNp = self.enemyActor.attachNewNode(self.enemyGroundCol)
		self.enemyGroundHandler = CollisionHandlerQueue()
		self.cTrav.addCollider(self.enemyGroundColNp, self.enemyGroundHandler)
		
		#self.enemyGroundColNp.show()
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
		
		startpos = self.enemyActor.getPos()
		
		self.cTrav.traverse(render)
		
		# Adjust enemy's Z coordinate.  If enemy's ray hit terrain,
		# update his Z. If it hit anything else, or didn't hit anything, put
		# him back where he was last frame.
		
		entries = []
		for i in range(self.enemyGroundHandler.getNumEntries()):
			entry = self.enemyGroundHandler.getEntry(i)
			entries.append(entry)
		entries.sort(lambda x,y: cmp(y.getSurfacePoint(render).getZ(),
									 x.getSurfacePoint(render).getZ()))
		if (len(entries)>0) and (entries[0].getIntoNode().getName() == "terrain"):
			self.enemyActor.setZ(entries[0].getSurfacePoint(render).getZ())
		else:
			self.enemyActor.setPos(startpos)

		return Task.cont
