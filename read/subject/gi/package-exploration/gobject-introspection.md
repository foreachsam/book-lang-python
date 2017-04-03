---
layout: page
title: Package - gobject-introspection
description: >
  Package - gobject-introspection
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/gobject-introspection.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---

# gobject-introspection

執行

``` sh
$ apt-cache search 'gobject introspection'
```

執行

``` sh
$ apt-cache search 'gobject-introspection'
```

執行

``` sh
$ apt-cache show gobject-introspection
```

執行

``` sh
$ apt-cache showsrc gobject-introspection
```

執行

``` sh
$ apt-cache show gobject-introspection | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.14), libffi6 (>= 3.0.4), libgirepository-1.0-1 (= 1.46.0-3ubuntu1), libglib2.0-0 (>= 2.45.3), python:any, build-essential, python-mako
```

執行

``` sh
$ apt-cache showsrc gobject-introspection | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: gobject-introspection
Binary: libgirepository-1.0-1, libgirepository1.0-dev, libgirepository1.0-doc, gobject-introspection, gir1.2-glib-2.0, gir1.2-freedesktop
Version: 1.46.0-3ubuntu1
```


執行

``` sh
$ dpkg -l gobject-introspection
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gobject-introspection           1.46.0-3ubuntu1      amd64                Generate interface introspection data for GObject libraries
```

執行

``` sh
$ dpkg -L gobject-introspection | less
```

執行

``` sh
$ dpkg -L gobject-introspection | grep bin | sort
```

顯示

```
/usr/bin
/usr/bin/dh_girepository
/usr/bin/g-ir-annotation-tool
/usr/bin/g-ir-compiler
/usr/bin/g-ir-doc-tool
/usr/bin/g-ir-generate
/usr/bin/g-ir-scanner
```

執行

``` sh
$ dpkg -L gobject-introspection | grep man | sort
```

顯示

``` sh
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/dh_girepository.1.gz
/usr/share/man/man1/g-ir-compiler.1.gz
/usr/share/man/man1/g-ir-generate.1.gz
/usr/share/man/man1/g-ir-scanner.1.gz
```

### Manpage

* $ man [dh_girepository](http://manpages.ubuntu.com/manpages/xenial/en/man1/dh_girepository.1.html)
* $ man [g-ir-compiler](http://manpages.ubuntu.com/manpages/xenial/en/man1/g-ir-compiler.1.html)
* $ man [g-ir-generate](http://manpages.ubuntu.com/manpages/xenial/en/man1/g-ir-generate.1.html)
* $ man [g-ir-scanner](http://manpages.ubuntu.com/manpages/xenial/en/man1/g-ir-scanner.1.html)
