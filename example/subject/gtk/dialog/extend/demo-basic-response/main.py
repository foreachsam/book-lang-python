#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import signal


class Dia (Gtk.Dialog):
	win = None

	title = 'Confirm'
	message = 'Quit application. Are you soure?'

	def __init__(self):
		pass

	def init (self):
		Gtk.Dialog.__init__(
			self,
			self.title,
			self.win,
			1,
			(
				Gtk.STOCK_CANCEL,
				Gtk.ResponseType.CANCEL,
				Gtk.STOCK_OK,
				Gtk.ResponseType.OK
			)
		)

		label = Gtk.Label(self.message)

		box = self.get_content_area()
		box.add(label)
		self.show_all()


class Btn (Gtk.Button):
	win = None
	label = 'Quit application'

	def __init__ (self):
		pass

	def init (self):
		self.init_btn()

	def init_btn (self):
		Gtk.Button.__init__(self, label=self.label)
		self.connect('clicked', self.on_button_clicked)

	def on_button_clicked(self, btn):
		print('')
		print('on_button_clicked:')
		print('	btn:', btn)
		self.go_show_dialog()

	def go_show_dialog(self):
		dia = Dia()
		dia.win = self.win
		dia.init()
		rtn = dia.run()

		if rtn == Gtk.ResponseType.OK:
			print('The OK button was clicked')
			Gtk.main_quit()
		elif rtn == Gtk.ResponseType.CANCEL:
			print('The Cancel button was clicked')
			dia.destroy()

class Win (Gtk.Window):
	title = 'Demo Extent Window'

	btn = None

	def __init__ (self):
		pass

	def init (self):
		self.init_win()

	def init_btn (self):
		self.btn = btn = Btn()
		btn.win = self
		btn.init()

	def init_win (self):
		Gtk.Window.__init__(self, title=self.title)
		#self.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		self.connect('delete-event', self.on_close_win)

		self.init_btn()
		self.add(self.btn)

		self.show_all()

	def on_close_win (self, win, evt):
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
