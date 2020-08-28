from socket import *
from urllib import parse
from pprint import pprint


class Listener:
    def __init__(self, ip, port, self_qq):  # 键入 初始配置: IP/ 端口/自己的QQ
        self.ip = ip
        self.port = port
        self.self_qq = int(self_qq)
        self.conn = self.crte_conn()

    def crte_conn(self):
        # 1.创建tcp_client_socket 套接字对象

        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        # 2.连接服务器  连接到172.16.66.170, 8404
        tcp_client_socket.connect((self.ip, self.port))
        return tcp_client_socket

    def listen(self):

        recv_data = self.conn.recv(1024)  # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了

        url_code = recv_data.decode('gbk')  # decode GBK
        receive_dict = eval(parse.unquote(url_code))
        if recv_data:

            print("返回的消息为:")
            pprint(receive_dict)  # quote2 url_code
            print('=' * 80)
            return receive_dict
        else:
            print("对方已离线...")

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    # 本代码仅用来监听,可单独运行
    l = Listener('172.16.66.170', 8404, 2154024779) # 键入 初始配置: IP/ 端口/自己的QQ
    while True:
        l.listen()

    l.close()
