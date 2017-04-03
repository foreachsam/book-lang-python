---
layout: page
title: Package - libgirepository1.0-dev
description: >
  Package - libgirepository1.0-dev
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libgirepository1.0-dev.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libgirepository1.0-dev

執行

``` sh
$ apt-cache show libgirepository1.0-dev
```

執行

``` sh
$ apt-cache showsrc libgirepository1.0-dev
```

執行

``` sh
$ apt-cache show libgirepository1.0-dev | grep '^Depends:'
```

顯示

```
Depends: libgirepository-1.0-1 (= 1.46.0-3ubuntu1), gobject-introspection (= 1.46.0-3ubuntu1), gir1.2-glib-2.0 (= 1.46.0-3ubuntu1), gir1.2-freedesktop (= 1.46.0-3ubuntu1), libglib2.0-dev (>= 2.44.0), libffi-dev
```

執行

``` sh
$ apt-cache showsrc libgirepository1.0-dev | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, libgirepository1.0-dev, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```

執行

``` sh
$ dpkg -l libgirepository1.0-dev
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libgirepository1.0-dev          1.46.0-3ubuntu1      amd64                Library for handling GObject introspection data (development files)
```

執行

``` sh
$ dpkg -L libgirepository1.0-dev | sort
```

顯示

```
/.
/usr
/usr/include
/usr/include/gobject-introspection-1.0
/usr/include/gobject-introspection-1.0/giarginfo.h
/usr/include/gobject-introspection-1.0/gibaseinfo.h
/usr/include/gobject-introspection-1.0/gicallableinfo.h
/usr/include/gobject-introspection-1.0/giconstantinfo.h
/usr/include/gobject-introspection-1.0/gienuminfo.h
/usr/include/gobject-introspection-1.0/gifieldinfo.h
/usr/include/gobject-introspection-1.0/gifunctioninfo.h
/usr/include/gobject-introspection-1.0/giinterfaceinfo.h
/usr/include/gobject-introspection-1.0/giobjectinfo.h
/usr/include/gobject-introspection-1.0/gipropertyinfo.h
/usr/include/gobject-introspection-1.0/giregisteredtypeinfo.h
/usr/include/gobject-introspection-1.0/girepository.h
/usr/include/gobject-introspection-1.0/girffi.h
/usr/include/gobject-introspection-1.0/gisignalinfo.h
/usr/include/gobject-introspection-1.0/gistructinfo.h
/usr/include/gobject-introspection-1.0/gitypeinfo.h
/usr/include/gobject-introspection-1.0/gitypelib.h
/usr/include/gobject-introspection-1.0/gitypes.h
/usr/include/gobject-introspection-1.0/giunioninfo.h
/usr/include/gobject-introspection-1.0/giversionmacros.h
/usr/include/gobject-introspection-1.0/givfuncinfo.h
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/libgirepository-1.0.a
/usr/lib/x86_64-linux-gnu/libgirepository-1.0.so
/usr/lib/x86_64-linux-gnu/pkgconfig
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-introspection-1.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-introspection-no-export-1.0.pc
/usr/share
/usr/share/doc
/usr/share/doc/libgirepository1.0-dev
/usr/share/doc/libgirepository1.0-dev/AUTHORS
/usr/share/doc/libgirepository1.0-dev/changelog.Debian.gz
/usr/share/doc/libgirepository1.0-dev/CONTRIBUTORS
/usr/share/doc/libgirepository1.0-dev/copyright
/usr/share/doc/libgirepository1.0-dev/NEWS.gz
/usr/share/doc/libgirepository1.0-dev/README
/usr/share/doc/libgirepository1.0-dev/TODO
/usr/share/gir-1.0
/usr/share/gir-1.0/cairo-1.0.gir
/usr/share/gir-1.0/DBus-1.0.gir
/usr/share/gir-1.0/DBusGLib-1.0.gir
/usr/share/gir-1.0/fontconfig-2.0.gir
/usr/share/gir-1.0/freetype2-2.0.gir
/usr/share/gir-1.0/Gio-2.0.gir
/usr/share/gir-1.0/GIRepository-2.0.gir
/usr/share/gir-1.0/GL-1.0.gir
/usr/share/gir-1.0/GLib-2.0.gir
/usr/share/gir-1.0/GModule-2.0.gir
/usr/share/gir-1.0/GObject-2.0.gir
/usr/share/gir-1.0/libxml2-2.0.gir
/usr/share/gir-1.0/win32-1.0.gir
/usr/share/gir-1.0/xfixes-4.0.gir
/usr/share/gir-1.0/xft-2.0.gir
/usr/share/gir-1.0/xlib-2.0.gir
/usr/share/gir-1.0/xrandr-1.3.gir
```

執行

``` sh
$ dpkg -L libgirepository1.0-dev | grep pc
```

顯示

```
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-introspection-no-export-1.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-introspection-1.0.pc
```

根據「/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-introspection-1.0.pc」，

執行

``` sh
$ pkg-config --cflags --libs gobject-introspection-1.0
```

顯示

```
-pthread -I/usr/include/gobject-introspection-1.0 -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lgirepository-1.0 -lgobject-2.0 -lglib-2.0
```
