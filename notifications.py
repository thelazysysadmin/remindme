from PyQt5 import Qt
import sys

class notifications:

    def buildNotification(self):
        app = Qt.QApplication(sys.argv)
        systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon("df"))
        systemtray_icon.show()
        systemtray_icon.showMessage('Title', 'Content')


nots = notifications()

nots.buildNotification()