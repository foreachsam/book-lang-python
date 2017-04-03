---
layout: page
title: Package - python3-gi
description: >
  Package - python3-gi
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/python3-gi.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# python3-gi

執行

``` sh
$ apt-cache search 'gobject-introspection' | grep python
```

顯示

```
python-gi - Python 2.x bindings for gobject-introspection libraries
python-glade2 - GTK+ bindings: Glade support
python-gobject-2 - deprecated static Python bindings for the GObject library
python-gobject-2-dbg - deprecated static Python bindings for the GObject library (debug extension)
python-gobject-2-dev - development headers for the static GObject Python bindings
python-gobject-dbg - Python 2.x debugging modules for GObject - transitional package
python-gobject-dev - Python 2.x development headers for GObject - transitional package
python-gtk2 - Python bindings for the GTK+ widget set
python-gtk2-dbg - Python bindings for the GTK+ widget set (debug extension)
python-gtk2-dev - GTK+ bindings: devel files
python-gtk2-doc - Python bindings for the GTK+ widget set - documentation
python3-gi - Python 3 bindings for gobject-introspection libraries
python3-gi-dbg - Python 3 bindings for gobject-introspection libraries (debug extension)
python-gobject - Python 2.x bindings for GObject - transitional package
python-v-sim - Python bindings for V_Sim (a 3D visualization package)
```

執行

``` sh
$ apt-cache search 'gobject-introspection' | grep python3
```

顯示

```
python3-gi - Python 3 bindings for gobject-introspection libraries
python3-gi-dbg - Python 3 bindings for gobject-introspection libraries (debug extension)
```

執行

``` sh
$ apt-cache show python3-gi
```

執行

``` sh
$ apt-cache showsrc python3-gi
```

執行

``` sh
$ apt-cache show python3-gi | grep '^Depends:'
```

顯示

```
Depends: python3 (<< 3.6), python3 (>= 3.5~), libc6 (>= 2.14), libffi6 (>= 3.0.4), libgirepository-1.0-1 (>= 1.44.0), libglib2.0-0 (>= 2.41.1), gir1.2-glib-2.0 (>= 1.39.0)
```

執行

``` sh
$ apt-cache showsrc python3-gi | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: pygobject
Binary: python-gi, python3-gi, python-gi-cairo, python-gi-dbg, python3-gi-dbg, python-gi-dev, python3-gi-cairo, python-gobject, python-gobject-dbg, python-gobject-dev
Version: 3.20.0-0ubuntu1
```

執行

``` sh
$ dpkg -l python3-gi
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  python3-gi                      3.20.0-0ubuntu1      amd64                Python 3 bindings for gobject-introspection libraries
```

執行

``` sh
$ dpkg -L python3-gi | sort
```

顯示

```
/.
/usr
/usr/lib
/usr/lib/python3
/usr/lib/python3/dist-packages
/usr/lib/python3/dist-packages/gi
/usr/lib/python3/dist-packages/gi/_constants.py
/usr/lib/python3/dist-packages/gi/docstring.py
/usr/lib/python3/dist-packages/gi/_error.py
/usr/lib/python3/dist-packages/gi/_gi.cpython-35m-x86_64-linux-gnu.so
/usr/lib/python3/dist-packages/gi/_gobject
/usr/lib/python3/dist-packages/gi/_gobject/__init__.py
/usr/lib/python3/dist-packages/gi/importer.py
/usr/lib/python3/dist-packages/gi/__init__.py
/usr/lib/python3/dist-packages/gi/module.py
/usr/lib/python3/dist-packages/gi/_option.py
/usr/lib/python3/dist-packages/gi/overrides
/usr/lib/python3/dist-packages/gi/overrides/Gdk.py
/usr/lib/python3/dist-packages/gi/overrides/GIMarshallingTests.py
/usr/lib/python3/dist-packages/gi/overrides/Gio.py
/usr/lib/python3/dist-packages/gi/overrides/GLib.py
/usr/lib/python3/dist-packages/gi/overrides/GObject.py
/usr/lib/python3/dist-packages/gi/overrides/Gtk.py
/usr/lib/python3/dist-packages/gi/overrides/__init__.py
/usr/lib/python3/dist-packages/gi/overrides/keysyms.py
/usr/lib/python3/dist-packages/gi/overrides/Pango.py
/usr/lib/python3/dist-packages/gi/_propertyhelper.py
/usr/lib/python3/dist-packages/gi/pygtkcompat.py
/usr/lib/python3/dist-packages/gi/repository
/usr/lib/python3/dist-packages/gi/repository/__init__.py
/usr/lib/python3/dist-packages/gi/_signalhelper.py
/usr/lib/python3/dist-packages/gi/types.py
/usr/lib/python3/dist-packages/pygobject-3.20.0.egg-info
/usr/lib/python3/dist-packages/pygtkcompat
/usr/lib/python3/dist-packages/pygtkcompat/generictreemodel.py
/usr/lib/python3/dist-packages/pygtkcompat/__init__.py
/usr/lib/python3/dist-packages/pygtkcompat/pygtkcompat.py
/usr/share
/usr/share/doc
/usr/share/doc/python3-gi
/usr/share/doc/python3-gi/changelog.Debian.gz
/usr/share/doc/python3-gi/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/python3-gi
```
