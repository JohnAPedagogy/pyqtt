# import sys
# from PyQt4.QtGui import QApplication, QPushButton
# app=QApplication(sys.argv)
# button=QMessageBox.warning (QWidget, "Exit?", "Exit", QMessageBox.Ok, StandardButton defaultButton = QMessageBox.NoButton)
# if button==
# button.show()
# sys.exit(app.exec_())

import cv2, base64
from aiohttp import web
cap = cv2.VideoCapture(0)

async def hello(request):
    _, image = cap.read()
    _, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    return web.Response(body=jpg_as_text)

app = web.Application()
app.add_routes([web.get('/', hello)])


web.run_app(app)


# print('imported')

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     cv2.imshow('Output', img)
#     cv2.waitKey(0)

