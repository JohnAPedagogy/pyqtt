# import sys
# from PyQt4.QtGui import QApplication, QPushButton
# app=QApplication(sys.argv)
# button=QMessageBox.warning (QWidget, "Exit?", "Exit", QMessageBox.Ok, StandardButton defaultButton = QMessageBox.NoButton)
# if button==
# button.show()
# sys.exit(app.exec_())

import cv2

print('imported')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow('Output', img)
    cv2.waitKey(0)