#!/usr/bin/env sh

## http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/

im_name=$(qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.GetIMAddon chewing)
echo $im_name

#echo $(qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.GetIMAddon chewing)
