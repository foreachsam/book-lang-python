---
layout: page
title: Python Gtk Webkit
description: >
  Python Gtk Webkit
date: 2017-03-29 14:04:21 +0800
source_url: '/read/subject/gtk/webkit/index.md'
---


## 範例

### Prototype Version

* [webkit-prototype-version](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/webkit/webkit-prototype-version/main.py)

### 整合範例

* [fullscreen/composite/demo-appindicator-webkit](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gtk/fullscreen/composite/demo-appindicator-webkit/main.py) ([Fullscreen](https://foreachsam.github.io/book-lang-python/read/subject/gtk/fullscreen/))


## API

### Gtk-3

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html)

### Gtk.Window

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Window.html)


### WebKit2

* [https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0](https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0)
* [https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes.html](https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes.html)

### WebKit2.WebView

* [https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes/WebView.html](https://lazka.github.io/pgi-docs/index.html#WebKit2-4.0/classes/WebView.html)


## Package

* [libwebkit2gtk-4.0-dev](http://packages.ubuntu.com/xenial/libwebkit2gtk-4.0-dev)
* [libwebkit2gtk-4.0-37](http://packages.ubuntu.com/xenial/libwebkit2gtk-4.0-37)
* [gir1.2-webkit2-4.0](http://packages.ubuntu.com/xenial/gir1.2-webkit2-4.0)


執行

``` sh
$ apt-cache search webkit
```

執行下面指令，安裝「[libwebkit2gtk-4.0-dev](http://packages.ubuntu.com/xenial/libwebkit2gtk-4.0-dev)」

``` sh
$ sudo apt-get install libwebkit2gtk-4.0-dev
```

執行

``` sh
$ dpkg -l '*webkit*'
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
un  gir1.0-webkit-3.0               <none>               <none>               (no description available)
ii  gir1.2-webkit-3.0:amd64         2.4.11-0ubuntu0.1    amd64                Web content engine library for GTK+ - GObject introspection data
ii  gir1.2-webkit2-3.0:amd64        2.4.11-0ubuntu0.1    amd64                WebKit2 API layer for WebKitGTK+ - GObject introspection data
ii  gir1.2-webkit2-4.0:amd64        2.14.5-0ubuntu0.16.0 amd64                Web content engine library for GTK+ - GObject introspection data
ii  libkdewebkit5                   4:4.14.16-0ubuntu3.1 amd64                KDE WebKit Library
un  libqt4-webkit                   <none>               <none>               (no description available)
ii  libqt5webkit5:amd64             5.5.1+dfsg-2ubuntu1  amd64                Web content engine library for Qt
ii  libqtwebkit4:amd64              2.3.2-0ubuntu11      amd64                Web content engine library for Qt
ii  libswt-webkit-gtk-3-jni         3.8.2-3              amd64                Standard Widget Toolkit for GTK+ WebKit JNI library
un  libwebkit2gtk-3.0-0             <none>               <none>               (no description available)
ii  libwebkit2gtk-3.0-25:amd64      2.4.11-0ubuntu0.1    amd64                WebKit2 API layer for WebKitGTK+
ii  libwebkit2gtk-4.0-37:amd64      2.14.5-0ubuntu0.16.0 amd64                Web content engine library for GTK+
ii  libwebkit2gtk-4.0-37-gtk2:amd64 2.14.5-0ubuntu0.16.0 amd64                Web content engine library for GTK+ - GTK+2 plugin process
ii  libwebkit2gtk-4.0-dev:amd64     2.14.5-0ubuntu0.16.0 amd64                Web content engine library for GTK+ - development files
ii  libwebkit2gtk-4.0-doc           2.14.5-0ubuntu0.16.0 all                  Web content engine library for GTK+ - documentation
ii  libwebkitgtk-1.0-0:amd64        2.4.11-0ubuntu0.1    amd64                Web content engine library for GTK+
ii  libwebkitgtk-1.0-common         2.4.11-0ubuntu0.1    all                  Web content engine library for GTK+ - data files
ii  libwebkitgtk-3.0-0:amd64        2.4.11-0ubuntu0.1    amd64                Web content engine library for GTK+
ii  libwebkitgtk-3.0-common         2.4.11-0ubuntu0.1    all                  Web content engine library for GTK+ - data files
ii  python-pyqt5.qtwebkit           5.5.1+dfsg-3ubuntu4  amd64                Python 2 bindings for Qt5's WebKit module
ii  python-pyside.qtwebkit          1.2.2-2build2        amd64                Qt 4 WebKit module - Python bindings
un  python2.7-pyside.qtwebkit       <none>               <none>               (no description available)
ii  python3-pyqt5.qtwebkit          5.5.1+dfsg-3ubuntu4  amd64                Python 3 bindings for Qt5's WebKit module
un  qml-module-qtwebkit             <none>               <none>               (no description available)
un  qtwebkit5-doc-html              <none>               <none>               (no description available)

```

執行

``` sh
$ apt-cache showsrc gir1.2-webkit2-4.0 | grep '^Binary:'
```

顯示

```
$ Binary: libjavascriptcoregtk-4.0-18, libjavascriptcoregtk-4.0-dev, libjavascriptcoregtk-4.0-bin, gir1.2-javascriptcoregtk-4.0, libwebkit2gtk-4.0-37, libwebkit2gtk-4.0-dev, libwebkit2gtk-4.0-doc, gir1.2-webkit2-4.0, libwebkit2gtk-4.0-37-gtk2
```

執行

``` sh
$ apt-cache show libwebkit2gtk-4.0-dev
```

執行

``` sh
$ apt-cache show gir1.2-webkit2-4.0
```
