from PyQt5 import Qt
#from event import CalendarEvent
import sys

class notifications:

    def buildNotification(self, kwargs):
        eventTitle = kwargs['eventTitle']
        eventDescription = kwargs['eventDescription']

        app = Qt.QApplication(sys.argv)
        systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon("df"))
        systemtray_icon.show()
        systemtray_icon.showMessage(eventTitle, eventDescription)

