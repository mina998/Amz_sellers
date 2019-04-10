# coding:utf-8
import sqlite3
import webbrowser
from time import time, sleep

from api.base import Base

DB_URI = './assets/spider.dll'
POP_TIME = 3600*24

class Ad(Base):

    def __init_db(self):
        self.__con = sqlite3.connect(DB_URI)
        self.__cur = self.__con.cursor()

    def __pop_ad(self):
        #当时间时间
        curr_time = int(time())
        # 上次弹出时间
        last_pop_time = self.__cur.execute('select last_pop_time from ad where id = 1').fetchall()[0][0]
        if last_pop_time == 0:
            self.__cur.execute('update ad set last_pop_time=%d where id = 1' % curr_time)
            self.__con.commit()
            return False
        if curr_time - POP_TIME > last_pop_time :
            self.__cur.execute('update ad set last_pop_time=%d where id = 1' % curr_time)
            self.__con.commit()
            return True
        return False

    def __get_ad_url(self):
        #当前时间
        curr_time = int(time())
        # 获取广告最后更新时间
        ad_up_time = self.__cur.execute('select ad_up_time from ad where id = 1').fetchall()[0][0]
        # 广告每7天更新一次
        if curr_time - ad_up_time > 7*24*3600:
            # 更新广告时间
            self.__cur.execute('update ad set ad_up_time=%s'%curr_time)
            # 下载广告链接
            self.request(url='https://raw.githubusercontent.com/mina998/data/master/ad_taobao_amz')
            if self.response.status_code != 200: return False
            urls = self.response.text.split('\n')
            urls = [url for url in urls if url !='']
            # 删除数据
            self.__cur.execute('delete from link')
            self.__cur.execute('update sqlite_sequence SET seq = 0 where name ="link"')
            self.__con.commit()
            # 从新添加数据
            for url in urls: self.__cur.execute('insert into link (url) values ("%s")'% url)
            self.__con.commit()
        else:
            url = self.__cur.execute('select url from link order by random() limit 1').fetchall()[0][0]
        return url

    def run(self):
        # 创建数据库链接
        self.__init_db()
        while True:
            url = self.__get_ad_url()
            if self.__pop_ad():
                webbrowser.open_new_tab(url)
            sleep(5)