# -*- coding: utf-8 -*-
# Authors: ep0s TurBoss
# Models: ep0s TurBoss

# Load Bar

from direct.gui.DirectGui import DirectWaitBar
from direct.showbase import DirectObject

class Bar(DirectObject.DirectObject):
	def __init__( self):
		self.bar = DirectWaitBar(text = "Loading...", value = 0, pos = (0,.4,.4))
		self.bar.hide()

	def incBar(self, arg):
		self.bar['value'] +=	arg
		#text = str(bar['value'])
		#textObject.setText(text)

	def show(self):
		self.bar.show()

	def hide(self):
		self.bar.hide()
