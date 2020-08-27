import threading
import time
from pymongo import *
from QQ_msg_with_Python_TCP.client_sender import Interactive
from gwills_tools.scrab_img_at_cl import get_web_link, find_url
from gwills_tools.insert_my_mongodb import insert_to_database
from pprint import pprint
# 2020年8月27日, 13点26分
# 本代码 已经修改- 主要有两个线程,一个监听listen,另一个后台不断检测并执行任务队列,
# listen到数据后不会处理,会扔给queue_lst并继续listen
# queue 会不断检测queue_lst,然后一点点按顺序处理
# 你可以自己修改.
# 本仓库主要用来备份自己的代码, 非必要不会做过多的 封装.

class Interact:
    def __init__(self, ip, port, qq):
        print('收到内置参数:', ip, port, qq)

    def listen(self):
        global queue_lst
        while True:
            # print('!', end=dddsfsdfds'')
            # time.sleep(1)
            strs = '监听中:' + '#' * 3 + '回车创建后台任务>'
            result = input(strs)
            return result
            # print('\n')


def block_listen():  # 前台不断接收 值,返回给列表,后不间断监听
    global queue_lst
    while 1:
        result = s.listen()
        if result:
            queue_lst = [result] + queue_lst
            print('已添加到消息处理队列-->共:', len(queue_lst))
            if 'fromQQ' in result.keys():
                s.private_msg('爸爸你交给我的事情我记下了,还有'+str(len(queue_lst))+'个没给您发完', result['fromQQ'])

def queue():   # 后台消息处理队列  不断检测输入内容, 并执行相应程序
    while 1:
        if queue_lst:
            queue_arg = queue_lst.pop()
            print('\n正在处理数据:', queue_arg)
            all_key = queue_arg.keys()
            if 'msg' in all_key and 'fromQQ' in all_key:
                find_url_res = find_url(queue_arg['msg'])
                print('里面找到的链接:')
                for finded_url in find_url_res:  # 如果有的话
                    url, title, output_lst, un_output_ls = get_web_link(finded_url)
                    send_msg = url + '\n' + title
                    send_to = queue_arg['fromQQ']

                    # 入数据库部分
                    data = {'title': title,
                            'url': url,
                            'output_lst':output_lst,
                            'un_output_lst': un_output_ls,
                            'fromQQ': send_to,
                            }
                    # pprint(data)
                    try:
                        mongo_insert(data)
                        s.private_msg('入库over', send_to)
                    except Exception as E:
                        print('入库出现问题', E)
                        s.private_msg(E, send_to)
                        pass

                    s.private_msg(send_msg, send_to)
                    for url in output_lst:
                        time.sleep(2)
                        s.private_msg(url, send_to)
            print('本条数据处理完毕')


def mongo_insert(data):
    data.update({'create_time': time.strftime("%Y-%m-%d %H:%m", time.localtime())})
    db_QQbot.insert(data)

def insert(te):
    for i in range(1, 6):
        notice = "..." * i
        states = "插入中: "
        if i == 5:
            notice = '!!!' * i
            states = "插入成功"
        print(f'\r{te[:20]:>21}|{states}{notice:15}| 队列剩余:{len(queue_lst) * "#":<10} \r')
        # print(f'\r|{te}操作中:{notice:15}| 队列剩余:{str(queue_lst):<10} \r')
        time.sleep(0.9)

def multi_process():
    global db_QQbot
    client = MongoClient('mongodb+srv://admin:---@qyt-cluster.catxh.azure.mongodb.net/QYT-cluster')
    db = client['private_spider_data']
    db_QQbot = db['QQ_bot']

    while True:
        global s, threads, queue_lst
        threads = []
        queue_lst = []
        try:
            print('尝试建立连接')
            s = Interactive("137.78.5.44", 8404, 2934289319)
            print('###进入监听发送模式,Ctrl+C退出:')
            front_func = threading.Thread(target=block_listen)  # 前台函数
            back_func = threading.Thread(target=queue)  # 后台任务处理队列
            threads.append(front_func)
            threads.append(back_func)
            back_func.start()
            front_func.start()
            for i in threads:
                i.join()
        except ConnectionResetError:
            print('连接中断!3s retry')
            time.sleep(3)
            break
        print('='*20)

if __name__ == '__main__':
    multi_process()

