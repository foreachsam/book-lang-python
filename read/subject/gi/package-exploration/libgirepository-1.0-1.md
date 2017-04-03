---
layout: page
title: Package - libgirepository-1.0-1
description: >
  Package - libgirepository-1.0-1
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libgirepository-1.0-1.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libgirepository-1.0-1

執行

``` sh
$ apt-cache show libgirepository-1.0-1
```

執行

``` sh
$ apt-cache showsrc libgirepository-1.0-1
```

執行

``` sh
$ apt-cache show libgirepository-1.0-1 | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.14), libffi6 (>= 3.0.4), libglib2.0-0 (>= 2.45.3)
```

執行

``` sh
$ apt-cache showsrc libgirepository-1.0-1 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, libgirepository-1.0-1, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```

執行

``` sh
$ dpkg -l libgirepository-1.0-1
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libgirepository-1.0-1:amd64     1.46.0-3ubuntu1      amd64                Library for handling GObject introspection data (runtime library)
```

執行

``` sh
$ dpkg -L libgirepository-1.0-1 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/libgirepository-1.0.so.1
/usr/lib/x86_64-linux-gnu/libgirepository-1.0.so.1.0.0
/usr/share
/usr/share/doc
/usr/share/doc/libgirepository-1.0-1
/usr/share/doc/libgirepository-1.0-1/AUTHORS
/usr/share/doc/libgirepository-1.0-1/changelog.Debian.gz
/usr/share/doc/libgirepository-1.0-1/CONTRIBUTORS
/usr/share/doc/libgirepository-1.0-1/copyright
/usr/share/doc/libgirepository-1.0-1/NEWS.gz
/usr/share/doc/libgirepository-1.0-1/README
/usr/share/doc/libgirepository-1.0-1/TODO
```
