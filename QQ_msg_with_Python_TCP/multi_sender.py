import threading
import time
from QQ_msg_with_Python_TCP.client_sender import Interactive
# 2020年8月26日,21点54分,
# 本代码仅仅是本地测试 未正式接入到 listener,
# 你可以自己修改.
# 本仓库主要用来备份自己的代码, 非必要不会做过多的 封装.




# def multi(func):
#     print('='*20)
#
#     def inner(lst=''):
#         for i in range(2):
#             print(i)
#             t = threading.Thread(target=func, args=lst)
#             threads.append(t)
#             t.start()
#         for t in threads:
#             t.join()
#
#         return
#
#     print('='*20)
#     return inner

def insert():

    for i in range(1,6):
        print(f'|操作中:{"##" * i:14}| 队列剩余:{len(queue_lst):<2} 回车可接受消息')
        time.sleep(0.8)

class Interact:
    def listen(self):
        global queue_lst
        # for i in range(10):
        #     strs = 'listen' + '#' * (10 - i) + 'Enter>\n'
        while True:
            strs = '监听中:' + '#' * 3 + '回车模拟发送消息>\n'
            input(strs)

            t = threading.Thread(target=insert)
            queue_lst.append(t)
            print('已添加到消息处理队列-->共:', len(queue_lst))
            print('\n')
            # t.start()
            # t.join()

queue_lst = []
def queue():
    while 1:
        # time.sleep(2)
        # print('current_ queue', queue_lst)
        if queue_lst:
            t = queue_lst.pop()
            t.start()
            t.join()
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# s = Interactive("172.16.66.170", 8404, 2934289319)
# s.crte_conn()

if __name__ == '__main__':
    s = Interact()

    threads = []
    t2 = threading.Thread(target=s.listen)
    threads.append(t2)
    t = threading.Thread(target=queue)
    threads.append(t)

    t.start()
    t2.start()

    for x in threads:  # 这里是在干嘛?
        x.join()

    # multi(s.listen)()



