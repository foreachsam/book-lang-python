#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Win (QWidget):
	app = None
	#win = None
	#view = None

	title = 'Demo Extent Window'
	width = 800
	height = 600
	top = 200
	left = 200

	#def __init__(self, *args, **kwds):
	#	super().__init__(*args, **kwds)

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()

	def init_win (self):
		self.setWindowTitle(self.title)
		self.resize(self.width, self.height)
		self.move(self.top, self.left)

		self.show()


class App:
	app = None

	#def __init__ (self):
	#	pass

	def init (self):
		self.app = app = QApplication(sys.argv)

		self.win = win = Win()
		win.app = self
		win.init()

	def run (self):
		#sys.exit(self.app.exec_())
		self.app.exec()

def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
