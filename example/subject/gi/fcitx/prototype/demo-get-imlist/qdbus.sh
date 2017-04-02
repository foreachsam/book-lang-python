#!/usr/bin/env sh

## http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/
qdbus --literal org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.IMList 
