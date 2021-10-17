#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2009 Nokia Corporation and/or its subsidiary(-ies).
## Contact: Qt Software Information (qt-info@nokia.com)
##
## This file is part of the example classes of the Qt Toolkit.
##
#############################################################################

from PyQt4 import QtCore, QtGui
#from enot import SciNot, EngNot


class ENotUI(QtGui.QWidget):
  def __init__(self, parent=None):
    super(ENotUI, self).__init__(parent)

    self.sn = QtGui.QLabel()
    self.en = QtGui.QLabel()
    self.val = QtGui.QLineEdit()

    #connections
    self.val.textChanged.connect(self.doConvert)

    #layouting
    mainLayout = QtGui.QVBoxLayout()
    mainLayout.addWidget(self.val)
    mainLayout.addWidget(self.en)
    mainLayout.addWidget(self.sn)

    self.setLayout(mainLayout)
    self.setWindowTitle("Notation Sampler")

  def doConvert(self, mstr):
    try:
      f=float(mstr)
    except ValueError:
      QtGui.QMessageBox.information(self, "Invalid Entry",
              "Please enter a numeric value.")
      self.val.undo()
    else:
      self.sn.setText(str(f))
      self.en.setText(str(f))

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)

  ui = ENotUI()
  ui.show()

  sys.exit(app.exec_())
