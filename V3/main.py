import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import Mainwin

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        mainwin = QMainWindow()
        ui = Mainwin.Ui_MainWindow()
        ui.setupUi(mainwin)
        mainwin.show()
        sys.exit(app.exec_())
    except:
        raise
    finally:
        ui.is_running=False