# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import server
import threading
import time
import socket
import uuid
transport_protocol = 2.0
uuids = str(uuid.uuid1())
class Ui_MainWindow(object):
    def __init__(self):
        self.is_running = True
        self.off_process = threading.Thread(target=self.end_process)
        self.off_process.start()
        self.user_name = "user name"
        self.server_ip = ""
        self.open_port = 9999
        self.join_sever_step = -1  # 用于控制配置服务器相关数据，-1表示配置完成
        self.s = socket.socket()
        self.Built_in_server=False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(825, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.chat_text = QtWidgets.QTextEdit(self.centralwidget)
        self.chat_text.setGeometry(QtCore.QRect(150, 80, 650, 460))
        self.chat_text.setObjectName("chat_text")
        self.chat_text.setReadOnly(True)
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
        self.craft_server.clicked.connect(self.start_servers)
        self.join_server.clicked.connect(self.join_servers)
        self.pushButton.clicked.connect(self.text_process)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def join_server_function(self):
        self.text_add("开始连接服务器\n")
        self.s.bind(("", self.open_port))
        self.s.connect((self.server_ip, 9980))
        byteses = bytes(f"Request-connection-V{transport_protocol} {self.user_name} {uuids}", "utf-8")
        # Request-connection-Vn.n 用于校验客户端与服务器连接协议是否相同
        self.s.send(byteses)
        self.text_add("正在发送验证信息\n")
        strs = self.s.recvfrom(2048)[0]
        strs = str(strs)
        if uuids in strs:
            self.text_add("UUID校验通过")
        else:
            self.text_add("UUID校验错误,请重试\n")
            raise
        byteses = bytes(f"{self.user_name} {uuids}", "utf-8")
        self.s.send(byteses)
        b = self.s.recvfrom(2048)[0]
        self.text_add("丢包检测通过\n")
        self.join_sever_step -= 1
        self.text_add("连接完成\n")

    def text_process(self):
        # 用于处理输入框输入的数据
        _translate = QtCore.QCoreApplication.translate
        strs = str(self.input_text.text())
        self.input_text.setText(_translate("MainWindow", ""))
        self.text_add(f"{self.user_name}:{strs} - {time.strftime('%Y/%m/%d %H:%M')}\n")
        if self.join_sever_step == -1:
            # 进入普通消息处理
            pass
        else:
            # 进入服务器加入数据处理
            if self.join_sever_step == 2:
                self.user_name = strs
                if self.Built_in_server:
                    self.join_sever_step = 0
                    self.server_ip="127.0.0.1"
                    self.text_add("请输入本机开启的端口号(缺省9999)\n")
                else:
                    self.join_sever_step -= 1
                    self.text_add("请输入服务器IP\n")
            elif self.join_sever_step == 1:
                self.server_ip = strs
                self.join_sever_step -= 1
                self.text_add("请输入本机开启的端口号(缺省9999)\n")
            elif self.join_sever_step == 0:
                try:
                    if strs=="":self.open_port = 9999
                    else:self.open_port = int(strs)
                    self.text_add("服务器配置完成,正在连接服务器\n")
                    self.join_server_function()
                    self.text_add("服务器已连接\n")
                except ValueError:
                    self.text_add("端口号输入错误,请确认是否输入了非数字字符,或者选择使用缺省值(留空)\n")

    def end_process(self):
        # 线程结束器(把is_running设为False以关闭所有线程)
        while self.is_running:
            pass
        server.is_running = False
        self.s.close()

    def text_add(self, strs):
        self.chat_text.setText(self.chat_text.toPlainText() + strs)

    def start_servers(self):
        self.text_add("正在启动服务器\n")
        self.servers = threading.Thread(target=server.listen_socket)
        self.servers.start()
        self.craft_server.setEnabled(False)
        self.join_server.setEnabled(False)
        self.text_add("服务器加载完成\n")
        self.Built_in_server=True
        self.text_add("请输入用户名\n")
        self.join_sever_step = 2

    def join_servers(self):
        self.text_add("请输入用户名\n")
        self.craft_server.setEnabled(False)
        self.join_server.setEnabled(False)
        self.join_sever_step = 2

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "hh的局域网聊天工具"))
        self.chat_text.setText(_translate("MainWindow", f"""
HH的局域网通讯程序 V3.0 (测试版)
当前连接协议：HH-web-V{transport_protocol}
请使用相同协议的客户端与服务器
IPV6支持：{socket.has_ipv6}
本机UUID:{uuids}

使用前须知:
    本程序中发送的内容均以明文传输，未经过加密，请不要发送重要信息

输入/以使用指令
"""))
        self.join_server.setText(_translate("MainWindow", "连接服务器"))
        self.LOGO.setText(_translate("MainWindow", "hh的局域网聊天工具"))
        self.version.setText(_translate("MainWindow", "V3.0.1"))
        self.craft_server.setText(_translate("MainWindow", "创建服务器"))
        self.input_text.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.chat.setText(_translate("MainWindow", "聊天"))
        self.about.setText(_translate("MainWindow", "关于"))
        self.status_bar.setTitle(_translate("MainWindow", "状态栏"))
        self.server_status.setText(_translate("MainWindow", "服务器:999.999.999.999"))
        self.label.setText(_translate("MainWindow", "延迟:9999ms"))
        self.label_2.setText(_translate("MainWindow", "在线人数:99"))
        self.label_3.setText(_translate("MainWindow", "公网延迟:9999ms"))
        self.pushButton_2.setText(_translate("MainWindow", "刷新"))
