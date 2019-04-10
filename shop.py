# coding:utf-8
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication
from api.shop import Shop
from resource.shop import Ui_Form

class Index(QWidget, Ui_Form):
    # 弹出窗口信号
    pop_monitor_trigger = pyqtSignal()
    # 卖家ID
    seller= False
    # 保存店铺ASIN列表
    asins = []

    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 设置为只读
        self.logs.setReadOnly(True)


    def submit_slot(self):
        self.asins = []
        self.logs.clear()
        self.seller = self.input.text().strip()
        self.thread = Shop(self,seller=self.seller)
        self.thread.trigger.connect(self.__asins_get)
        self.thread.start()
        self.status.setText('状态:运行中...')
        self.submit.setEnabled(False)


    def input_check_slot(self):
        if len(self.input.text()) > 5: self.submit.setEnabled(True)
        else: self.submit.setEnabled(False)


    def pop_monitor_slot(self):
        self.pop_monitor_trigger.emit()


    def __asins_get(self,result):
        if result['action'] < 1: self.logs.insertPlainText(result['msg']+'\n')
        if result['action'] == 3:
            for asin in result['asins']:
                self.asins.append(asin)
                self.status.setText('状态:正在获取店铺ASIN [%s]'%len(self.asins))
                # 光标移到最后
                cursor = self.logs.textCursor()
                cursor.movePosition(QtGui.QTextCursor.End)
                self.logs.setTextCursor(cursor)
                # 插入内容
                self.logs.insertPlainText(asin+'\n')
        if result['action'] == 2:
            self.status.setText(result['msg']+':共获取[%s]数据'%len(self.asins))
            self.monitor.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Index()
    win.show()
    sys.exit(app.exec_())