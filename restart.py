import sys,os
from PyQt4 import QtCore, QtGui
def getUI():
  d = QtGui.QDialog()
  label = QtGui.QLabel("Restart Phone?")
  okButton = QtGui.QPushButton("&OK")
  escButton = QtGui.QPushButton("&Cancel")
  layout= QtGui.QHBoxLayout(d)
  layout.addWidget(label)
  layout.addWidget(okButton)
  layout.addWidget(escButton)
  okButton.clicked.connect(restart)
  escButton.clicked.connect(cancel)
  return d

def restart():
  os.system("echo \"reboot\"|sudo gainroot| echo \"\"")
  return

def cancel():
  sys.exit(0)
  return

app = QtGui.QApplication(sys.argv)
x=getUI()
sys.exit(x.exec_())
