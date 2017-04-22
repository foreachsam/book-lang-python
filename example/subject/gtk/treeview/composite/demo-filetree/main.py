#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf


import os
import stat
import signal

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
		print('	dir(file):', dir(file))
		print(' is_folder:', stat.S_ISDIR(file.st_mode))

		return True

	def on_key_press_event(self, wgt, evt):
		print('on_key_press_event:')


class Win:
	app = None
	win = None
	tree = None

	title = 'Demo File Tree'
	width = 600
	height = 800

	default_load_path = '/home'

	def prep (self, **kwds):
		self.app = kwds['app']

	def init (self):
		self.init_win()

	def init_filetree (self):
		self.filetree = filetree = FileTree()
		filetree.init()
		filetree.load_path(self.default_load_path)

	def init_win (self):
		self.win = win = Gtk.Window()

		win.set_title(self.title)
		win.resize(self.width, self.height)

		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event
		#win.connect('delete-event', Gtk.main_quit)
		win.connect('delete-event', self.on_close_win)

		self.init_filetree()
		win.add(self.filetree.view)

		win.show_all()

	def on_close_win (self, wgt, evt):
		## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit
		Gtk.main_quit()

		return True

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
	def init (self):
		self.signal = signal = Signal()
		signal.app = self
		signal.init()

		self.win = win = Win()
		win.app = self
		win.init()

	def run (self):
		Gtk.main()

def main ():
	app = App()
	app.init()
	app.run()

if __name__ == '__main__':
	main()

## Tutorial
## http://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

## Gtk
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize
## https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html#Gtk.Window.resize_to_geometry

## Gtk.TreeView
## https://lazka.github.io/pgi-docs/#Gtk-3.0/classes/TreeView.html

## os
## https://docs.python.org/3/library/os.html
## https://docs.python.org/3/library/os.html#os.scandir

## stat
## https://docs.python.org/3/library/stat.html
