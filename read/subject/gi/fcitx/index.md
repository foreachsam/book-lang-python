---
layout: page
title: Python Fcitx
description: >
  Python Fcitx
date: 2017-04-03 01:47:04 +0800
source_url: '/read/subject/gi/fcitx/index.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


## 範例


### Prototype

* [demo-import](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-import/main.py)
* [demo-get-current-state](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-get-current-state/main.py)
* [demo-get-imlist](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-get-imlist/main.py)
* [demo-get-current-im](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-get-current-im/main.py)
* [demo-toggle](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-toggle/main.py)
* [demo-reload-config](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-reload-config/main.py)
* [demo-restart](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-restart/main.py)
* [demo-exit](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-restart/main.py)
* [demo-configure](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-configure/main.py)
* [demo-get-im-addon](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-get-im-addon/main.py)
* [demo-configure-addon](https://github.com/foreachsam/book-lang-python/blob/gh-pages/example/subject/gi/fcitx/prototype/demo-configure-addon/main.py)


## API

### Fcitx

* [https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0](https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0)
* [https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes.html](https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes.html)

### Fcitx.InputMethod

* [https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes/InputMethod.html](https://lazka.github.io/pgi-docs/index.html#Fcitx-1.0/classes/InputMethod.html)


## 相關連結

* [http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/](http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/)
* [http://foreachsam.github.io/book-util-fcitx/book/content/command/fcitx-remote/](http://foreachsam.github.io/book-util-fcitx/book/content/command/fcitx-remote/)
* [http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/pygi-gio/](http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/pygi-gio/)

## 相關套件

* [gir1.2-fcitx-1.0](http://packages.ubuntu.com/xenial/gir1.2-fcitx-1.0)

### 操作步驟

執行下面指令，查詢相關套件

``` sh
$ apt-cache search fcitx | grep gir
```

顯示

```
gir1.2-fcitx-1.0 - Flexible Input Method Framework - GObject introspection
```

執行

``` sh
$ apt-cache show gir1.2-fcitx-1.0
```

執行

``` sh
$ apt-cache showsrc gir1.2-fcitx-1.0
```

執行下面指令，安裝「[gir1.2-fcitx-1.0](http://packages.ubuntu.com/xenial/gir1.2-fcitx-1.0)」

``` sh
$ apt-get install gir1.2-fcitx-1.0
```
