#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.gnome.gedit.preferences.encodings')

## print(settings)
## print(dir(settings))
## print(type(settings))

candidate_encodings = settings.get_strv('candidate-encodings')

print(candidate_encodings)
## print(dir(candidate_encodings))
## print(type(candidate_encodings))

## https://foreachsam.github.io/book-util-gsettings/book/content/case/gedit/preferences-encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
