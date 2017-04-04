#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

gi.require_version('Vte', '2.91')
from gi.repository import Vte

import os
import signal


## https://docs.python.org/3/library/signal.html
## https://docs.python.org/2/library/signal.html
signal.signal(signal.SIGINT, signal.SIG_DFL)


win = Gtk.Window()
win.set_title('Demo Vte.Terminal')
win.connect('delete-event', Gtk.main_quit)


## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.new
term = Vte.Terminal()

## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync
rtn = term.spawn_sync(
	Vte.PtyFlags.DEFAULT,
	os.environ['HOME'],
	['/bin/bash'],
	[],
	GLib.SpawnFlags.DO_NOT_REAP_CHILD,
	None,
	None,
)

print(rtn)

term.show_all()

win.add(term)

win.show_all()
Gtk.main()


## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
