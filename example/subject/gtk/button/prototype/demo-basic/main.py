#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import signal


## https://docs.python.org/3/library/signal.html
## https://docs.python.org/2/library/signal.html
signal.signal(signal.SIGINT, signal.SIG_DFL)


def on_button_clicked(btn):
	print('')
	print('on_button_clicked:')
	print('	btn:', btn)


win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)


btn = Gtk.Button(label='Click Here')
btn.connect('clicked', on_button_clicked)
win.add(btn)


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

## Gtk.Button
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Button.html#Gtk.Button.signals.clicked
