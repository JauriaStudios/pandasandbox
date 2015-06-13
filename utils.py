# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Just sandboxing

from time import *

from panda3d.core import TextNode

from direct.task import Task

from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText

"""
	def drawGui(self):
		
		
		# Load the pictures.
		
		self.hp = OnscreenImage(image = 'hp.png',
								pos = (-1.185, 0, -0.85),
								scale = (0.15, 0.15, 0.15)
								)
								
		self.hp.setTransparency(TransparencyAttrib.MAlpha)
		
		self.mana = OnscreenImage(image = 'mana.png',
								pos = (1.185, 0, -0.85),
								scale = (0.15, 0.15, 0.15)
								)
								
		self.mana.setTransparency(TransparencyAttrib.MAlpha)
		"""

class Crono():
	
	def __init__(self, app):
		
		
		self.app = app
		self.countRunning = False
		self.count = 0
		self.counttime = 0.5
		self.countMax = 30
		
		self.windowGui = self.app.loader.loadModel("models/window")
		
		self.windowGui.setDepthTest(True)
		self.windowGui.setDepthWrite(True)
		
	def draw(self, x, y):
		
		self.windowGui.setScale(0.06, 0.06, 0.06)
		self.windowGui.setPos(x, 0, y)
		self.windowGui.reparentTo(self.app.render2d)
		
		
		clockStr = "00:00:%s" % self.countMax
		
		self.clockMsg = OnscreenText(text=clockStr, style=1, fg=(1,1,1,1), pos=(x+0.1, y-0.01), align=TextNode.ALeft, scale = .05)
		
	def task(self, Task):
		
		#print strftime("%H:%M:%S", localtime())
		horas = int(strftime("%H", localtime()))
		minutos = int(strftime("%M", localtime()))
		segundos = int(strftime("%S", localtime()))
		
		sec = minutos*60
		minute = horas*60
		segundosTotales = segundos+sec+minute
		#print segundosTotales
		countStart = 0
		
		if self.countRunning:
			if ( (segundosTotales - self.count) > self.counttime ):
				self.count = segundosTotales
				self.countMax -= 1
				if self.countMax >= 0:
					clockStr = "00:00:%s" % self.countMax
					self.clockMsg.setText(clockStr)
				else:
					self.countRunning = False
					self.countMax = 30
			
		
		return Task.cont
		
	def start(self):
		
		self.countRunning = True
		print "countdown starts"

class CursorPos():
	
	def __init__(self, app):
		
		self.app = app
		
	
		self.windowGui = self.app.loader.loadModel("models/window")
		
		self.windowGui.setDepthTest(True)
		self.windowGui.setDepthWrite(True)
		
	def draw(self,x ,y):
		
		self.windowGui.setScale(0.06, 0.06, 0.06)
		self.windowGui.setPos(x, 0, y)
		self.windowGui.reparentTo(self.app.render2d)
		
		msg = ['']*2
		self.coord = ['']*2
		
		msg[0] = ("Mouse X: 0")
		msg[1] = ("Mouse Y: 0")
		
		
		self.coord[0] = OnscreenText(text=msg[0], style=1, fg=(1,1,1,1), pos=(x-0.2, y+0.01), align=TextNode.ALeft, scale = .05)
		self.coord[1] = OnscreenText(text=msg[1], style=1, fg=(1,1,1,1), pos=(x-0.2, y-0.03), align=TextNode.ALeft, scale = .05)
			
	def task(self, task):
		
		x = 0
		y = 0
		
		if self.app.mouseWatcherNode.hasMouse():
			mpos = self.app.mouseWatcherNode.getMouse()
			x = mpos.getX()
			y = mpos.getY()
			
			msg = ['']*2
			pos = ['']*2
			
			msg[0] = ("Mouse X: %.2f" % x)
			msg[1] = ("Mouse Y: %.2f" % y)
			
			for i in range(len(msg)):
				self.coord[i].setText(msg[i])
		
		return Task.cont

class PlayerPos():
	
	def __init__(self, app):
		self.app = app
		self.lastPos = 0
	
		self.windowGui = self.app.loader.loadModel("models/window")
		
		self.windowGui.setDepthTest(True)
		self.windowGui.setDepthWrite(True)
		self.posx = 0
		self.posy = 0
		self.posz = 0
		
		
	def draw(self,x ,y):
		
		self.windowGui.setScale(0.06, 0.06, 0.06)
		self.windowGui.setPos(x, 0, y)
		self.windowGui.reparentTo(self.app.render2d)
		
		msg = ['']*3
		self.coord = ['']*3
		
		msg[0] = ("Player X: 0")
		msg[1] = ("Player Y: 0")
		msg[2] = ("Player Z: 0")
		
		
		self.coord[0] = OnscreenText(text=msg[0], style=1, fg=(1,1,1,1), pos=(x-0.5, y+0.01), align=TextNode.ALeft, scale = .05)
		self.coord[1] = OnscreenText(text=msg[1], style=1, fg=(1,1,1,1), pos=(x-0.5, y-0.03), align=TextNode.ALeft, scale = .05)
		self.coord[2] = OnscreenText(text=msg[2], style=1, fg=(1,1,1,1), pos=(x-0.5, y-0.07), align=TextNode.ALeft, scale = .05)
		
	def task(self, task):
		
		
		pos = self.app.dt6.playerActor.getPos()
		
		msg = ['']*3
		
		if self.lastPos != pos:
			self.posx = pos[0]
			self.posy = pos[1]
			self.posz = pos[2]
			self.lastPos = pos
			
		
			msg[0] = ("Player X: %.2f" % self.posx)
			msg[1] = ("Player Y: %.2f" % self.posy)
			msg[2] = ("Player Z: %.2f" % self.posz)
			
			for i in range(len(msg)):
				self.coord[i].setText(msg[i])
		
		return Task.cont
