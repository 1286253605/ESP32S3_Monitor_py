# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\2ESP32_Platformio\SerialMonitor_Python\python_sw\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 180)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 90, 395, 31))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_flush = QtWidgets.QPushButton(self.widget)
        self.pushButton_flush.setObjectName("pushButton_flush")
        self.gridLayout.addWidget(self.pushButton_flush, 0, 0, 1, 1)
        self.pushButton_open_serial = QtWidgets.QPushButton(self.widget)
        self.pushButton_open_serial.setObjectName("pushButton_open_serial")
        self.gridLayout.addWidget(self.pushButton_open_serial, 0, 1, 1, 1)
        self.pushButton_monitor_start = QtWidgets.QPushButton(self.widget)
        self.pushButton_monitor_start.setObjectName("pushButton_monitor_start")
        self.gridLayout.addWidget(self.pushButton_monitor_start, 0, 2, 1, 1)
        self.pushButton_monitor_stop = QtWidgets.QPushButton(self.widget)
        self.pushButton_monitor_stop.setObjectName("pushButton_monitor_stop")
        self.gridLayout.addWidget(self.pushButton_monitor_stop, 0, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(100, 40, 450, 28))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_com_select = QtWidgets.QComboBox(self.widget1)
        self.comboBox_com_select.setObjectName("comboBox_com_select")
        self.gridLayout_2.addWidget(self.comboBox_com_select, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.comboBox_baud = QtWidgets.QComboBox(self.widget1)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.gridLayout_2.addWidget(self.comboBox_baud, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)
        self.comboBox_gap_time = QtWidgets.QComboBox(self.widget1)
        self.comboBox_gap_time.setEditable(True)
        self.comboBox_gap_time.setObjectName("comboBox_gap_time")
        self.comboBox_gap_time.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_gap_time, 0, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SerialCtrl"))
        self.pushButton_flush.setText(_translate("MainWindow", "刷新串口"))
        self.pushButton_open_serial.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_monitor_start.setText(_translate("MainWindow", "开始监控"))
        self.pushButton_monitor_stop.setText(_translate("MainWindow", " 停止监控"))
        self.label.setText(_translate("MainWindow", "串口号:"))
        self.label_2.setText(_translate("MainWindow", "波特率:"))
        self.label_3.setText(_translate("MainWindow", "时间间隔："))
        self.comboBox_gap_time.setItemText(0, _translate("MainWindow", "1000"))
