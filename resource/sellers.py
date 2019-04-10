# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\0.Code\SellM\resource\ui\sellers.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 500)
        Form.setMinimumSize(QtCore.QSize(400, 500))
        Form.setMaximumSize(QtCore.QSize(400, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(Form)
        self.header.setStyleSheet("")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.header)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sound = QtWidgets.QRadioButton(self.header)
        self.sound.setEnabled(True)
        self.sound.setCheckable(True)
        self.sound.setChecked(True)
        self.sound.setObjectName("sound")
        self.horizontalLayout_2.addWidget(self.sound)
        self.sms = QtWidgets.QRadioButton(self.header)
        self.sms.setObjectName("sms")
        self.horizontalLayout_2.addWidget(self.sms)
        self.input = QtWidgets.QLineEdit(self.header)
        self.input.setMinimumSize(QtCore.QSize(170, 24))
        self.input.setMaximumSize(QtCore.QSize(170, 24))
        self.input.setObjectName("input")
        self.horizontalLayout_2.addWidget(self.input)
        self.verticalLayout.addWidget(self.header)
        self.tables = QtWidgets.QTableWidget(Form)
        self.tables.setMinimumSize(QtCore.QSize(60, 0))
        self.tables.setRowCount(0)
        self.tables.setColumnCount(3)
        self.tables.setObjectName("tables")
        self.tables.horizontalHeader().setVisible(True)
        self.tables.horizontalHeader().setCascadingSectionResizes(True)
        self.tables.horizontalHeader().setDefaultSectionSize(123)
        self.verticalLayout.addWidget(self.tables)
        self.footer = QtWidgets.QFrame(Form)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status = QtWidgets.QLabel(self.footer)
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.view_logs = QtWidgets.QPushButton(self.footer)
        self.view_logs.setMaximumSize(QtCore.QSize(90, 16777215))
        self.view_logs.setObjectName("view_logs")
        self.horizontalLayout.addWidget(self.view_logs)
        self.verticalLayout.addWidget(self.footer)

        self.retranslateUi(Form)
        self.view_logs.clicked.connect(Form.view_logs_slot)
        self.sms.clicked.connect(Form.sms_slot)
        self.sound.clicked.connect(Form.sound_slot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "监控跟卖 Q519999189"))
        self.label.setText(_translate("Form", "发现跟卖:"))
        self.sound.setText(_translate("Form", "播放声音"))
        self.sms.setText(_translate("Form", "短信"))
        self.input.setPlaceholderText(_translate("Form", "请输入接收短信的手机号码"))
        self.status.setText(_translate("Form", "等待中..."))
        self.view_logs.setText(_translate("Form", "查看监控记录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

