#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as WebKit

import signal


## https://docs.python.org/3/library/signal.html
## https://docs.python.org/2/library/signal.html
signal.signal(signal.SIGINT, signal.SIG_DFL)

## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize_to_geometry
win = Gtk.Window()
win.connect('delete-event', Gtk.main_quit)
win.resize(600, 800)

## WebKit2
## https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0
## https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes/WebView.html
webview = WebKit.WebView()
webview.load_uri('https://www.google.com')
win.add(webview)


win.show_all()
Gtk.main()
