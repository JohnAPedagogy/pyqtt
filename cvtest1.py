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
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow('Output', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break