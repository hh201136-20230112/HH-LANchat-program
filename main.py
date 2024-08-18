import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import Mainwin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = Mainwin.Ui_MainWindow()
    ui.setupUi(mainwin)
    try:
        mainwin.show()
        sys.exit(app.exec_())
    finally:
        ui.is_running = False