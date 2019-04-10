# coding:utf-8
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore

from api.ad import Ad
from shop import Index
from sellers import Sellers

class Main(QWidget):

    monitor_tables_data_trigger = pyqtSignal(list, str)
    def __init__(self):
        super().__init__()
        self.resize(400,450)
        self.setMinimumSize(QtCore.QSize(400, 500))
        self.setMaximumSize(QtCore.QSize(400, 500))
        self.index = Index(self)
        self.setWindowTitle(self.index.windowTitle())
        self.index.pop_monitor_trigger.connect(self.pop_monitor_win)


    def pop_monitor_win(self):
        th = Ad(self)
        th.start()

        self.index.hide()
        self.monitor = Sellers(self)
        self.monitor.move(0,0)
        self.monitor.show()
        self.setWindowTitle(self.monitor.windowTitle())
        self.monitor_tables_data_trigger.emit(self.index.asins, self.index.seller)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())