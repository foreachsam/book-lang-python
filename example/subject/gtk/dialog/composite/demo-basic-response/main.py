#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import signal


class Dia:
	app = None
	win = None
	dia = None

	title = 'Confirm'
	message = 'Quit application. Are you soure?'

	def __init__ (self):
		pass

	def init (self):
		self.dia = dia = Gtk.Dialog(
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

		box = dia.get_content_area()
		box.add(label)
		dia.show_all()

	def show (self):
		rtn = self.run()
		if rtn == Gtk.ResponseType.OK:
			print('The OK button was clicked')
			self.app.go_quit()
		elif rtn == Gtk.ResponseType.CANCEL:
			print('The Cancel button was clicked')
			self.destroy()

	def run (self):
		self.init()
		return self.dia.run()

	def destroy (self):
		return self.dia.destroy()


class Btn:
	app = None
	btn = None
	label = 'Quit application'

	def __init__ (self):
		pass

	def init (self):
		self.init_btn()

	def init_btn (self):
		self.btn = btn = Gtk.Button(label=self.label)
		btn.connect('clicked', self.on_button_clicked)

	def on_button_clicked(self, btn):
		print('')
		print('on_button_clicked:')
		print('	btn:', btn)
		self.go_show_dialog()

	def go_show_dialog(self):
		dia = Dia()
		dia.app = self.app
		dia.win = self.app.win.win
		dia.show()

class Win:
	app = None
	win = None
	btn = None

	title = 'Demo Composite Window'

	def __init__ (self):
		pass

	def init (self):
		self.init_win()

	def init_btn (self):
		self.btn = btn = Btn()
		btn.app = self.app
		btn.init()

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		self.init_btn()
		win.add(self.btn.btn)

		win.show_all()

	def on_close_win (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		self.app.go_quit()
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
		win.app = self
		win.init()

	def run (self):
		self.init()
		Gtk.main()

	def go_quit (self):
		Gtk.main_quit()

def main ():
	app = App()
	app.run()

if __name__ == '__main__':
	main()

## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/dialogs.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize_to_geometry

## Gtk.Button
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html#Gtk.Button.signals.clicked


## Gtk.Dialog
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Dialog.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Dialog.html#Gtk.Dialog.run
