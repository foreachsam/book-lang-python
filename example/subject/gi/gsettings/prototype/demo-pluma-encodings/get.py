#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.mate.pluma')

## print(settings)
## print(dir(settings))
## print(type(settings))

auto_detected_encodings = settings.get_strv('auto-detected-encodings')

print(auto_detected_encodings)
## print(dir(auto_detected_encodings))
## print(type(auto_detected_encodings))

## http://foreachsam.github.io/book-util-gsettings/book/content/case/pluma/encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
