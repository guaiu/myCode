#!/usr/bin/env python
# -*- coding: utf-8 -*-

# demo2 QML文件的载入

from PySide2.QtWidgets import QApplication
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import QUrl

#

if __name__ == '__main__':
    app = QApplication([])
    view = QQuickView()
    url = QUrl("demo2QML.qml")

    view.setSource(url)
    view.show()
    app.exec_()