import sys
from PyQt4.QtGui import QApplication, QPushButton
app=QApplication(sys.argv)
button=QMessageBox.warning (QWidget, "Exit?", "Exit", QMessageBox.Ok, StandardButton defaultButton = QMessageBox.NoButton)
if button==
button.show()
sys.exit(app.exec_())