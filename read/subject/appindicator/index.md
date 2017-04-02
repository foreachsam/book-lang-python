---
layout: page
title: Python Gtk Appindicator
description: >
  Python Gtk Appindicator
date: 2017-03-29 14:03:35 +0800
source_url: '/read/subject/appindicator/index.md'
---


## 範例

### Prototype

* [demo-import](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/appindicator/prototype/demo-import/main.py)
* [demo-app](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/appindicator/prototype/demo-app/main.py)
* [demo-daemon](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/appindicator/prototype/demo-daemon/main.py)

### Composite

* [demo-app](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/appindicator/composite/demo-app/main.py)
* [demo-daemon](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/appindicator/composite/demo-daemon/main.py)

### 整合範例

* [fullscreen-composite-appindicator-webkit-version](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/fullscreen/fullscreen-composite-appindicator-webkit-version/main.py) ([Fullscreen](https://foreachsam.github.io/book-lang-python/read/subject/fullscreen/))

## API

### Gtk-3

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes.html)

### AppIndicator3

* [https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/](https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/)
* [https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes.html](https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes.html)
* [https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html](https://lazka.github.io/pgi-docs/index.html#AppIndicator3-0.1/classes/Indicator.html)

### Gtk.Menu

* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/Menu.html)
* [https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html](https://lazka.github.io/pgi-docs/index.html#Gtk-3.0/classes/MenuItem.html)

## Package

* [libappindicator3-dev](http://packages.ubuntu.com/xenial/libappindicator3-dev)
* [libappindicator3-1](http://packages.ubuntu.com/xenial/libappindicator3-1)
* [gir1.2-appindicator3-0.1](http://packages.ubuntu.com/xenial/gir1.2-appindicator3-0.1)


執行下面指令，安裝「[libappindicator3-dev](http://packages.ubuntu.com/xenial/libappindicator3-dev)」

``` sh
$ sudo apt-get install libappindicator3-dev
```

執行

``` sh
$ dpkg -l '*appindicator*'
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  gir1.2-appindicator3-0.1        12.10.1+16.04.201702 amd64                Typelib files for libappindicator3-1.
ii  libappindicator-doc             12.10.1+16.04.201702 all                  Application Indicators
ii  libappindicator1                12.10.1+16.04.201702 amd64                Application Indicators
ii  libappindicator3-1              12.10.1+16.04.201702 amd64                Application Indicators
ii  libappindicator3-dev            12.10.1+16.04.201702 amd64                Application Indicators
ii  python-appindicator             12.10.1+16.04.201702 amd64                Python bindings for libappindicator
un  python2.7-appindicator          <none>               <none>               (no description available)
```



執行

``` sh
$ apt-cache showsrc libappindicator3-dev | grep '^Binary:'
```

顯示

```
Binary: python-appindicator, libappindicator1, gir1.2-appindicator-0.1, libappindicator-dev, libappindicator-doc, libappindicator3-1, libappindicator3-dev, gir1.2-appindicator3-0.1, libappindicator0.1-cil, libappindicator0.1-cil-dev
```

執行

``` sh
$ apt-cache show libappindicator3-dev | grep '^Depends:'
```

顯示

```
Depends: gir1.2-appindicator3-0.1 (= 12.10.1+16.04.20170215-0ubuntu1), libdbusmenu-glib-dev (>= 0.1.8), libdbus-glib-1-dev (>= 0.76), libappindicator3-1 (= 12.10.1+16.04.20170215-0ubuntu1)
```

## 相關連結

* Ubuntu Wiki / [ApplicationIndicators](https://wiki.ubuntu.com/DesktopExperienceTeam/ApplicationIndicators)
* Launchpad / [libappindicator](https://launchpad.net/libappindicator)
