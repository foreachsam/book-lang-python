#!/usr/bin/env python3

## Demo Switch Fullscreen
## * Double click
## * F11

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class App:
	is_debug = True
	#is_debug = False

	app_name = 'DemoFullScreenApp'
	app_title = 'Demo Fullscreen App'

	#icon_name = 'folder'
	#icon_name = 'image'
	#icon_name = 'video-display'
	icon_name = 'video'

	state_fullscreen = False
	state_shown = True

	def __init__ (self):
		self.init_win()

	def init_win (self):
		self.win = win = Gtk.Window()

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.set_title
		win.set_title(self.app_title)
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.set_icon_name
		win.set_icon_name(self.icon_name)

		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_app)

		## mouse button event
		win.connect('button-press-event', self.on_button_press)
		win.connect('button-release-event', self.on_button_release)

		## keyboard key event
		win.connect('key-press-event', self.on_key_press)
		win.connect('key-release-event', self.on_key_release)

		win.show_all()

	def on_close_app (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event

		if self.is_debug:
			print('')
			print('on_close_app:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

	def on_button_press (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.button_press_event
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes/EventButton.html#Gdk.EventButton
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/flags.html#Gdk.ModifierType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType.DOUBLE_BUTTON_PRESS
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType._2BUTTON_PRESS

		if self.is_debug:
			print('')
			print('on_button_press:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)

		## on mouse left button double click
		if evt.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
			self.go_switch_fullscreen()
			return True

		return False

	def on_button_release (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.button_release_event

		if self.is_debug:
			print('')
			print('on_button_release:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)

		return False

	def on_key_press (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.key_press_event
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes/EventKey.html
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/flags.html#Gdk.ModifierType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_get_label
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_name

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)


		if self.is_debug:
			print('')
			print('on_key_press:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)

			#print('	get_keycode:', evt.get_keycode())
			#print('	get_keyval:', evt.get_keyval())
			#print('	hardware_keycode:', evt.hardware_keycode)
			#print('	keyval:', evt.keyval)

			#get_keycode: (True, keycode=95)
			#get_keyval: (True, keyval=65480)
			#hardware_keycode: 95
			#keyval: 65480

			print('	accelerator_name:', accelerator_name)
			print('	accelerator_label:', accelerator_label)

		## on press [F11]
		## if accelerator_label == 'F11':
		if accelerator_name == 'F11':
			self.go_switch_fullscreen()
			return True

		return False

	def on_key_release (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.key_release_event

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)

		if self.is_debug:
			print('')
			print('on_key_release:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)
			print('	accelerator_name:', accelerator_name)
			print('	accelerator_label:', accelerator_label)

		return False

	def is_fullscreen (self):
		return self.state_fullscreen

	def set_state_fullscreen (self, val):
		self.state_fullscreen = val

	def go_switch_fullscreen (self):
		if self.is_fullscreen():
			self.go_unfullscreen()
		else:
			self.go_fullscreen()

	def go_fullscreen (self):
		self.set_state_fullscreen(True)
		self.win.fullscreen()

	def go_unfullscreen (self):
		self.set_state_fullscreen(False)
		self.win.unfullscreen()


	def run (self):
		Gtk.main()

def main ():
	app = App()
	app.run()


if __name__ == '__main__':
	main()

## https://wiki.gnome.org/Projects/PyGObject
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/
## https://lazka.github.io/pgi-docs/

## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## https://lazka.github.io/pgi-docs/#Gdk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_name
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_get_label

## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes.html

## freedesktop.org / www / Specifications
## https://freedesktop.org/wiki/Specifications/

## Desktop Entry Specification
## https://freedesktop.org/wiki/Specifications/desktop-entry-spec/
## https://standards.freedesktop.org/desktop-entry-spec/
## https://standards.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html

## Icon Theme specification
## https://freedesktop.org/wiki/Specifications/icon-theme-spec/
## https://specifications.freedesktop.org/icon-theme-spec/
## https://specifications.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html

## /usr/share/icons/
## ~/.local/share/icons/
## /usr/share/icons/hicolor/
## ~/.local/share/icons/hicolor/

## $ dpkg -l '*icon*'
## $ dpkg -l '*xdg*'

## $ dpkg -L hicolor-icon-theme
## $ dpkg -L xdg-utils
## $ dpkg -L gnome-icon-theme
