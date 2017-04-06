---
layout: page
title: Python Gtk Keybinder
description: >
  Python Gtk Keybinder
date: 2017-04-06 17:13:26 +0800
source_url: '/read/subject/gtk/keybinder/index.md'
parent:
  title: Python Gtk+ 3
  url: '/read/subject/gtk/'
---

# Keybinder


## 範例

### 整合範例

* [fullscreen/composite/demo-appindicator-webkit](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/fullscreen/composite/demo-appindicator-webkit/main.py) ([Fullscreen](https://foreachsam.github.io/book-lang-python/read/subject/gtk/fullscreen/))
* [fullscreen/composite/demo-appindicator-terminal](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/fullscreen/composite/demo-appindicator-terminal/main.py) ([Fullscreen](https://foreachsam.github.io/book-lang-python/read/subject/gtk/fullscreen/))


## API

### Gtk-3

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html)

### Keybinder

* [https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0](https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0)
* [https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0/functions.html](https://lazka.github.io/pgi-docs/index.html#Keybinder-3.0/functions.html)


## Package

### 探索步驟

執行

``` sh
$ apt-cache search gir | grep keybinder
```

顯示

``` sh
gir1.2-keybinder-0.0 - registers global key bindings for applications - introspection data
gir1.2-keybinder-3.0 - registers global key bindings for applications - Gtk+3 - typelib
```

執行

``` sh
$ apt-cache show gir1.2-keybinder-3.0
```

執行

``` sh
$ apt-cache showsrc gir1.2-keybinder-3.0
```

執行

``` sh
$ apt-cache show gir1.2-keybinder-3.0 | grep '^Depends:'
```

顯示

```
Depends: gir1.2-glib-2.0, libkeybinder-3.0-0 (>= 0.3.0)
```

執行

``` sh
$ apt-cache showsrc gir1.2-keybinder-3.0 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: keybinder-3.0
Binary: libkeybinder-3.0-0, libkeybinder-3.0-dev, gir1.2-keybinder-3.0, keybinder-3.0-doc
Version: 0.3.1-1
```

執行

``` sh
$ dpkg -l gir1.2-keybinder-3.0
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-keybinder-3.0            0.3.1-1              amd64                registers global key bindings for applications - Gtk+3 - typelib
```

執行

``` sh
$ dpkg -L gir1.2-keybinder-3.0 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/girepository-1.0
/usr/lib/girepository-1.0/Keybinder-3.0.typelib
/usr/share
/usr/share/doc
/usr/share/doc/gir1.2-keybinder-3.0
/usr/share/doc/gir1.2-keybinder-3.0/changelog.Debian.gz
/usr/share/doc/gir1.2-keybinder-3.0/copyright
```


### 套件列表

* [gir1.2-keybinder-3.0](http://packages.ubuntu.com/xenial/gir1.2-keybinder-3.0)
* [libkeybinder-3.0-0](http://packages.ubuntu.com/xenial/libkeybinder-3.0-0)
* [libkeybinder-3.0-dev](http://packages.ubuntu.com/xenial/libkeybinder-3.0-dev)
* [keybinder-3.0-doc](http://packages.ubuntu.com/xenial/keybinder-3.0-doc)
