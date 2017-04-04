#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

gi.require_version('Vte', '2.91')
from gi.repository import Vte

import signal
import os

class Term(Vte.Terminal):

	def __init__(self, *args, **kwds):
		super().__init__(*args, **kwds)
		## super(Term, self).__init__(*args, **kwds)

	def init (self):
		self.init_term()

	def init_term (self):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync
		rtn = self.spawn_sync(
			Vte.PtyFlags.DEFAULT,
			os.environ['HOME'],
			['/bin/bash'],
			[],
			GLib.SpawnFlags.DO_NOT_REAP_CHILD,
			None,
			None,
		)

		print(rtn)

		self.watch_child(rtn[1])

		self.show_all()

	def do_child_exited(self, status):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		print('')
		print('do_child_exited:')
		print('	status:', status)

		Gtk.main_quit()

class Win(Gtk.Window):
	title = 'Demo Vte.Terminal'

	term = None

	def __init__(self, *args, **kwds):
		super().__init__(*args, **kwds)
		## super(Win, self).__init__(*args, **kwds)

	def init (self):
		self.init_win()

	def init_term (self):
		self.term = term = Term()
		term.init()

	def init_win (self):
		self.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		self.connect('delete-event', self.on_close_win)

		self.init_term()
		self.add(self.term)

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

## Vte
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes.html

## Vte.Terminal
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
