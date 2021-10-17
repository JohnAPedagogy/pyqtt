from PyQt4 import QtCore, QtGui

def getwindow():
  checkbox=QtGui.QCheckBox("case sensitive")
  combobox=QtGui.QComboBox()
  combobox.addItem("Large (L)")
  spinbox=QtGui.QSpinBox()
  window = QtGui.QWidget()
  label = QtGui.QLabel("name:")
  editor= QtGui.QLineEdit()
  layout= QtGui.QHBoxLayout(window)
  layout.addWidget(label)
  layout.addWidget(editor)
  return window #.show()

if __name__ == '__main__':
  import sys

  app = QtGui.QApplication(sys.argv)

  ui = getwindow()
  ui.show()

  sys.exit(app.exec_())
