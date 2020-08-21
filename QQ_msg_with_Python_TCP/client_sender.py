from socket import *
from urllib import parse
import time

class Interactive:
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

    def private_msg(self, msg, from_qq):
        # 组合
        data = {"msg": msg,
                "random": 0,
                "fromQQ": int(from_qq),
                "selfQQ": self.self_qq,
                "type": 101,
                "req": 0}
        # 3.向服务器发送数据
        self.conn.send(str(data).encode('gbk'))
        print('私聊执行完毕')

    def group_msg(self, msg, from_group):
        data = {"msg": msg,
                "random": 0,
                "fromGroup": int(from_group),
                "selfQQ": self.self_qq,
                "type": 201,  # 203 也是群聊
                "req": 0}
        self.conn.send(str(data).encode('gbk'))


    def listen(self):
        recv_data = self.conn.recv(1024)  # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
        url_code = recv_data.decode('gbk')  # decode GBK
        receive_dict = eval(parse.unquote(url_code))
        if recv_data:

            return receive_dict
        else:
            print("对方已离线。。")

    def run(self):
        print('###进入交互发送模式,Ctrl+C退出:')
        while True:
            try:
                input_text = '2/群聊消息/1106878273' #input('输入选择和内容, 用/ 分割:')
                choice, msg, toqq = input_text.split('/')
                print(choice, msg, toqq)
                if choice == '1':
                    self.private_msg(msg, toqq)
                if choice == '2':
                    self.group_msg(msg, toqq)
                print('send over.sleep')
                time.sleep(5)
            except KeyboardInterrupt:
                try:
                    input('用户中断: Ctrl+C终止/Enter继续')
                except KeyboardInterrupt:
                    break
            except Exception as E:
                print('注意！输入出现了问题！', E)
                input('回车后继续')

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    s = Interactive("172.16.66.170", 8404, 2934289319)
    s.crte_conn()
    # s.run()
    s.private_msg('To 12dfd7', 1274667113)
    time.sleep(2)
    s.group_msg('主动群聊测试', 1106878273)
    s.close()
