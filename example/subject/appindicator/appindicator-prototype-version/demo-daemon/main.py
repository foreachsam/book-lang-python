#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html

## AppIndicator3
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/
## https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes.html

# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html
# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html#Gtk.Menu.new
menu = Gtk.Menu()

# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html
# https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html#Gtk.MenuItem.new
item = Gtk.MenuItem.new_with_label('quit')
menu.append(item)
item.connect('activate', Gtk.main_quit)
menu.show_all()

# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html
# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.new
# new (id, icon_name, category)
indicator = AppIndicator.Indicator.new(
	'DemoApp',
	'folder',
	AppIndicator.IndicatorCategory.APPLICATION_STATUS
)

# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_menu
indicator.set_menu(menu)

# https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html#AppIndicator3.Indicator.set_status
indicator.set_status(AppIndicator.IndicatorStatus.ACTIVE)


#type(indicator)
#<class 'gi.repository.AppIndicator3.Indicator'>


Gtk.main()
