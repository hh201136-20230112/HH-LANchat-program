from PyQt5.QtWidgets import QApplication, QMainWindow
import Mainwin
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = Mainwin.Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()
    sys.exit(app.exec_())