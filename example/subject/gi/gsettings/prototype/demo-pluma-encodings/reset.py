#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.mate.pluma')

settings.reset('auto-detected-encodings')

## http://foreachsam.github.io/book-util-gsettings/book/content/case/pluma/encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
