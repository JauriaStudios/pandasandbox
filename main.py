# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

#import pdb

import sys, os
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence

from panda3d.core import CollisionTraverser,CollisionNode
from panda3d.core import CollisionHandlerQueue,CollisionRay
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32, VBase4
from panda3d.core import Point3, TransparencyAttrib,TextNode
from panda3d.core import Filename,AmbientLight,DirectionalLight, PointLight, Spotlight

from pandac.PandaModules import WindowProperties

from utils import Crono, CursorPos, PlayerPos
from player import Player
from enemy import Enemy


class World(ShowBase):
	
	def __init__(self):
		ShowBase.__init__(self)
		
		#pdb.set_trace()
		self.dt6 = Player(self,100, 50, 5, 2)
		self.foe1 = Enemy(100, 50, 5, 2)
		
		self.crono = Crono(self)
		self.cursorpos = CursorPos(self)
		self.playerpos = PlayerPos(self)
		
		self.crono.draw(0.7, -0.85)
		self.cursorpos.draw(0.0, -0.85)
		self.playerpos.draw(-0.7, -0.85)
		
		self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
		
		# Load the models.
		
		self.environ = self.loader.loadModel("models/castillo")
		#self.juggernaut = self.loader.loadModel("models/juggernaut")
		self.statusBar = self.loader.loadModel("models/statusbar")
		
		
		self.statusBar.setDepthTest(True)
		self.statusBar.setDepthWrite(True)
		# Load the actors.
		
		# Reparent the model to render.
		
		self.environ.reparentTo(self.render)
		
		
		# Reparent the model to render2d.
		
		#self.juggernaut.reparentTo(self.render2d)
		self.statusBar.reparentTo(self.render2d)
		
		
		#texture_dt6 = self.loader.loadTexture("models/tex/Cube_AO.png")
		#texture_env = self.loader.loadTexture("models/tex/Plane_AO.png")
		#texture_jug = self.loader.loadTexture("models/juggernaut.png")
		#texture_stats = self.loader.loadTexture("models/statusbar.png")
		
		#self.dt6.setTexture(texture_dt6)
		#self.environ.setTexture(texture_env)
		#self.juggernaut.setTexture(texture_jug)
		#self.statusBar.setTexture(texture_stats)
		
		# Apply scale and position transforms on the model.
		self.environ.setScale(8, 8, 8)
		self.environ.setPos(0, 0, 0)
		
		#self.juggernaut.setScale(0.03, 0.03, 0.03)
		#self.juggernaut.setPos(0.75, 0, 0.6)
		
		
		self.statusBar.setScale(0.15, 0.15, 0.15)
		self.statusBar.setPos(-0.95, 0, 0.65)
		
		
		
		# Add the spinCameraTask procedure to the task manager.
		
		#self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
		self.taskMgr.add(self.dt6.move, "moveTask")
		
		self.taskMgr.add(self.crono.task, "cronoTask")
		self.taskMgr.add(self.cursorpos.task, "cursorposTask")
		self.taskMgr.add(self.playerpos.task, "playerposTask")
		self.taskMgr.add(self.foe1.update, "enemyTask")
		
		# Accept the control keys
		self.accept("escape", sys.exit)
		
		
		self.accept("c", self.crono.start)
		
		
		# Window change event handler
		#self.windowEventSetup()
		
		
		# Uncomment this line to see the collision rays
		#self.dt6GroundColNp.show()
		
		#self.camGroundColNp.show()
	   
		# Uncomment this line to show a visual representation of the 
		# collisions occuring
		#self.cTrav.showCollisions(render)
		
		# Create some lighting
		
		ambientLight = AmbientLight("ambientLight")
		ambientLight.setColor(Vec4(.1, .1, .1, 1))
		directionalLight = DirectionalLight("directionalLight")
		directionalLight.setDirection(Vec3(-10, -10, -10))
		directionalLight.setColor(Vec4(1, 1, 1, 1))
		directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
		
		plight1 = PointLight('plight1')
		plight1.setColor(VBase4(1, 1, 1, 0.05))
		plight1.showFrustum()
		plight1.setShadowCaster(True)
		plnp1 = render.attachNewNode(plight1)
		plnp1.setPos(26.71, -33.2, 6)
		
		render.setLight(plnp1)
		render.setLight(render.attachNewNode(ambientLight))
		self.environ.setShaderAuto()
		
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
