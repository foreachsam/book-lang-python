---
layout: page
title: Package - libffi-dev
description: >
  Package - libffi-dev
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libffi-dev.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libffi-dev

執行

``` sh
$ apt-cache show libffi-dev
```

執行

``` sh
$ apt-cache showsrc libffi-dev
```

執行

``` sh
$ apt-cache show libffi-dev | grep '^Depends:'
```

顯示

```
Depends: libffi6 (= 3.2.1-4), dpkg (>= 1.15.4) | install-info
```

執行

``` sh
$ apt-cache showsrc libffi-dev | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: libffi
Binary: libffi-dev, libffi6, libffi6-dbg, libffi6-udeb
Version: 3.2.1-4
```

執行

``` sh
$ dpkg -l libffi-dev
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libffi-dev:amd64                3.2.1-4              amd64                Foreign Function Interface library (development files)
```

執行

``` sh
$ dpkg -L libffi-dev | sort
```

顯示

```
/.
/usr
/usr/include
/usr/include/x86_64-linux-gnu
/usr/include/x86_64-linux-gnu/ffi.h
/usr/include/x86_64-linux-gnu/ffitarget.h
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/libffi.a
/usr/lib/x86_64-linux-gnu/libffi_pic.a
/usr/lib/x86_64-linux-gnu/libffi.so
/usr/lib/x86_64-linux-gnu/pkgconfig
/usr/lib/x86_64-linux-gnu/pkgconfig/libffi.pc
/usr/share
/usr/share/doc
/usr/share/doc-base
/usr/share/doc-base/libffi
/usr/share/doc/libffi6
/usr/share/doc/libffi6/changelog.gz
/usr/share/doc/libffi6/ChangeLog.libffi-3.1.gz
/usr/share/doc/libffi6/ChangeLog.libffi.gz
/usr/share/doc/libffi6/ChangeLog.libgcj
/usr/share/doc/libffi6/ChangeLog.v1.gz
/usr/share/doc/libffi6/html
/usr/share/doc/libffi6/html/Closure-Example.html
/usr/share/doc/libffi6/html/Complex.html
/usr/share/doc/libffi6/html/Complex-Type-Example.html
/usr/share/doc/libffi6/html/index.html
/usr/share/doc/libffi6/html/Index.html
/usr/share/doc/libffi6/html/Introduction.html
/usr/share/doc/libffi6/html/Missing-Features.html
/usr/share/doc/libffi6/html/Multiple-ABIs.html
/usr/share/doc/libffi6/html/Primitive-Types.html
/usr/share/doc/libffi6/html/Simple-Example.html
/usr/share/doc/libffi6/html/Structures.html
/usr/share/doc/libffi6/html/The-Basics.html
/usr/share/doc/libffi6/html/The-Closure-API.html
/usr/share/doc/libffi6/html/Type-Example.html
/usr/share/doc/libffi6/html/Types.html
/usr/share/doc/libffi6/html/Using-libffi.html
/usr/share/doc/libffi-dev
/usr/share/info
/usr/share/info/libffi.info.gz
/usr/share/man
/usr/share/man/man3
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_call.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_prep_cif_var.3.gz
```

執行

``` sh
$ dpkg -L libffi-dev | grep man
```

顯示

```
/usr/share/man
/usr/share/man/man3
/usr/share/man/man3/ffi_prep_cif_var.3.gz
/usr/share/man/man3/ffi.3.gz
/usr/share/man/man3/ffi_prep_cif.3.gz
/usr/share/man/man3/ffi_call.3.gz
```

執行

``` sh
$ dpkg -L libffi-dev | grep pc
```

顯示

```
/usr/lib/x86_64-linux-gnu/pkgconfig/libffi.pc
```

根據「/usr/lib/x86_64-linux-gnu/pkgconfig/libffi.pc」，

執行

``` sh
$ pkg-config --cflags --libs libffi
```

顯示

```
-lffi
```
