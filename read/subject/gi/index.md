---
layout: page
title: Python PyGObject (PyGI)
description: >
  Python PyGObject (PyGI)
date: 2017-04-03 01:47:04 +0800
source_url: '/read/subject/gi/index.md'
---

# Python PyGObject (PyGI)

## Subject

* [Fcitx](fcitx)
* [Gsettings](gsettings)


## Document

### Python GObject

* [PyGObject (aka PyGI)](https://wiki.gnome.org/Projects/PyGObject)
* [The Python GTK+ 3 Tutorial](http://python-gtk-3-tutorial.readthedocs.io/en/latest/index.html)
* [Python GObject Introspection API Reference](https://lazka.github.io/pgi-docs/index.html)
* GitHub / Gnome / [pygobject](https://github.com/GNOME/pygobject.git)
* [GNOME Developer Platform Demos](https://developer.gnome.org/gnome-devel-demos/stable/index.html.en) / [Tutorials, code samples and platform demos in Python](https://developer.gnome.org/gnome-devel-demos/stable/py.html.en)


## 套件

* [python3-gi](package-exploration/python3-gi)
* [gobject-introspection](package-exploration/gobject-introspection)
* [gir1.2-glib-2.0](package-exploration/gir1.2-glib-2.0)
* [gir1.2-freedesktop](package-exploration/gir1.2-freedesktop)
* [libgirepository-1.0-1](package-exploration/libgirepository-1.0-1)
* [libgirepository1.0-dev](package-exploration/libgirepository1.0-dev)
* [libgirepository1.0-doc](package-exploration/libgirepository1.0-doc)
* [libglib2.0-0](package-exploration/libglib2.0-0)
* [libglib2.0-bin](package-exploration/libglib2.0-bin)
* [libglib2.0-dev](package-exploration/libglib2.0-dev)
* [libglib2.0-doc](package-exploration/libglib2.0-doc)
* [libffi6](package-exploration/libffi6)
* [libffi-dev](package-exploration/libffi-dev)


### 套件探索

執行

``` sh
$ apt-cache search gir | less
```

執行

``` sh
$ apt-cache search gir1.2 | less
```

執行

``` sh
$ apt-cache search gir | grep fcitx
```

顯示

```
gir1.2-fcitx-1.0 - Flexible Input Method Framework - GObject introspection
```

執行

``` sh
$ dpkg -l gir1.2-fcitx-1.0
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-fcitx-1.0                1:4.2.9.1-1ubuntu1.1 amd64                Flexible Input Method Framework - GObject introspection
```

執行

``` sh
$ dpkg -l | grep gir | grep fcitx
```

顯示

```
ii  gir1.2-fcitx-1.0                                     1:4.2.9.1-1ubuntu1.16.04.2                    amd64        Flexible Input Method Framework - GObject introspection
```

執行

``` sh
$ dpkg -L gir1.2-fcitx-1.0 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/girepository-1.0
/usr/lib/x86_64-linux-gnu/girepository-1.0/Fcitx-1.0.typelib
/usr/share
/usr/share/doc
/usr/share/doc/gir1.2-fcitx-1.0
/usr/share/doc/gir1.2-fcitx-1.0/changelog.Debian.gz
/usr/share/doc/gir1.2-fcitx-1.0/copyright
/usr/share/gir-1.0
/usr/share/gir-1.0/Fcitx-1.0.gir
```

## 路徑

* /usr/lib/x86_64-linux-gnu/girepository-1.0
* /usr/share/gir-1.0

### 路徑探索

執行

``` sh
$ ls /usr/share/gir-1.0/
```

執行

``` sh
$ ls /usr/lib/x86_64-linux-gnu/girepository-1.0
```

執行

``` sh
$ dpkg -S /usr/share/gir-1.0/
```

執行

``` sh
$ dpkg -S /usr/lib/x86_64-linux-gnu/girepository-1.0
```
