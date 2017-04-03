---
layout: page
title: Package - libglib2.0-bin
description: >
  Package - libglib2.0-bin
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libglib2.0-bin.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libglib2.0-bin

執行

``` sh
$ apt-cache show libglib2.0-bin
```

執行

``` sh
$ apt-cache showsrc libglib2.0-bin
```

執行

``` sh
$ apt-cache show libglib2.0-bin | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.4), libelf1 (>= 0.142), libglib2.0-0 (= 2.48.2-0ubuntu1), libglib2.0-data
```

執行

``` sh
$ apt-cache showsrc libglib2.0-bin | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: glib2.0
Binary: libglib2.0-0, libglib2.0-tests, libglib2.0-udeb, libglib2.0-bin, libglib2.0-dev, libglib2.0-0-dbg, libglib2.0-data, libglib2.0-doc, libgio-fam, libglib2.0-0-refdbg
Version: 2.48.0-1ubuntu4
```

執行

``` sh
$ dpkg -l libglib2.0-bin
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libglib2.0-bin                  2.48.2-0ubuntu1      amd64                Programs for the GLib library
```

執行

``` sh
$ dpkg -L libglib2.0-bin | sort
```

顯示

```
/.
/usr
/usr/bin
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gio-querymodules
/usr/bin/glib-compile-resources
/usr/bin/glib-compile-schemas
/usr/bin/gresource
/usr/bin/gsettings
/usr/share
/usr/share/bash-completion
/usr/share/bash-completion/completions
/usr/share/bash-completion/completions/gapplication
/usr/share/bash-completion/completions/gdbus
/usr/share/bash-completion/completions/gresource
/usr/share/bash-completion/completions/gsettings
/usr/share/doc
/usr/share/doc/libglib2.0-bin
/usr/share/doc/libglib2.0-bin/AUTHORS
/usr/share/doc/libglib2.0-bin/changelog.Debian.gz
/usr/share/doc/libglib2.0-bin/copyright
/usr/share/doc/libglib2.0-bin/NEWS.gz
/usr/share/doc/libglib2.0-bin/README.gz
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/gdbus.1.gz
/usr/share/man/man1/gio-querymodules.1.gz
/usr/share/man/man1/glib-compile-resources.1.gz
/usr/share/man/man1/glib-compile-schemas.1.gz
/usr/share/man/man1/gresource.1.gz
/usr/share/man/man1/gsettings.1.gz
```


執行

``` sh
$ dpkg -L libglib2.0-bin | grep bin
```

顯示

```
/usr/bin
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gresource
/usr/bin/gsettings
/usr/share/doc/libglib2.0-bin
/usr/share/doc/libglib2.0-bin/copyright
/usr/bin/gio-querymodules
/usr/bin/glib-compile-schemas
/usr/bin/glib-compile-resources
/usr/share/doc/libglib2.0-bin/changelog.Debian.gz
/usr/share/doc/libglib2.0-bin/README.gz
/usr/share/doc/libglib2.0-bin/AUTHORS
/usr/share/doc/libglib2.0-bin/NEWS.gz
```

執行

``` sh
$ dpkg -L libglib2.0-bin | grep man
```

顯示

```
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/gsettings.1.gz
/usr/share/man/man1/glib-compile-resources.1.gz
/usr/share/man/man1/glib-compile-schemas.1.gz
/usr/share/man/man1/gdbus.1.gz
/usr/share/man/man1/gio-querymodules.1.gz
/usr/share/man/man1/gresource.1.gz
```
