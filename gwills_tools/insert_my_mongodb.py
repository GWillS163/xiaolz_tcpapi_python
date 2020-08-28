# coding=utf-8
from pymongo import *
import time

data_lst = [{'img': 'http://i2.hdslb.com/bfs/archive/e0784716f4553c198484eed7381f6187319c4a8c.jpg',
             'tit': 'FlexConnect.第50期教主技术进化论-亁颐堂现任明教教主秦柯CCIE#13778',
             'lnk': 'http://www.bilibili.com/video/BV1Jb411K7TD',
             'tme': '02:00:36', 'dat': '2019-4-12'},]

class insert_to_database:
    def __init__(self, url_link, db_name, collect_name):
        self.username = 'admin'
        self.passwod = 'Cisc0123'
        self.url_link = url_link
        self.db = db_name
        self.collect = collect_name
        client = MongoClient(url_link.format(self.username, self.passwod))
        db = client[db_name]  # 选择或进入数据库
        # db.create_collection('QQ_bot')  # 其实不写，下一句也会自动创建
        self.db_coll = db['QQ_bot3']  # 选择数据库内的合集

    def insert_mydata_to(self, data):
        data.update({'create_time': time.strftime("%Y-%m-%d %H:%m", time.localtime())})
        self.db_coll.insert(data)


if __name__ == '__main__':
    db = insert_to_database('mongodb+srv://****:*****@qyt-cluster.catxh.azure.mongodb.net/QYT-cluster',
                            'private_spider_data', 'QQ_bot')
    for da in data_lst:
        db.insert_mydata_to(da)
