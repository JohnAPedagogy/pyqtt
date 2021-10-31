# import sys
# from PyQt4.QtGui import QApplication, QPushButton
# app=QApplication(sys.argv)
# button=QMessageBox.warning (QWidget, "Exit?", "Exit", QMessageBox.Ok, StandardButton defaultButton = QMessageBox.NoButton)
# if button==
# button.show()
# sys.exit(app.exec_())

import cv2, base64
from aiohttp import web
import aiohttp_cors


cap = cv2.VideoCapture(0)

async def hello(request):
    return web.Response(text="Hello, world")

async def capture(request):
    _, image = cap.read()
    _, buffer = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(buffer)
    return web.Response(body=jpg_as_text)

app = web.Application()
# app.add_routes([web.get('/', capture)
#             , web.get('/hello', hello)
#             ])

# `aiohttp_cors.setup` returns `aiohttp_cors.CorsConfig` instance.
# The `cors` instance will store CORS configuration for the
# application.
cors = aiohttp_cors.setup(app)

# To enable CORS processing for specific route you need to add
# that route to the CORS configuration object and specify its
# CORS options.
hello_url = cors.add(app.router.add_resource("/hello"))
root_url = cors.add(app.router.add_resource("/"))
route = cors.add(
    hello_url.add_route("GET", hello), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("*",),
            allow_headers=("*"),
            max_age=3600,
        )
    })
route = cors.add(
    root_url.add_route("GET", capture), {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers=("*",),
            allow_headers=("*"),
            max_age=3600,
        )
    })

# cors.add(route, {
#         "*":
#             aiohttp_cors.ResourceOptions(allow_credentials=False),
#         "http://client.example.org":
#             aiohttp_cors.ResourceOptions(allow_credentials=True),
#     })
web.run_app(app)


# print('imported')

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
#     cv2.imshow('Output', img)
#     cv2.waitKey(0)

