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
from gi.repository import GdkPixbuf
from gi.repository import GLib


gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as AppIndicator

gi.require_version('Keybinder', '3.0')
from gi.repository import Keybinder

gi.require_version('Vte', '2.91')
from gi.repository import Vte


import signal
import os
import stat

class Term:
	app = None
	win = None
	view = None
	term = None

	cmd = '/usr/bin/vim'

	path = ''

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_term()
		self.view = self.term

	def init_term (self):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.new
		self.term = term = Vte.Terminal()

		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.spawn_sync
		ok, pid = term.spawn_sync(
			Vte.PtyFlags.DEFAULT,
			os.environ['HOME'],
			[self.cmd, self.path],
			[],
			GLib.SpawnFlags.DO_NOT_REAP_CHILD,
			None,
			None,
		)

		print('ok:', ok)
		print('pid:', pid)

		if (not ok):
			return False

		term.watch_child(pid)

		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		term.connect('child-exited', self.on_child_exited);

		term.show_all()

	def on_child_exited(self, term, status):
		## https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited
		print('')
		print('on_child_exited:')
		print('	term:', term)
		print('	status:', status)

		self.win.destroy()


class Editor:
	app = None
	win = None
	term = None

	title = 'Vim'
	path = ''

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()

	def init_term (self):
		self.term = term = Term()
		term.app = self.app
		term.win = self.win
		term.path = self.path
		term.init()

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		self.init_term()
		win.add(self.term.view)

	def show (self):
		self.win.show_all()

	def on_close_win (self, win, evt):
		self.win.destroy()
		return False



class FileTree:
	app = None
	view = None

	scroll = None
	filetree = None

	model = None
	column = None

	column_head_title = 'File'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_filetree()
		self.init_scroll()
		self.view = self.scroll

	def init_scroll (self):
		self.scroll = scroll = Gtk.ScrolledWindow()
		scroll.add(self.filetree)

	def init_model (self):
		self.model = Gtk.TreeStore(str, str, GdkPixbuf.Pixbuf)

	def init_filetree (self):

		self.init_model()
		self.init_column()

		self.filetree = filetree = Gtk.TreeView()

		filetree.connect('row-expanded', self.on_row_expanded)
		filetree.connect('row-collapsed', self.on_row_collapsed)
		filetree.connect('row-activated', self.on_row_activated)

		filetree.connect('key-press-event', self.on_key_press_event)

		filetree.set_model(self.model)
		filetree.append_column(self.column)

	def init_column (self):
		self.column = column = Gtk.TreeViewColumn(self.column_head_title)

		cell_text = Gtk.CellRendererText()
		cell_img = Gtk.CellRendererPixbuf()

		column.pack_start(cell_img, False)
		column.pack_start(cell_text, True)

		column.add_attribute(cell_img, 'pixbuf', 2)
		column.add_attribute(cell_text, 'text', 0)

	def new_none_list (self):
		return [None, None, None]

	def load_path (self, path, parent=None):
		list_dir = []
		list_file = []
		list = None
		for node in os.scandir(path):
			if node.is_dir():
				list_dir.append(node)
			else:
				list_file.append(node)

		## https://docs.python.org/3/howto/sorting.html
		list_dir = sorted(list_dir, key=lambda node: node.name)
		list_file = sorted(list_file, key=lambda node: node.name)

		list = list_dir + list_file
		self.load_list(list, parent)


	def load_list (self, list, parent=None):
		iter = None
		model = self.model

		total = 0
		for node in list:
			total += 1
			##print(node.path);
			##print(type(node))

			if node.is_dir():
				icon = 'folder'
			else:
				icon = 'empty'

			icon = Gtk.IconTheme.get_default().load_icon(icon, 22, 0)
			iter = model.append(parent, [node.name, node.path, icon])

			if node.is_dir():
				model.append(iter, self.new_none_list())

		if total < 0:
			model.append(parent, self.new_none_list())


	def on_row_expanded (self, view, iter, path):
		print('')
		print('on_row_expanded:')
		print('	view:', view)
		print('	iter:', iter)
		print('	path:', path)

		model = view.get_model()

		file_path = model.get_value(iter, 1)
		print(file_path)

		self.load_path(file_path, iter)

		model.remove(model.iter_children(iter))

	def on_row_collapsed (self, view, iter, path):
		print('')
		print('on_row_collapsed:')
		print('	view:', view)
		print('	iter:', iter)
		print('	path:', path)

		model = view.get_model()

		child = model.iter_children(iter)

		while child:
			model.remove(child)
			child = model.iter_children(iter)

		model.append(iter, self.new_none_list())

	def on_row_activated (self, view, path, column):
		print('')
		print('on_row_activated:')
		print('	view:', view)
		print('	path:', path)
		print('	column:', column)

		model = view.get_model()
		iter = model.get_iter(path)
		file_path = model.get_value(iter, 1)

		file = os.stat(file_path)
		print('	file_path:', file_path)
		#print('	dir(file):', dir(file))

		is_folder = stat.S_ISDIR(file.st_mode)
		print(' is_folder:', is_folder)

		if is_folder:
			return True

		self.go_open_editor(file_path)


		return True

	def on_key_press_event(self, wgt, evt):
		print('on_key_press_event:')


	def go_open_editor(self, path):
		editor = Editor()
		editor.path = path
		editor.init()
		editor.show()


class Win:
	app = None
	win = None
	filetree = None

	title = 'Demo File Tree Open File By Vim App'

	state_fullscreen = False
	state_activate = True

	width = 600
	height = 800

	top = 200
	left = 200

	default_load_path = '/home'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()

	def init_filetree (self):
		self.filetree = filetree = FileTree()
		filetree.app = self.app
		filetree.init()
		filetree.load_path(self.default_load_path)

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)
		win.resize(self.width, self.height)
		#win.resize_to_geometry(self.width, self.height)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		## keyboard key event
		win.connect('key-press-event', self.on_key_press)
		win.connect('key-release-event', self.on_key_release)

		self.init_filetree()
		win.add(self.filetree.view)

		win.show_all()


	def on_close_win (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event

		self.go_deactivate()


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


		return self.app.keybind.handle_by_accelerator_name(accelerator_name)


	def on_key_release (self, win, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.key_release_event

		accelerator_name = Gtk.accelerator_name(evt.keyval, evt.state)
		accelerator_label = Gtk.accelerator_get_label(evt.keyval, evt.state)

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
		self.win.move(self.top, self.left)


class Indicator:
	app = None

	icon_name_on_win_activate = 'empty'
	icon_name_on_win_deactivate = 'folder'
	icon_name_btn_app_quit = 'application-exit'

	def prep (self, **kwds):
		self.app = kwds['app']

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
		print('on_test:')

	def on_show_about(self, menu_item):
		self.app.go_show_about()

	def on_quit_app(self, menu_item):
		self.app.go_quit()

	def on_activate_win(self, menu_item):
		self.app.win.go_activate()

	def on_fullscreen_win(self, menu_item):
		self.app.win.go_fullscreen()

	def go_switch_icon_on_win_activate(self):
		self.indicator.set_icon(self.icon_name_on_win_activate)

	def go_switch_icon_on_win_deactivate(self):
		self.indicator.set_icon(self.icon_name_on_win_deactivate)


class Keybind:
	app = None

	accelerator_name_activate = '<Super>a'
	accelerator_name_fullscreen = 'F11'
	accelerator_name_play_youtube = 'F1'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_keybind()

	def init_keybind(self):
		Keybinder.init()
		Keybinder.bind(self.accelerator_name_activate, self.on_key_activate_win)

	def on_key_activate_win(self, accelerator_name):
		self.app.win.go_switch_activate()

	def handle_by_accelerator_name(self, accelerator_name):
		## on press [F11]
		## if accelerator_label == 'F11':
		if accelerator_name == self.app.keybind.accelerator_name_fullscreen:
			self.app.win.go_switch_fullscreen()
			return True

		return False


class Signal:
	app = None

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_signal()

	def init_signal (self):
		## https://docs.python.org/3/library/signal.html
		## https://docs.python.org/2/library/signal.html
		signal.signal(signal.SIGINT, signal.SIG_DFL)


class App:

	#is_debug = True
	is_debug = False

	name = 'DemoFileTreeOpenFileByVimApp'

	signal = None
	keybind = None

	indicator = None
	win = None

	#def __init__ (self):
	#	pass

	def init (self):
		self.signal = signal = Signal()
		signal.app = self
		signal.init()

		self.keybind = keybind = Keybind()
		keybind.app = self
		keybind.init()

		self.win = win = Win()
		win.app = self
		win.init()

		self.indicator = indicator = Indicator()
		indicator.app = self
		indicator.init()

	def run (self):
		Gtk.main()

	def go_show_about(self):
		print('app.go_show_about:')

	def go_quit(self):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

def main ():
	app = App()
	app.init()
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
