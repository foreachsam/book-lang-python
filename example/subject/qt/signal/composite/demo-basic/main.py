#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import qApp

import signal

class Signal:
	app = None

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		## for [<Ctrl>+c]
		signal.signal(signal.SIGINT, signal.SIG_DFL)


class Win:
	app = None
	win = None
	view = None

	title = 'Demo Signal'
	width = 800
	height = 600
	top = 200
	left = 200

	def prep (self, *args, **kwds):
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
		self.signal = signal = Signal()
		self.app = self
		signal.init()

		self.app = app = QApplication(sys.argv)

		self.win = win = Win()
		win.app = self
		win.init()

	def run (self):
		#sys.exit(self.app.exec_())
		self.app.exec()

	def go_quit (self):
		qApp.quit()

def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()
