#!/usr/bin/env python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

gi.require_version('Fcitx', '1.0')
from gi.repository import Fcitx

## https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes/InputMethod.html#Fcitx.InputMethod.new
im = Fcitx.InputMethod.new(Gio.BusType.SESSION, Gio.DBusProxyFlags.NONE, 0, None)
#im = Fcitx.InputMethod()

#print(dir(im))

im.restart()



## Fcitx
## https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0
## https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes.html

## Fcitx.InputMethod
## https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes/InputMethod.html
## https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes/InputMethod.html#Fcitx.InputMethod.restart


## http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/
## $ qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.Restart
