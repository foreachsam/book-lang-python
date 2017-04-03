---
layout: page
title: Package - libglib2.0-0
description: >
  Package - libglib2.0-0
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libglib2.0-0.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libglib2.0-0

執行

``` sh
$ apt-cache show libglib2.0-0
```

執行

``` sh
$ apt-cache showsrc libglib2.0-0
```

執行

``` sh
$ apt-cache show libglib2.0-0 | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.17), libffi6 (>= 3.0.4), libpcre3, libselinux1 (>= 1.32), zlib1g (>= 1:1.2.2)
```

執行

``` sh
$ apt-cache showsrc libglib2.0-0 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: glib2.0
Binary: libglib2.0-0, libglib2.0-tests, libglib2.0-udeb, libglib2.0-bin, libglib2.0-dev, libglib2.0-0-dbg, libglib2.0-data, libglib2.0-doc, libgio-fam, libglib2.0-0-refdbg
Version: 2.48.0-1ubuntu4
```

執行

``` sh
$ dpkg -l libglib2.0-0
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libglib2.0-0:amd64              2.48.2-0ubuntu1      amd64                GLib library of C routines
```

執行

``` sh
$ dpkg -L libglib2.0-0 | sort
```

顯示

```
/.
/lib
/lib/x86_64-linux-gnu
/lib/x86_64-linux-gnu/libglib-2.0.so.0
/lib/x86_64-linux-gnu/libglib-2.0.so.0.4800.2
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/gio
/usr/lib/x86_64-linux-gnu/gio/modules
/usr/lib/x86_64-linux-gnu/glib-2.0
/usr/lib/x86_64-linux-gnu/glib-2.0/gio-querymodules
/usr/lib/x86_64-linux-gnu/glib-2.0/glib-compile-resources
/usr/lib/x86_64-linux-gnu/glib-2.0/glib-compile-schemas
/usr/lib/x86_64-linux-gnu/libgio-2.0.so.0
/usr/lib/x86_64-linux-gnu/libgio-2.0.so.0.4800.2
/usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0
/usr/lib/x86_64-linux-gnu/libgmodule-2.0.so.0.4800.2
/usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0
/usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0.4800.2
/usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0
/usr/lib/x86_64-linux-gnu/libgthread-2.0.so.0.4800.2
/usr/share
/usr/share/doc
/usr/share/doc/libglib2.0-0
/usr/share/doc/libglib2.0-0/AUTHORS
/usr/share/doc/libglib2.0-0/changelog.Debian.gz
/usr/share/doc/libglib2.0-0/copyright
/usr/share/doc/libglib2.0-0/NEWS.gz
/usr/share/doc/libglib2.0-0/NEWS.pre-1-3.gz
/usr/share/doc/libglib2.0-0/README.gz
/usr/share/glib-2.0
/usr/share/glib-2.0/schemas
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/libglib2.0-0
```
