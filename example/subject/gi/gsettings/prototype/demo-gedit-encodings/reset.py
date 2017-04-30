#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.gnome.gedit.preferences.encodings')

settings.reset('candidate-encodings')

## https://foreachsam.github.io/book-util-gsettings/book/content/case/gedit/preferences-encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
