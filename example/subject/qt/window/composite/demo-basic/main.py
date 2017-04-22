#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Win:
	app = None
	win = None
	view = None

	title = 'Demo Composite Window'
	width = 800
	height = 600
	top = 200
	left = 200

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()
		self.view = self.win

	def init_win (self):
		self.win = win = QWidget()

		win.setWindowTitle(self.title)
		win.resize(self.width, self.height)
		win.move(self.top, self.left)

		win.show()


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
