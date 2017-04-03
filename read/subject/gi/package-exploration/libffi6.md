---
layout: page
title: Package - libffi6
description: >
  Package - libffi6
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libffi6.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libffi6

執行

``` sh
$ apt-cache show libffi6
```

執行

``` sh
$ apt-cache showsrc libffi6
```

執行

``` sh
$ apt-cache show libffi6 | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.14)
```

執行

``` sh
$ apt-cache showsrc libffi6 | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: libffi
Binary: libffi-dev, libffi6, libffi6-dbg, libffi6-udeb
Version: 3.2.1-4
```

執行

``` sh
$ dpkg -l libffi6
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libffi6:amd64                   3.2.1-4              amd64                Foreign Function Interface library runtime
```

執行

``` sh
$ dpkg -L libffi6 | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/libffi.so.6
/usr/lib/x86_64-linux-gnu/libffi.so.6.0.4
/usr/share
/usr/share/doc
/usr/share/doc/libffi6
/usr/share/doc/libffi6/changelog.Debian.gz
/usr/share/doc/libffi6/copyright
```
