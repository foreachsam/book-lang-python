---
layout: page
title: Package - gir1.2-glib-2.0
description: >
  Package - gir1.2-glib-2.0
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/gir1.2-glib-2.0.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# gir1.2-glib-2.0

執行

``` sh
$ apt-cache show gir1.2-glib-2.0
```

執行

``` sh
$ apt-cache showsrc gir1.2-glib-2.0
```

執行

``` sh
$ apt-cache show gir1.2-glib-2.0 | grep '^Depends:'
```

顯示

```
Depends: libgirepository-1.0-1 (>= 1.45.4), libglib2.0-0 (>= 2.47.1)
```

執行

``` sh
$ apt-cache showsrc gir1.2-glib-2.0 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, gir1.2-glib-2.0, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```

執行

``` sh
$ dpkg -l gir1.2-glib-2.0
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-glib-2.0:amd64           1.46.0-3ubuntu1      amd64                Introspection data for GLib, GObject, Gio and GModule
```

執行

``` sh
$ dpkg -L gir1.2-glib-2.0 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/girepository-1.0
/usr/lib/x86_64-linux-gnu/girepository-1.0/Gio-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/GIRepository-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/GLib-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/GModule-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/GObject-2.0.typelib
/usr/share
/usr/share/doc
/usr/share/doc/gir1.2-glib-2.0
/usr/share/doc/gir1.2-glib-2.0/AUTHORS
/usr/share/doc/gir1.2-glib-2.0/changelog.Debian.gz
/usr/share/doc/gir1.2-glib-2.0/CONTRIBUTORS
/usr/share/doc/gir1.2-glib-2.0/copyright
/usr/share/doc/gir1.2-glib-2.0/NEWS.gz
/usr/share/doc/gir1.2-glib-2.0/README
/usr/share/doc/gir1.2-glib-2.0/TODO
```
