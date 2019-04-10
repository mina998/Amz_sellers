# coding:utf-8
import os
import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QTableWidgetItem, QAbstractItemView

from api.asin import Asin
from resource.sellers import Ui_Form


class Sellers(QWidget, Ui_Form):
    remind_signal = pyqtSignal(int)

    __logfile = '监控记录.txt'
    __asins = []

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__remind = 1
        self.setupUi(self)

        if parent: parent.monitor_tables_data_trigger.connect(self.__set_tables_data)

    def __set_tables_data2(self, data, seller):
        self.__asins = data
        self.__seller= seller
        model = QStandardItemModel(self.tables)
        model.setColumnCount(3)
        model.setHeaderData(0, Qt.Horizontal, 'ASIN')
        model.setHeaderData(1, Qt.Horizontal, '最后查询时间')
        model.setHeaderData(2, Qt.Horizontal, '发现跟卖')

        model.setRowCount(len(data))
        for i, item in enumerate(data):
            model.setItem(i, 0, QStandardItem(item))
        self.tables.setModel(model)
        # 开始
        self.__start()

    def __set_tables_data(self, data, seller):
        self.__asins = data
        self.__seller= seller

        self.tables.setRowCount(len(data))
        self.tables.setColumnCount(3)
        self.tables.setHorizontalHeaderLabels(['ASIN', '最后查询时间', '跟卖'])

        for i, item in enumerate(data):
            self.tables.setItem(i, 0, QTableWidgetItem(item))
        self.tables.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tables.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tables.resizeColumnsToContents()
        self.tables.setColumnWidth(0,100)
        self.tables.setColumnWidth(1,155)
        self.tables.setColumnWidth(2,75)

        # 开始
        self.__start()

    def __start(self):
        '''
        开始操作
        :return:
        '''
        self.status.setText('监控开始...')
        # 删除日志文件
        if os.path.isfile(self.__logfile): os.remove(self.__logfile)
        th = Asin(self, asins=self.__asins, seller=self.__seller, remind=self.__remind)
        th.trigger.connect(self.__update_tables)
        th.start()



    def view_logs_slot(self):
        '''
        查看日志
        :return:
        '''
        if os.path.isfile(self.__logfile):
            os.system('explorer.exe ".\\%s"'%self.__logfile)
        else:
            QMessageBox.information(self, '系统提示', '没有任何记录')

    def clear_logs_slot(self):
        # 删除日志文件
        if os.path.isfile(self.__logfile): os.remove(self.__logfile)
        QMessageBox.information(self, '系统提示', '清理完成!')

    def sms_slot(self):
        QMessageBox.information(self, '系统提示', '暂不支持短信提醒!\n选此项将不在播报提醒声音.')
        self.__remind = 2
        self.remind_signal.emit(2)

    def sound_slot(self):
        self.__remind = 1
        self.remind_signal.emit(1)

    def __update_tables(self, results):
        '''
        动态运行操作记录
        :param results:
        :return:
        '''
        if results['action'] < 1:
            self.status.setText(results['msg'])

        elif results['action'] == 1:
            data = results['data']
            if len(data) > 0:
                msg = ' 跟卖已被记录日志'
                self.tables.setItem(results['idx'], 1, QTableWidgetItem(results['date']))
                self.tables.setItem(results['idx'], 2, QTableWidgetItem('有跟卖'))
                self.__log_write(results['asin'], results['date'], data)
            else:
                msg = ' 未发现跟卖'
            self.status.setText(results['msg'] + msg)

    def __log_write(self, asin, date, data):
        '''
        写入日志文件
        :param asin: 查询的ASIN号
        :param date: 查询时间
        :param data: 查询数据记录
        :return:
        '''
        with open(self.__logfile, 'a+', encoding='utf-8') as f:
            logs = '----[%s]--[%s]---------------\n' % (asin, date)
            for row in data:
                type = '自发货' if row['type'] == 0 else 'FBA'
                logs += '[类型]:%s [店铺ID]:%s [店铺名]:%s \n' % (type, row['sell'], row['name'])
            logs += '-----------------------------------------------------------\n\n'
            f.write(logs)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Sellers()
    win.show()

    sys.exit(app.exec_())
