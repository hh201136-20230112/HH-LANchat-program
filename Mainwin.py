# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chat_text = QtWidgets.QTextEdit(self.centralwidget)
        self.chat_text.setGeometry(QtCore.QRect(150, 80, 650, 460))
        self.chat_text.setObjectName("chat_text")
        self.join_server = QtWidgets.QPushButton(self.centralwidget)
        self.join_server.setGeometry(QtCore.QRect(10, 70, 95, 30))
        self.join_server.setObjectName("join_server")
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(10, 4, 135, 31))
        self.LOGO.setObjectName("LOGO")
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(50, 30, 51, 16))
        self.version.setObjectName("version")
        self.craft_server = QtWidgets.QPushButton(self.centralwidget)
        self.craft_server.setGeometry(QtCore.QRect(10, 110, 95, 30))
        self.craft_server.setObjectName("craft_server")
        self.input_text = QtWidgets.QLineEdit(self.centralwidget)
        self.input_text.setGeometry(QtCore.QRect(150, 549, 570, 41))
        self.input_text.setObjectName("input_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 549, 80, 41))
        self.pushButton.setObjectName("pushButton")
        self.chat = QtWidgets.QPushButton(self.centralwidget)
        self.chat.setGeometry(QtCore.QRect(10, 150, 95, 30))
        self.chat.setObjectName("chat")
        self.about = QtWidgets.QPushButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(10, 560, 95, 30))
        self.about.setObjectName("about")
        self.status_bar = QtWidgets.QGroupBox(self.centralwidget)
        self.status_bar.setGeometry(QtCore.QRect(150, 10, 581, 61))
        self.status_bar.setObjectName("status_bar")
        self.server_status = QtWidgets.QLabel(self.status_bar)
        self.server_status.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.server_status.setObjectName("server_status")
        self.label = QtWidgets.QLabel(self.status_bar)
        self.label.setGeometry(QtCore.QRect(201, 14, 91, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.status_bar)
        self.label_2.setGeometry(QtCore.QRect(300, 14, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.status_bar)
        self.label_3.setGeometry(QtCore.QRect(400, 14, 121, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(740, 20, 60, 52))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chat_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是聊天内容</p></body></html>"))
        self.join_server.setText(_translate("MainWindow", "连接服务器"))
        self.LOGO.setText(_translate("MainWindow", "hh的局域网聊天软件"))
        self.version.setText(_translate("MainWindow", "V3.0.1"))
        self.craft_server.setText(_translate("MainWindow", "创建服务器"))
        self.input_text.setText(_translate("MainWindow", "我是输入框"))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.chat.setText(_translate("MainWindow", "聊天"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.status_bar.setTitle(_translate("MainWindow", "状态栏"))
        self.server_status.setText(_translate("MainWindow", "服务器:999.999.999.999"))
        self.label.setText(_translate("MainWindow", "延迟:9999ms"))
        self.label_2.setText(_translate("MainWindow", "在线人数:99"))
        self.label_3.setText(_translate("MainWindow", "公网延迟:9999ms"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
