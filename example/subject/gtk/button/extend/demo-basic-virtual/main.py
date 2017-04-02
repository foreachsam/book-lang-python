#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import signal

class Btn(Gtk.Button):

	def __init__ (self):
		pass

	def init (self):
		self.init_btn()

	def init_btn (self):
		Gtk.Button.__init__(self, label='Click Here')

		#self.connect('clicked', self.on_button_clicked)

	def do_clicked(self):
		print('')
		print('do_clicked:')
		print('	self:', self)

class Win(Gtk.Window):
	title = 'Demo Extent Window'

	btn = None

	def __init__ (self):
		pass

	def init (self):
		self.init_win()

	def init_btn (self):
		self.btn = btn = Btn()
		btn.init()

	def init_win (self):
		Gtk.Window.__init__(self, title=self.title)
		#self.set_title(self.title)

		self.init_btn()
		self.add(self.btn)

		self.show_all()

	def do_delete_event (self, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.do_delete_event
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

		return True

class Signal:
	def __init__ (self):
		pass

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)

class App:
	def __init__ (self):
		pass

	def init (self):
		self.signal = signal = Signal()
		signal.init()

		self.win = win = Win()
		win.init()

	def run (self):
		self.init()
		Gtk.main()

def main ():
	app = App()
	app.run()

if __name__ == '__main__':
	main()

## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html

## Gtk.Button
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html#Gtk.Button.signals.clicked
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html#Gtk.Button.do_clicked
