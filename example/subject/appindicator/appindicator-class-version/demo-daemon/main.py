#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator

import signal

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html

## AppIndicator3
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes.html


class App:
	app_name = 'DemoApp'
	icon_name_on_app_activate = 'folder'
	icon_name_on_app_deactivate = 'view-restore'
	icon_name_btn_app_quit = 'application-exit'

	def __init__(self):
		self.init_signal()
		self.init_menu()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)

	def init_menu(self):
		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html
		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html#Gtk.Menu.new
		self.menu = menu = Gtk.Menu()

		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html
		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html#Gtk.MenuItem.new
		item = Gtk.MenuItem.new_with_label('about')
		item.connect('activate', self.do_show_about)
		menu.append(item)

		#http://www.pygtk.org/pygtk2reference/gtk-stock-items.html
		#https://lazka.github.io/pgi-docs/Gtk-3.0/classes/Image.html#Gtk.Image.new_from_icon_name
		img = Gtk.Image.new_from_icon_name(self.icon_name_btn_app_quit, 16)
		## item = Gtk.MenuItem.new_with_label('quit')
		## https://lazka.github.io/pgi-docs/Gtk-3.0/classes/ImageMenuItem.html#Gtk.ImageMenuItem.new_with_label
		item = Gtk.ImageMenuItem.new_with_label('quit')
		#item.connect('activate', Gtk.main_quit)
		item.connect('activate', self.on_quit_app)
		item.set_image(img)
		menu.append(item)


		#print(dir(Gtk))
		#print(Gtk.STOCK_QUIT)


		## item = Gtk.MenuItem.new_with_label('quit')
		## http://www.pygtk.org/pygtk2reference/gtk-stock-items.html
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/constants.html#Gtk.STOCK_QUIT
		## The “Quit” item and icon.
		## Deprecated since version 3.10: Use named icon “application-exit” or the label “_Quit”.
		## item = Gtk.ImageMenuItem.new_from_stock(Gtk.STOCK_QUIT)
		item = Gtk.ImageMenuItem.new_from_stock(Gtk.STOCK_QUIT)
		#item.connect('activate', Gtk.main_quit)
		item.connect('activate', self.on_quit_app)
		menu.append(item)


		menu.show_all()

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html
		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.new
		# new (id, icon_name, category)
		self.indicator = indicator = AppIndicator.Indicator.new(
			self.app_name,
			self.icon_name_on_app_activate,
			AppIndicator.IndicatorCategory.APPLICATION_STATUS
		)

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_menu
		indicator.set_menu(menu)

		# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_status
		indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)
		#type(indicator)
		#<class 'gi.repository.AppIndicator3.Indicator'>

	def do_show_about(self, menu_item):
		print('')
		print('do_show_about:')
		print('	menu_item:', menu_item)

	def on_quit_app(self, menu_item):
		print('')
		print('on_quit_app:')
		print('	menu_item:', menu_item)
		Gtk.main_quit()

	def on_activate_app(self, menu_item):
		print('')
		print('on_activate_app:')
		print('	menu_item:', menu_item)
		self.do_show_app()
		self.do_switch_on_activate_icon()

	def do_show_app(self):
		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.show
		# self.win.show();
		# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.present
		self.win.present()


	def do_hide_app(self):
		self.win.hide()

	def do_switch_on_deactivate_icon(self):
		# https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
		self.indicator.set_icon(self.icon_name_on_app_deactivate)

	def do_switch_on_activate_icon(self):
		# https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html
		self.indicator.set_icon(self.icon_name_on_app_activate)

	def run(self):
		Gtk.main()

def main():
	app = App()
	app.run()

if __name__ == '__main__':
	main()
