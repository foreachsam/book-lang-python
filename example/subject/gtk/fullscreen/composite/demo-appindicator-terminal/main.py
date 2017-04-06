#!/usr/bin/env python3

## Demo Switch Fullscreen
## * Double click
## * F11

## Demo Switch Activate
## * <Super>a


import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib

gi.require_version('Vte', '2.91')
from gi.repository import Vte

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator

gi.require_version('Keybinder', '3.0')
from gi.repository import Keybinder

import signal
import os


class Term:
	app = None
	term = None

	def __init__ (self):
		pass

	def init (self):
		self.init_term()

	def init_term (self):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.new
		self.term = term = Vte.Terminal()

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

		##term.watch_child(rtn[1])

		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		term.connect('child-exited', self.on_child_exited);

		## mouse button event
		term.connect('button-press-event', self.on_button_press)
		term.connect('button-release-event', self.on_button_release)

		term.show_all()

	def on_child_exited(self, term, status):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		print('')
		print('on_child_exited:')
		print('	term:', term)
		print('	status:', status)

		self.app.go_quit()

	def on_button_press (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.button_press_event
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes/EventButton.html#Gdk.EventButton
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/flags.html#Gdk.ModifierType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType.DOUBLE_BUTTON_PRESS
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType._2BUTTON_PRESS

		if self.app.is_debug:
			print('')
			print('on_button_press:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)

		## on mouse left button double click
		if evt.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:
			self.app.win.go_switch_fullscreen()
			#return True

		#return False

	def on_button_release (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.button_release_event

		if self.app.is_debug:
			print('')
			print('on_button_release:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)

		return False


class Indicator:
	app = None

	icon_name_on_win_activate = 'terminal'
	icon_name_on_win_deactivate = 'video-display'
	icon_name_btn_app_quit = 'application-exit'

	def __init__ (self):
		pass

	def init (self):
		self.init_menu()

	def init_menu(self):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html#Gtk.Menu.new
		self.menu = menu = Gtk.Menu()

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html#Gtk.MenuItem.new
		item = Gtk.MenuItem.new_with_label('Activate (<Super>a)')
		item.connect('activate', self.on_activate_win)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Fullscreen (F11)')
		item.connect('activate', self.on_fullscreen_win)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('About')
		item.connect('activate', self.on_show_about)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Test')
		item.connect('activate', self.on_test)
		menu.append(item)


		#http://www.pygtk.org/pygtk2reference/gtk-stock-items.html
		#https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Image.html#Gtk.Image.new_from_icon_name
		img = Gtk.Image.new_from_icon_name(self.icon_name_btn_app_quit, 16)
		## item = Gtk.MenuItem.new_with_label('quit')
		## https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ImageMenuItem.html#Gtk.ImageMenuItem.new_with_label
		item = Gtk.ImageMenuItem.new_with_label('Quit')
		#item.connect('activate', Gtk.main_quit)
		item.connect('activate', self.on_quit_app)
		item.set_image(img)
		menu.append(item)


		menu.show_all()

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html
		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.new
		# new (id, icon_name, category)
		self.indicator = indicator = AppIndicator.Indicator.new(
			self.app.name,
			self.icon_name_on_win_activate,
			AppIndicator.IndicatorCategory.APPLICATION_STATUS
		)

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_menu
		indicator.set_menu(menu)

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_status
		indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
		#type(indicator)
		#<class 'gi.repository.AppIndicator3.Indicator'>

	def on_test(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_test:')
			print('	menu_item:', menu_item)

	def on_show_about(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_show_about:')
			print('	menu_item:', menu_item)
		self.app.go_show_about()

	def on_quit_app(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_quit_app:')
			print('	menu_item:', menu_item)

		self.app.go_quit()

	def on_activate_win(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_activate_win:')
			print('	menu_item:', menu_item)

		self.app.win.go_activate()

	def on_fullscreen_win(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_fullscreen_win:')
			print('	menu_item:', menu_item)

		self.app.win.go_fullscreen()

	def go_switch_icon_on_win_activate(self):
		self.indicator.set_icon(self.icon_name_on_win_activate)

	def go_switch_icon_on_win_deactivate(self):
		self.indicator.set_icon(self.icon_name_on_win_deactivate)


class Win:
	app = None
	win = None
	term = None

	title = 'Demo Fullscreen Appindicator Terminal App'

	state_fullscreen = False
	state_activate = True

	width = 800
	height = 600


	def __init__ (self):
		pass

	def init (self):
		self.init_win()

	def init_term (self):
		self.term = term = Term()
		term.app = self.app
		term.init()

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)

		#win.resize(self.width, self.height)
		#win.resize_to_geometry(self.width, self.height)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		## keyboard key event
		win.connect('key-press-event', self.on_key_press)
		win.connect('key-release-event', self.on_key_release)

		self.init_term()
		win.add(self.term.term)

		win.show_all()


	def on_close_win (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event

		if self.app.is_debug:
			print('')
			print('on_close_app:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))

		self.go_deactivate()
		## self.app.go_quit()

		return True # must True. For switch indicator icon work.

	def on_key_press (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.key_press_event
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes/EventKey.html
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/flags.html#Gdk.ModifierType
		## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/enums.html#Gdk.EventType
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_get_label
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_name

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)


		if self.app.is_debug:
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

		return self.app.keybind.handle_by_accelerator_name(accelerator_name)


	def on_key_release (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.key_release_event

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)

		if self.app.is_debug:
			print('')
			print('on_key_release:')
			print('	win:', win)
			print('	evt:', evt)
			print('	dir(evt):', dir(evt))
			print('	evt.type:', evt.type)
			print('	accelerator_name:', accelerator_name)
			print('	accelerator_label:', accelerator_label)

		return False

	## fullscreen
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
		self.go_activate()

	def go_unfullscreen (self):
		self.set_state_fullscreen(False)
		self.win.unfullscreen()
		self.go_show_default()

	## activate
	def is_activate (self):
		return self.state_activate

	def set_state_activate (self, val):
		self.state_activate = val

	def go_switch_activate (self):
		if self.is_activate():
			self.go_deactivate()
		else:
			self.go_activate()

	def go_activate (self):
		self.set_state_activate(True)
		self.win.present()
		self.app.indicator.go_switch_icon_on_win_activate()
		self.go_show_default()

	def go_deactivate (self):
		self.set_state_activate(False)
		self.win.hide()
		self.app.indicator.go_switch_icon_on_win_deactivate()

	def go_show_default (self):
		self.win.move(200,200)


class Keybind:
	app = None

	accelerator_name_activate = '<Super>a'
	accelerator_name_fullscreen = 'F11'
	accelerator_name_play_youtube = 'F1'

	def __init__ (self):
		pass

	def init (self):
		self.init_keybind()

	def init_keybind(self):
		if self.app.is_debug:
			print('')
			print('init_keybind:')
			print('	accelerator_name_activate:', self.accelerator_name_activate)

		Keybinder.init()
		Keybinder.bind(self.accelerator_name_activate, self.on_key_activate_win)

	def on_key_activate_win(self, accelerator_name):
		if self.app.is_debug:
			print('')
			print('on_key_activate_win:')
			print('	accelerator_name:', accelerator_name)

		self.app.win.go_switch_activate()
		## self.app.win.go_activate()

	def handle_by_accelerator_name(self, accelerator_name):
		## on press [F11]
		## if accelerator_label == 'F11':
		if accelerator_name == self.app.keybind.accelerator_name_fullscreen:
			self.app.win.go_switch_fullscreen()
			return True

		return False


class Signal:
	app = None

	def __init__ (self):
		pass

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)


class App:

	#is_debug = True
	is_debug = False

	name = 'DemoFullscreenAppindicatorTerminalApp'

	signal = None
	win = None
	indicator = None
	keybind = None

	def __init__ (self):
		pass

	def init (self):
		self.signal = signal = Signal()
		signal.app = self
		signal.init()

		self.win = win = Win()
		win.app = self
		win.init()

		self.indicator = indicator = Indicator()
		indicator.app = self
		indicator.init()

		self.keybind = keybind = Keybind()
		keybind.app = self
		keybind.init()

	def run (self):
		self.init()
		Gtk.main()

	def go_show_about(self):
		if self.is_debug:
			print('')
			print('app.go_show_about:')

	def go_quit(self):
		if self.is_debug:
			print('')
			print('app.go_quit:')

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
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

## Vte
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes.html

## Vte.Terminal
## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html
