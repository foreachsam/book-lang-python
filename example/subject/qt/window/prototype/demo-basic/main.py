#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle('Demo Window')
win.resize(800, 600)
win.move(200, 200)

win.show()

app.exec()
#sys.exit(app._exec())

## Doc
## file:///usr/share/doc/pyqt5-doc/html/pyqt4_differences.html
