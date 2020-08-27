import threading
import time
import queue
from pymongo import *
from QQ_msg_with_Python_TCP.client_sender import Interactive
from gwills_tools.scrab_img_at_cl import get_web_link, find_url
from gwills_tools.insert_my_mongodb import insert_to_database
from pprint import pprint

# 2020年8月27日, 19点28分
# 使用 queue 队列技术
# 本代码 已经修改- 主要有两个线程,一个监听listen,另一个后台不断检测并执行任务队列,
# listen到数据后不会处理,会扔给queue_lst并继续listen
# queue 会不断检测queue_lst,然后一点点按顺序处理
# 你可以自己修改.
# 本仓库主要用来备份自己的代码, 非必要不会做过多的 封装.


def block_listen():  # 前台不断接收 值,返回给列表,后不间断监听
    global queue_lst
    while 1:
        result = s.listen()
        if result:
            # queue_lst = [result] + queue_lst
            q.put(result)
            print('已添加到消息处理队列--:')
            if 'fromQQ' in result.keys():
                s.private_msg('爸爸你交给我的事情我记下了,还有'+str(q.qsize())+'个没给您发完', result['fromQQ'])

my_qq = 2934289319
def detect_about_me(result):
    if 'fromQQ' in result.keys():  # TODO: 这里改成特定条件触发回复
        res_type = result.get('res_type')
        res_msg = result.get('msg')
        if res_type == 1:  # 如果type 为1 进行私发回复
            from_qq = int(result.get('fromQQ'))
            message = result.get('msg')
            from_group = result.get('fromGroup')
            print('提取about me 的消息:', res_msg)
            return True, res_msg
        if res_type == 2:
            if f"[@{my_qq}]" in res_msg:
                print('提取about me 的消息:', res_msg)
                return True, res_msg
            else:
                return None
        if res_type == 3:
            print('事件消息', res_msg)

def back_queue():   # 后台消息处理队列  不断检测输入内容, 并执行相应程序
    while 1:
        queue_arg = q.get()
        if queue_arg:

            for i in range(1, 6):
                notice = "..." * i
                states = "操作中: "
                if i == 5:
                    notice = '!!!' * i
                    states = "操作成功"
                notice = f'{i:>2}/5|{queue_arg["msg"][:5]:<6}|{states}{notice:15}| 队列剩余:{q.qsize() * "#":<10}'
                print(notice)
                s.private_msg(notice, from_qq=1274667113)
                time.sleep(0.9)
            print('====本条数据处理完毕=====')


def multi_process():
    while True:
        global s, threads, queue_lst, q
        threads = []
        queue_lst = []
        q = queue.Queue()
        try:
            print('尝试建立连接')
            s = Interactive("137.78.5.44", 8404, 2934289319)
            # s = Interact("172.16.66.170", 8404, 2154024779)
            print('###进入监听发送模式,Ctrl+C退出:')
            front_func = threading.Thread(target=block_listen)  # 前台函数
            back_func = threading.Thread(target=back_queue)  # 后台任务处理队列
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


