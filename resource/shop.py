# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\0.Code\SellM\resource\ui\shop.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(-1, -1, -1, 3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(0, 110))
        self.label.setMaximumSize(QtCore.QSize(16777215, 110))
        self.label.setStyleSheet("")
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setEnabled(False)
        self.submit.setMinimumSize(QtCore.QSize(40, 32))
        self.submit.setMaximumSize(QtCore.QSize(40, 32))
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 0, 1, 1, 1)
        self.input = QtWidgets.QLineEdit(Form)
        self.input.setMinimumSize(QtCore.QSize(0, 30))
        self.input.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input.setText("")
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 0, 0, 1, 1)
        self.logs = QtWidgets.QPlainTextEdit(Form)
        self.logs.setObjectName("logs")
        self.gridLayout.addWidget(self.logs, 2, 0, 1, 2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        self.status.setMinimumSize(QtCore.QSize(0, 24))
        self.status.setMaximumSize(QtCore.QSize(16777215, 24))
        self.status.setStyleSheet("")
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        self.monitor = QtWidgets.QPushButton(self.frame)
        self.monitor.setEnabled(False)
        self.monitor.setMinimumSize(QtCore.QSize(60, 24))
        self.monitor.setMaximumSize(QtCore.QSize(60, 24))
        self.monitor.setObjectName("monitor")
        self.horizontalLayout.addWidget(self.monitor)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 2)

        self.retranslateUi(Form)
        self.input.textChanged['QString'].connect(Form.input_check_slot)
        self.submit.clicked.connect(Form.submit_slot)
        self.monitor.clicked.connect(Form.pop_monitor_slot)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "查询店铺ASIN Q:519999189"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">操作方法</span></p><p>1.输入卖家店铺ID:点[开始]. <a href=\"https://jingyan.baidu.com/article/afd8f4ded1681834e286e917.html\"><span style=\" text-decoration: underline; color:#0000ff;\">如何获取卖家ID</span></a></p><p>2.获取ASIN完成:点[监控跟卖] </p><p>3.查看监控记录</p></body></html>"))
        self.submit.setText(_translate("Form", "开始"))
        self.input.setPlaceholderText(_translate("Form", "请输入店铺ID"))
        self.status.setText(_translate("Form", "等待中..."))
        self.monitor.setText(_translate("Form", "监控跟卖"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

