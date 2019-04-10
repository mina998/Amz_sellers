# coding:utf-8
import requests
from time import sleep
from PyQt5.QtCore import QThread

class Base(QThread):
    # 亚马逊首页
    index = 'https://www.amazon.com'
    # headers
    __headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = None
    # 每次请求返回信息
    results = dict(
        action=0, #-1 请求失败, 0 没有错误
        msg='开始获取令牌!',
        data=[]
    )

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__session = requests.session()
        self.__session.headers.update(self.__headers)


    def request(self, method='GET', url=None, params=None, data=None):
        '''
        发送请求
        :param method: 请求方法
        :param url: 请求地址
        :param params: url参数 dict类型
        :param data: Post数据 dict类型
        :return: Response 对象
        '''

        try:
            self.response = self.__session.request(method, url=url, params=params, data=data)
        except Exception as e:
            self.results['action'] = -1
            self.results['msg'] = 'HTTP请求异常'

    def update(self, headers={}):
        '''
        更新Headers 和 Cookies
        :param headers:
        :return:
        '''
        self.__session.headers.update(headers)

    def token_get(self):
        change = 'https://www.amazon.com/gp/delivery/ajax/address-change.html'
        # 获取首页cookies
        self.request(url=self.index)
        if self.results['action'] == -1: return False
        sleep(3)
        # 获取此页面设置的必要cookies
        data = {
            'locationType': 'LOCATION_INPUT',
            'zipCode': '10001',
            'storeContext': 'generic',
            'deviceType': 'web',
            'pageType': 'Gateway',
            'actionSource': 'glow'
        }
        self.request(method='POST', url=change, data=data)
        if self.results['action'] == -1: return False
        if not self.__session.cookies.get('ubid-main'):
            self.results['action'] = -1
            self.results['msg'] = '令牌获取失败!'
        else: self.results['msg'] = '令牌获取成功!'
