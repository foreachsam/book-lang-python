#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.gnome.gedit.preferences.encodings')

candidate_encodings = ['UTF-8', 'BIG5', 'BIG5-HKSCS', 'EUC-TW', 'GB18030', 'GB2312', 'GBK', 'CURRENT', 'ISO-8859-15', 'UTF-16']

settings.set_strv('candidate-encodings', candidate_encodings)

## https://foreachsam.github.io/book-util-gsettings/book/content/case/gedit/preferences-encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
