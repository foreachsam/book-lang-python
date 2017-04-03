---
layout: page
title: Package - gir1.2-freedesktop
description: >
  Package - gir1.2-freedesktop
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/gir1.2-freedesktop.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# gir1.2-freedesktop

執行

``` sh
$ apt-cache show gir1.2-freedesktop
```

執行

``` sh
$ apt-cache showsrc gir1.2-freedesktop
```

執行

``` sh
$ apt-cache show gir1.2-freedesktop | grep '^Depends:'
```

顯示

```
Depends: gir1.2-glib-2.0 (= 1.46.0-3ubuntu1), libgirepository-1.0-1 (>= 1.41.4-1)
```

執行

``` sh
$ apt-cache showsrc gir1.2-freedesktop | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, gir1.2-glib-2.0, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```

執行

``` sh
$ dpkg -l gir1.2-freedesktop
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-freedesktop:amd64        1.46.0-3ubuntu1      amd64                Introspection data for some FreeDesktop components
```

執行

``` sh
$ dpkg -L gir1.2-freedesktop | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/girepository-1.0
/usr/lib/x86_64-linux-gnu/girepository-1.0/cairo-1.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/DBus-1.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/DBusGLib-1.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/fontconfig-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/freetype2-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/GL-1.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/libxml2-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/xfixes-4.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/xft-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/xlib-2.0.typelib
/usr/lib/x86_64-linux-gnu/girepository-1.0/xrandr-1.3.typelib
/usr/share
/usr/share/doc
/usr/share/doc/gir1.2-freedesktop
/usr/share/doc/gir1.2-freedesktop/AUTHORS
/usr/share/doc/gir1.2-freedesktop/changelog.Debian.gz
/usr/share/doc/gir1.2-freedesktop/CONTRIBUTORS
/usr/share/doc/gir1.2-freedesktop/copyright
/usr/share/doc/gir1.2-freedesktop/NEWS.gz
/usr/share/doc/gir1.2-freedesktop/README
/usr/share/doc/gir1.2-freedesktop/TODO
```
