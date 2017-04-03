---
layout: page
title: Package - libgirepository1.0-doc
description: >
  Package - libgirepository1.0-doc
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libgirepository1.0-doc.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libgirepository1.0-doc

執行

``` sh
$ apt-cache show libgirepository1.0-doc
```

執行

``` sh
$ apt-cache showsrc libgirepository1.0-doc
```

執行

``` sh
$ apt-cache show libgirepository1.0-doc | grep '^Depends:'
```

沒有顯示


執行

``` sh
$ apt-cache showsrc libgirepository1.0-doc | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, libgirepository1.0-doc, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```

執行

``` sh
$ dpkg -l libgirepository1.0-doc
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libgirepository1.0-doc          1.46.0-3ubuntu1      all                  Library for handling GObject introspection data (documentation)
```

執行

``` sh
$ dpkg -L libgirepository1.0-doc | sort
```

顯示

```
/.
/usr
/usr/share
/usr/share/doc
/usr/share/doc/libgirepository1.0-doc
/usr/share/doc/libgirepository1.0-doc/AUTHORS
/usr/share/doc/libgirepository1.0-doc/changelog.Debian.gz
/usr/share/doc/libgirepository1.0-doc/CONTRIBUTORS
/usr/share/doc/libgirepository1.0-doc/copyright
/usr/share/doc/libgirepository1.0-doc/NEWS.gz
/usr/share/doc/libgirepository1.0-doc/README
/usr/share/doc/libgirepository1.0-doc/TODO
/usr/share/gtk-doc
/usr/share/gtk-doc/html
/usr/share/gtk-doc/html/gi
/usr/share/gtk-doc/html/gi/annotation-glossary.html
/usr/share/gtk-doc/html/gi/api-index-1-29-0.html
/usr/share/gtk-doc/html/gi/api-index-1-29-17.html
/usr/share/gtk-doc/html/gi/api-index-1-30-1.html
/usr/share/gtk-doc/html/gi/api-index-1-34.html
/usr/share/gtk-doc/html/gi/api-index-1-35-8.html
/usr/share/gtk-doc/html/gi/api-index-deprecated.html
/usr/share/gtk-doc/html/gi/api-index-full.html
/usr/share/gtk-doc/html/gi/ch01.html
/usr/share/gtk-doc/html/gi/ch03.html
/usr/share/gtk-doc/html/gi/gi-building.html
/usr/share/gtk-doc/html/gi/gi-common-types.html
/usr/share/gtk-doc/html/gi/gi.devhelp2
/usr/share/gtk-doc/html/gi/gi-GIArgInfo.html
/usr/share/gtk-doc/html/gi/gi-GIBaseInfo.html
/usr/share/gtk-doc/html/gi/gi-GICallableInfo.html
/usr/share/gtk-doc/html/gi/gi-GICallbackInfo.html
/usr/share/gtk-doc/html/gi/gi-GIConstantInfo.html
/usr/share/gtk-doc/html/gi/gi-GIEnumInfo.html
/usr/share/gtk-doc/html/gi/gi-GIFieldInfo.html
/usr/share/gtk-doc/html/gi/gi-GIFunctionInfo.html
/usr/share/gtk-doc/html/gi/gi-GIInterfaceInfo.html
/usr/share/gtk-doc/html/gi/gi-GIObjectInfo.html
/usr/share/gtk-doc/html/gi/gi-GIPropertyInfo.html
/usr/share/gtk-doc/html/gi/gi-GIRegisteredTypeInfo.html
/usr/share/gtk-doc/html/gi/gi-girffi.html
/usr/share/gtk-doc/html/gi/gi-gir-reference.html
/usr/share/gtk-doc/html/gi/gi-GISignalInfo.html
/usr/share/gtk-doc/html/gi/gi-GIStructInfo.html
/usr/share/gtk-doc/html/gi/gi-GITypeInfo.html
/usr/share/gtk-doc/html/gi/gi-gitypelib.html
/usr/share/gtk-doc/html/gi/gi-GITypelib.html
/usr/share/gtk-doc/html/gi/gi-GIUnionInfo.html
/usr/share/gtk-doc/html/gi/gi-GIValueInfo.html
/usr/share/gtk-doc/html/gi/gi-GIVFuncInfo.html
/usr/share/gtk-doc/html/gi/gi.html
/usr/share/gtk-doc/html/gi/gi-programming.html
/usr/share/gtk-doc/html/gi/GIRepository.html
/usr/share/gtk-doc/html/gi/gi-struct-hierarchy.html
/usr/share/gtk-doc/html/gi/gi-typelib.html
/usr/share/gtk-doc/html/gi/home.png
/usr/share/gtk-doc/html/gi/index.html
/usr/share/gtk-doc/html/gi/index.sgml
/usr/share/gtk-doc/html/gi/left-insensitive.png
/usr/share/gtk-doc/html/gi/left.png
/usr/share/gtk-doc/html/gi/overview.html
/usr/share/gtk-doc/html/gi/overview.png
/usr/share/gtk-doc/html/gi/right-insensitive.png
/usr/share/gtk-doc/html/gi/right.png
/usr/share/gtk-doc/html/gi/style.css
/usr/share/gtk-doc/html/gi/up-insensitive.png
/usr/share/gtk-doc/html/gi/up.png
```

執行

``` sh
$ firefox /usr/share/gtk-doc/html/gi/index.html
```

執行

``` sh
$ lynx /usr/share/gtk-doc/html/gi/index.html
```

執行

``` sh
$ w3m /usr/share/gtk-doc/html/gi/index.html
```
