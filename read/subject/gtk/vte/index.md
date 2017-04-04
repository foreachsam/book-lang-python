---
layout: page
title: Python Gtk Vte
description: >
  Python Gtk Vte
date: 2017-04-04 21:21:56 +0800
source_url: '/read/subject/gtk/vte/index.md'
parent:
  title: Python Gtk+ 3
  url: '/read/subject/gtk/'
---


## 範例

### Prototype

* [demo-basic](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/prototype/demo-basic/main.py)

### Composite

* [demo-basic](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/composite/demo-basic/main.py)
* [demo-basic-on-child-exited](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/composite/demo-basic-on-child-exited/main.py)


### Extend

* [demo-basic](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/extend/demo-basic/main.py)
* [demo-basic-on-child-exited](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/extend/demo-basic-on-child-exited/main.py)
* [demo-basic-do-child-exited](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/vte/extend/demo-basic-do-child-exited/main.py)


## API

### Gtk-3

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html)

### Gtk.Window

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.signals.delete_event)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.do_delete_event](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Widget.html#Gtk.Widget.do_delete_event)

### Gtk.main_quit

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/functions.html#Gtk.main_quit)

### Vte

* [https://lazka.github.io/pgi-docs/index.html#Vte-2.91](https://lazka.github.io/pgi-docs/index.html#Vte-2.91)
* [https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes.html](https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes.html)

### Vte.Terminal

* [https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html](https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html)
* [https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited](https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.signals.child_exited)
* [https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.do_child_exited](https://lazka.github.io/pgi-docs/index.html#Vte-2.91/classes/Terminal.html#Vte.Terminal.do_child_exited)


## Package

### 探索步驟

執行

``` sh
$ apt-cache search gir | grep vte
```

顯示

``` sh
gir1.2-vte-2.91 - GObject introspection data for the VTE library
```

執行

``` sh
$ apt-cache show gir1.2-vte-2.91
```

執行

``` sh
$ apt-cache showsrc gir1.2-vte-2.91
```

執行

``` sh
$ apt-cache show gir1.2-vte-2.91 | grep '^Depends:'
```

顯示

```
Depends: gir1.2-gtk-3.0, gir1.2-pango-1.0, libgirepository-1.0-1 (>= 1.41.4-1), libvte-2.91-0 (>= 0.40.2)
```

執行

``` sh
$ apt-cache showsrc gir1.2-vte-2.91 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: vte2.91
Binary: libvte-2.91-0, libvte-2.91-0-udeb, gir1.2-vte-2.91, libvte-2.91-dev, libvte-2.91-common, libvte-2.91-doc
Version: 0.42.5-1ubuntu1
```

執行

``` sh
$ dpkg -l gir1.2-vte-2.91
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-vte-2.91:amd64           0.42.5-1ubuntu1      amd64                GObject introspection data for the VTE library
```

執行

``` sh
$ dpkg -L gir1.2-vte-2.91 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/girepository-1.0
/usr/lib/x86_64-linux-gnu/girepository-1.0/Vte-2.91.typelib
/usr/share
/usr/share/doc
/usr/share/doc/gir1.2-vte-2.91
/usr/share/doc/gir1.2-vte-2.91/AUTHORS
/usr/share/doc/gir1.2-vte-2.91/changelog.Debian.gz
/usr/share/doc/gir1.2-vte-2.91/copyright
/usr/share/doc/gir1.2-vte-2.91/NEWS.gz
/usr/share/doc/gir1.2-vte-2.91/README
```


### 套件列表

* [gir1.2-vte-2.91](http://packages.ubuntu.com/xenial/gir1.2-vte-2.91)
* [libvte-2.91-0](http://packages.ubuntu.com/xenial/libvte-2.91-0)
* [libvte-2.91-dev](http://packages.ubuntu.com/xenial/libvte-2.91-dev)
* [libvte-2.91-doc](http://packages.ubuntu.com/xenial/libvte-2.91-doc)
* [libvte-2.91-common](http://packages.ubuntu.com/xenial/libvte-2.91-common)
