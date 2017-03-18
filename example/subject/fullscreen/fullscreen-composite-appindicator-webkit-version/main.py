#!/usr/bin/env python3

## Demo Switch Fullscreen
## * Double click
## * F11

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator

gi.require_version('Keybinder', '3.0')
from gi.repository import Keybinder

gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2 as WebKit

import subprocess


class WebView:
	uri_google = 'https://www.google.com'
	uri_youtube = 'https://www.youtube.com'
	uri_default = 'https://www.google.com'

	def __init__ (self):
		pass

	def init (self):
		self.init_webview()

	def init_webview (self):
		self.webview = webview = WebKit.WebView()

		self.go_load_default()

		## mouse button event
		webview.connect('button-press-event', self.on_button_press)
		webview.connect('button-release-event', self.on_button_release)

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
			return True

		return False

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

	def go_load_default (self):
		self.webview.load_uri(self.uri_default)

	def go_get_uri (self):
		return self.webview.get_uri()

	def go_load_google (self):
		self.webview.load_uri(self.uri_google)

	def go_load_youtube (self):
		self.webview.load_uri(self.uri_youtube)

	def go_play_youtube (self):
		uri = self.go_get_uri()
		#self.ps = subprocess.Popen(('mpv', uri))
		subprocess.Popen(('mpv', uri))
		

class Indicator:
	app = None

	icon_name_on_win_activate = 'video'
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
		item = Gtk.MenuItem.new_with_label('About')
		item.connect('activate', self.on_show_about)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Test')
		item.connect('activate', self.on_test)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Activate (<Super>a)')
		item.connect('activate', self.on_activate_win)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Fullscreen (F11)')
		item.connect('activate', self.on_fullscreen_win)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Get Current Page URI')
		item.connect('activate', self.on_get_uri)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Load YouTube')
		item.connect('activate', self.on_load_youtube)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Load Google')
		item.connect('activate', self.on_load_google)
		menu.append(item)

		item = Gtk.MenuItem.new_with_label('Play YouTube (F1)')
		item.connect('activate', self.on_play_youtube)
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

	def on_get_uri(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_get_uri:')
			print('	menu_item:', menu_item)

		print('current_uri:', self.app.win.webview.go_get_uri())

	def on_load_google(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_load_google:')
			print('	menu_item:', menu_item)

		self.app.win.webview.go_load_google()

	def on_load_youtube(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_load_youtube:')
			print('	menu_item:', menu_item)

		self.app.win.webview.go_load_youtube()

	def on_play_youtube(self, menu_item):
		if self.app.is_debug:
			print('')
			print('on_play_youtube:')
			print('	menu_item:', menu_item)

		self.app.win.webview.go_play_youtube()

	def go_switch_icon_on_win_activate(self):
		self.indicator.set_icon(self.icon_name_on_win_activate)

	def go_switch_icon_on_win_deactivate(self):
		self.indicator.set_icon(self.icon_name_on_win_deactivate)


class Win:
	app = None
	box = None
	webview = None

	state_fullscreen = False
	state_activate = True

	keybind_accelerator_name_activate = '<Super>a'

	def __init__ (self):
		pass

	def init (self):
		self.init_win()
		self.init_keybind()

	def init_keybind(self):
		if self.app.is_debug:
			print('')
			print('init_keybind:')
			print('	keybind_accelerator_name_activate:', self.keybind_accelerator_name_activate)

		Keybinder.init()
		Keybinder.bind(self.keybind_accelerator_name_activate, self.on_key_activate_win)

	def init_win (self):
		self.win = win = Gtk.Window()

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.set_title
		win.set_title(self.app.title)
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.set_icon_name
		win.set_icon_name(self.app.icon_name)

		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		## keyboard key event
		win.connect('key-press-event', self.on_key_press)
		win.connect('key-release-event', self.on_key_release)

		self.box = box = Gtk.Box(spacing=6)
		win.add(box)

		self.webview = webview = WebView()
		webview.app = self.app
		webview.init()

		box.pack_start(webview.webview, True, True, 0)

		win.resize_to_geometry(600, 800)
		win.show_all()

	def on_key_activate_win(self, accelerator_name):
		if self.app.is_debug:
			print('')
			print('on_key_activate_win:')
			print('	accelerator_name:', accelerator_name)
		self.go_activate()

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

		## on press [F11]
		## if accelerator_label == 'F11':
		if accelerator_name == 'F11':
			self.go_switch_fullscreen()
			return True

		## on press [F1]
		if accelerator_name == 'F1':
			self.app.win.webview.go_play_youtube()
			return True

		return False

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

	def go_deactivate (self):
		self.set_state_activate(False)
		self.win.hide()
		self.app.indicator.go_switch_icon_on_win_deactivate()


class App:
	is_debug = True
	#is_debug = False

	name = 'DemoFullscreenAppindicatorWebkitApp'
	title = 'Demo Fullscreen Appindicator Webkit App'

	#icon_name = 'folder'
	#icon_name = 'image'
	#icon_name = 'video-display'
	icon_name = 'video'

	def __init__ (self):
		pass

	def init (self):

		self.win = win = Win()
		win.app = self
		win.init()

		self.indicator = indicator = Indicator()
		indicator.app = self
		indicator.init()

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

## https://wiki.gnome.org/Projects/PyGObject
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/
## https://lazka.github.io/pgi-docs/

## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## Gtk
## https://lazka.github.io/pgi-docs/#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_name
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.accelerator_get_label

## Gdk
## https://lazka.github.io/pgi-docs/#Gdk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gdk-3.0/classes.html

## AppIndicator3
## https://lazka.github.io/pgi-docs/#AppIndicator3-0.1
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes.html

## Keybinder
## https://lazka.github.io/pgi-docs/#Keybinder-3.0
## https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0
## https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0/functions.html

## subprocess
## https://docs.python.org/3/library/subprocess.html

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
