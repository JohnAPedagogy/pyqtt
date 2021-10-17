# import sys
# from PyQt4.QtGui import QApplication, QPushButton
# app=QApplication(sys.argv)
# button=QMessageBox.warning (QWidget, "Exit?", "Exit", QMessageBox.Ok, StandardButton defaultButton = QMessageBox.NoButton)
# if button==
# button.show()
# sys.exit(app.exec_())

import cv2
import aiohttp
import asyncio
import cv2, base64
import numpy as np

async def main():
    while True:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:8080/') as resp:
                jpg_original = base64.b64decode(await resp.read())
                nparr = np.frombuffer(jpg_original, np.uint8)
                img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                cv2.imshow('Output', img_np)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

