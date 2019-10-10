# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 360)
        Form.setMinimumSize(QtCore.QSize(512, 440))
        Form.setMaximumSize(QtCore.QSize(512, 440))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pinterest.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background:gray;")

        self.mail_address = QtWidgets.QLineEdit(Form)
        self.mail_address.setGeometry(QtCore.QRect(20, 20, 471, 20))
        self.mail_address.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.mail_address.setObjectName("mail_address")

        self.password = QtWidgets.QLineEdit(Form)
        self.password.setGeometry(QtCore.QRect(20, 60, 471, 20))
        self.password.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.board_link = QtWidgets.QLineEdit(Form)
        self.board_link.setGeometry(QtCore.QRect(20, 100, 471, 20))
        self.board_link.setStyleSheet("background:white;\n"
"border-radius:5px;")
        self.board_link.setObjectName("board_link")

        self.new_board = QtWidgets.QLineEdit(Form)
        self.new_board.setGeometry(QtCore.QRect(20, 140, 471, 20))
        self.new_board.setStyleSheet("background:white;\n"
                                      "border-radius:5px;")
        self.new_board.setObjectName("new_board")

        self.start_but = QtWidgets.QPushButton(Form)
        self.start_but.setGeometry(QtCore.QRect(270, 190, 220, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_but.setFont(font)
        self.start_but.setStyleSheet("background:#7de055;\n"
"border-radius:15px;")
        self.start_but.setObjectName("start_but")

        self.stop_but = QtWidgets.QPushButton(Form)
        self.stop_but.setGeometry(QtCore.QRect(270, 260, 220, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stop_but.setFont(font)
        self.stop_but.setStyleSheet("background:#e84833;\n"
"border-radius:15px;")
        self.stop_but.setObjectName("stop_but")

        self.show_browser = QtWidgets.QCheckBox(Form)
        self.show_browser.setGeometry(QtCore.QRect(20, 260, 150, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.show_browser.setFont(font)
        self.show_browser.setObjectName("show_browser")
        self.show_browser.setChecked(True)

        self.google_account = QtWidgets.QCheckBox(Form)
        self.google_account.setGeometry(QtCore.QRect(20, 287, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.google_account.setFont(font)
        self.google_account.setObjectName("google_account")

        self.excel_board = QtWidgets.QCheckBox(Form)
        self.excel_board.setGeometry(QtCore.QRect(20, 314, 230, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.excel_board.setFont(font)
        self.excel_board.setObjectName("excel_board")

        self.board_option = QtWidgets.QCheckBox(Form)
        self.board_option.setGeometry(QtCore.QRect(20, 339, 230, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.board_option.setFont(font)
        self.board_option.setObjectName("board_option")

        self.min_int = QtWidgets.QSpinBox(Form)
        self.min_int.setGeometry(QtCore.QRect(200, 190, 42, 22))
        self.min_int.setStyleSheet("background:yellow;")
        self.min_int.setObjectName("min_int")

        self.max_int = QtWidgets.QSpinBox(Form)
        self.max_int.setGeometry(QtCore.QRect(200, 230, 42, 22))
        self.max_int.setStyleSheet("background:yellow;")
        self.max_int.setObjectName("max_int")
        self.max_int.setMinimum(1)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 176, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 178, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.time_remaining = QtWidgets.QLabel(Form)
        self.time_remaining.setGeometry(QtCore.QRect(10, 365, 492, 55))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.time_remaining.setStyleSheet("background:#34bfbf;color:white;")
        self.time_remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.time_remaining.setFont(font)
        self.time_remaining.setObjectName("time_remaining")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PinterestBot"))
        self.mail_address.setPlaceholderText(_translate("Form", "  Mail address"))
        self.password.setPlaceholderText(_translate("Form", "  Password"))
        self.board_link.setPlaceholderText(_translate("Form", "  Board Link"))
        self.new_board.setPlaceholderText(_translate("Form", "  New Board Name"))
        self.start_but.setText(_translate("Form", "START"))
        self.stop_but.setText(_translate("Form", "STOP"))
        self.show_browser.setText(_translate("Form", "Show Browser"))
        self.google_account.setText(_translate("Form", "Use Google Account"))
        self.label_3.setText(_translate("Form", "min. interval (minute)"))
        self.label_4.setText(_translate("Form", "max. interval (minute)"))
        self.time_remaining.setText(_translate("Form", "Time Remaining"))
        self.excel_board.setText(_translate("Form", "Take Board From Excel"))
        self.board_option.setText(_translate("Form", "New Board Create"))