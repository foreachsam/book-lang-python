#!/usr/bin/env python3

from gi.repository import Gio

settings = Gio.Settings('org.mate.pluma')

auto_detected_encodings = ['UTF-8', 'BIG5', 'BIG5-HKSCS', 'EUC-TW', 'GB18030', 'GB2312', 'GBK', 'CURRENT', 'ISO-8859-15', 'UTF-16']

settings.set_strv('auto-detected-encodings', auto_detected_encodings)

## http://foreachsam.github.io/book-util-gsettings/book/content/case/pluma/encodings/
## https://lazka.github.io/pgi-docs/#Gio-2.0/classes/Settings.html
