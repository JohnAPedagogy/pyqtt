#!/usr/bin/env python

from cachedtable import TableEditor

import connection
from PyQt4 import QtCore, QtGui


class TabDialog(QtGui.QWidget):
    def __init__(self, fileName):
        super(TabDialog, self).__init__()

        fileInfo = QtCore.QFileInfo(fileName)
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(TableEditor('names'), "Members")
        tabWidget.addTab(TableEditor('att'), "Attendance")
        tabWidget.addTab(TableEditor('prog'), "Programm")
        tabWidget.addTab(TableEditor('ict'), "ICT")
        tabWidget.addTab(ApplicationsTab(fileInfo), "Applications")


        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        self.setLayout(mainLayout)

        self.setWindowTitle("Christ Church Young Adults Database")

class ApplicationsTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(ApplicationsTab, self).__init__(parent)

        topLabel = QtGui.QLabel("Open with:")

        applicationsListBox = QtGui.QListWidget()
        applications = []

        for i in range(1, 31):
            applications.append("Application %d" % i)

        applicationsListBox.insertItems(0, applications)

        alwaysCheckBox = QtGui.QCheckBox()

        if fileInfo.suffix():
            alwaysCheckBox = QtGui.QCheckBox("Always use this application to "
                    "open files with the extension '%s'" % fileInfo.suffix())
        else:
            alwaysCheckBox = QtGui.QCheckBox("Always use this application to "
                    "open this type of file")

        layout = QtGui.QVBoxLayout()
        layout.addWidget(topLabel)
        layout.addWidget(applicationsListBox)
        layout.addWidget(alwaysCheckBox)
        self.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        fileName = "."
    if not connection.createConnection():
        sys.exit(1)

    tabdialog = TabDialog(fileName)
    tabdialog.show()
    sys.exit(app.exec_())
