# coding:utf-8
import re, time, pythoncom
from api.conf import CARRY_TIME
from PyQt5.QtCore import pyqtSignal
from lxml import etree
from api.base import Base
from win32com import client

class Asin(Base):
    # Listing 页面前缀
    __offer = 'https://www.amazon.com/gp/offer-listing/'
    # Asin 列表
    __asins = []
    #
    __remind_mode = 1 #1为播放电脑声音, 2为短信通知
    # 触发信号
    trigger = pyqtSignal(dict)

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.__asins = kwargs['asins']
        self.__seller= kwargs['seller']
        self.__remind_mode = kwargs['remind']

    def __listing_get(self):

        for idx, asin in enumerate(self.__asins):
            # 写入日志 查看哪里出错了
            self.__run_log_write(asin)
            # 请求 https://www.amazon.com/gp/offer-listing/B01ARGB67M
            self.request(url=self.__offer+asin)
            # print(asin)
            html = etree.HTML(self.response.text)
            # 获取卖家列表
            rows = html.xpath('//div[@id="olpOfferList"]//div[@role="row"]/div[4]/h3')
            # 查找跟卖
            data = self.__sellers_get(rows)
            if len(data) > 0:
                self.results['data'] = data
                self.__remind_()
            else: self.results['data'] =[]

            self.results['action'] = 1
            self.results['asin'] = asin
            self.results['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            self.results['idx']  = idx
            self.results['msg']  = '正在查看[%s]:%s'%(idx+1,asin)
            self.trigger.emit(self.results)
            time.sleep(2)


    def __sellers_get(self, elements):
        '''
        查找跟卖
        :param elements: 卖家列表(html) elements
        :return:
        '''
        sellers = []
        for ele in elements:
            data = {}
            href = ele.xpath('.//a/@href')[0]
            logo = ele.xpath('.//img/@alt')
            type = re.findall(r'isAmazonFulfilled=(\d)&', href)
            sell = re.findall(r'shops/([A-Z0-9]+?)/', href)
            if not sell:  sell = re.findall(r'seller=([A-Z0-9]+)', href)
            # print(sell)
            data['sell'] = sell[0]
            data['name'] = logo[0] if logo else ele.xpath('.//a/text()')[0]
            data['type'] = int(type[0]) if len(type) == 1 else 1
            # 如果是自己就退出
            if data['sell'] == self.__seller: continue

            sellers.append(data)
        return sellers


    def __remind_(self):
        if self.__remind_mode == 1:
            import winsound
            # 初始化
            pythoncom.CoInitialize()
            msg = '有跟卖!'
            speak = client.Dispatch('SAPI.SPVOICE')
            speak.Speak(msg)
            # 播放音乐
            winsound.PlaySound('assets/sound.wav', flags=1) #此行不需要释放资源 只是为了音乐提前播放
            speak.Speak(msg)
            # 释放资源
            pythoncom.CoUninitialize()
        if self.__remind_mode == 2: ''

    def __run_log_write(self,log):
        sjc = time.localtime(time.time())
        date = time.strftime('%Y-%m-%d %H:%M:%S', sjc)
        file = time.strftime('%Y-%m-%d', sjc)+'.log'
        with open('assets/'+file, 'a+', encoding='utf-8') as fb:
            fb.write('--['+date+']: '+log+'\n')

    def __remind_slot(self,mode):
        '''
        监控父窗体发来信号(提醒方法)
        :param mode:
        :return:
        '''
        self.__remind_mode = mode


    def run(self):
        #0.
        self.parent().remind_signal.connect(self.__remind_slot)
        #1. 开始获取令牌
        self.trigger.emit(self.results)
        #2. 获取令牌
        self.token_get()
        #3. 抛出token获取信息
        self.trigger.emit(self.results)
        #4. 开始查找跟卖
        while True:
            self.__listing_get()
            s = int(CARRY_TIME)
            while s:
                s = s-1
                time.sleep(1)
                self.results['action'] = -1
                self.results['msg'] = '查询完成! 倒计时[%s]秒后继续...'%s
                self.trigger.emit(self.results)