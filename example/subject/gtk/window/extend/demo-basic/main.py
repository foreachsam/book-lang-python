#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Win(Gtk.Window):

	title = 'Demo Extent Window'

	def __init__ (self):
		pass

	def init (self):
		self.init_win()

	def init_win (self):
		Gtk.Window.__init__(self, title=self.title)
		#self.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		self.connect('delete-event', self.on_close_win)
		self.show_all()

	def on_close_win (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

		return True

class App:
	def __init__ (self):
		pass

	def init (self):
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
