# coding:utf-8
import json, re
from time import sleep
from PyQt5.QtCore import pyqtSignal
from lxml import etree
from api.base import Base
from api.conf import LENGTH_ASIN


class Shop(Base):
    # 店铺地址前缀
    __shop_url = 'https://www.amazon.com/shops/'
    # 保存店铺列表所有链接
    __links = []
    # 统计页码
    __tongji_page = 0
    # 统计Asin数量
    __tongji_asin = 0
    # 限制Asin获取数量
    __length = LENGTH_ASIN
    # 触发信号
    trigger = pyqtSignal(dict)

    def __init__(self, parent=None, **kwargs):
        super().__init__(parent)
        self.seller = kwargs['seller']


    def __page_links_get(self, url):
        '''
        获得店铺列表页所有链接
        :param url: 店铺首页链接
        :return: 链接列表 list
        '''
        #
        if self.__tongji_asin > self.__length: return False

        self.request(url=url)
        sleep(1.5)
        html = etree.HTML(self.response.text)
        self.__tongji_page+=1
        self.results['action'] = 0
        self.results['msg'] = '开始获取店铺第%s页数据!' % self.__tongji_page
        self.trigger.emit(self.results)
        # 当前页链接数
        links = html.xpath('//div[@data-asin]//h5/a/@href')
        # 获取当前页链接下面的所有Asin
        self.__link_asin_get(links)
        # 下一页
        next = html.xpath('//ul[@class="a-pagination"]/li[@class="a-selected"]/following-sibling::li[@class="a-normal"][1]/a/@href')

        if len(next)>0: self.__page_links_get(self.index+next[0])


    def __link_asin_get(self,links):
        for url in links:
            #
            if self.__tongji_asin > self.__length:
                self.results['action'] = 0
                self.results['msg'] = '测试版限制获取[%s]条Asin'% str(self.__length+1)
                self.trigger.emit(self.results)
                break

            self.request(url=self.index+url)
            code = re.findall(r'"dimensionToAsinMap"\s*:\s*(\{.*?\}),', self.response.text)
            if len(code)>0:
                asins = json.loads(code[0])
                asins = [v for k,v in asins.items()]
            else:
                asins =  re.findall(r'/dp/([A-Z0-9]*?)/', url)
            # 统计所获得的Asin数
            self.__tongji_asin += len(asins)

            self.results['action'] = 3
            self.results['asins'] = asins
            self.trigger.emit(self.results)
            sleep(1.5)


    def run(self):
        #0.
        self.trigger.emit(self.results)
        #1. 获取令牌
        self.token_get()
        #2. 抛出token获取信息
        self.trigger.emit(self.results)
        #3. 获取店铺所有ASIN
        self.__page_links_get(url=self.__shop_url+self.seller)
        #4. 获取完成 结束
        self.results['action'] = 2
        self.results['msg'] = '获取完成'
        self.trigger.emit(self.results)


