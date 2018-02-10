#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import qApp

from PyQt5.QtWidgets import QSystemTrayIcon
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

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


class Indicator:
	app = None
	view = None
	tray = None
	menu = None

	def prep (self, *args, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_tray()
		self.view = self.tray

	def init_tray (self):

		#http://pyqt.sourceforge.net/Docs/PyQt5/api/qicon.html
		#https://doc.qt.io/qt-5/qicon.html#QIcon-4
		#https://doc.qt.io/qt-5/qicon.html#fromTheme
		#https://doc.qt.io/qt-5/qtwidgets-widgets-icons-example.html


		#self.tray = QSystemTrayIcon(self.app.win.view)
		#self.tray = QSystemTrayIcon(QIcon('icon.png'), self.app.win.view)
		self.tray = QSystemTrayIcon(QIcon.fromTheme('folder'), self.app.win.view)


		self.init_menu()
		self.tray.setContextMenu(self.menu)

		self.tray.show()

	def init_menu (self):
		self.menu = QMenu()

		item = QAction('Exit', self.menu)
		#item.triggered.connect(qApp.quit)
		item.triggered.connect(self.on_quit_app)
		self.menu.addAction(item)

		item = QAction('Help', self.menu)
		item.triggered.connect(self.on_show_help)
		self.menu.addAction(item)

		item = QAction('Info', self.menu, triggered=self.on_show_info)
		self.menu.addAction(item)

	def on_quit_app(self, rs):
		## print(rs)
		self.app.go_quit()

	def on_show_help(self, rs):
		print('show help')

	def on_show_info(self, rs):
		print('show info')


class Win:
	app = None
	win = None
	view = None

	title = 'Demo QSystemTrayIcon Window'
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

		self.indicator = indicator = Indicator()
		indicator.app = self
		indicator.init()


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
