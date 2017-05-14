from PyQt5 import Qt
import sys
app = Qt.QApplication(sys.argv)
systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon("df"))
systemtray_icon.show()
systemtray_icon.showMessage('Title', 'Content')