from socket import *
from urllib import parse
import time
import json
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
        """/**              public static void sendPrivateMessages(long selfQQ,long fromQQ,String msg,long random,long req){
             * 发送私聊消息                   JSONObject json = new JSONObject();
             * @param selfQQ	框架QQ                    json.put("type", 101);
             * @param fromQQ	好友QQ                    json.put("selfQQ", selfQQ);
             * @param msg		发送的内容                   json.put("fromQQ", fromQQ);
             * @param random	撤回消息用                   json.put("msg", msg);
             * @param req		撤回消息用                   json.put("random", random);
             */
            }
        """
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

    def send_group_temporary_msg(self, msg, fromgroup, fromQQ,i):
        """
        /**
         * 发送群临时消息
         * @param selfQQ	框架QQ
         * @param fromGroup	群号
         * @param fromQQ	对方QQ
         * @param msg		发送的内容
         * @param random	撤回消息用
         * @param seq		撤回消息用
         */
        :return:
        """
        time.sleep(0.3)
        data = {"msg": msg,
                "random": 0,
                "fromQQ": int(fromQQ),
                "fromGroup": fromgroup,
                "selfQQ": self.self_qq,
                "type": 209,
                "req": 0}
        # 3.向服务器发送数据
        self.conn.send(str(data).encode('gbk'))
        print("临时会话 发送成功")
    # def n_json_msg(self, msg, fromQQ):
    #     """/**
    #          * 发送私聊Json消息
    #          * @param selfQQ	框架QQ
    #          * @param fromQQ	好友QQ
    #          * @param msg		发送的Json内容
    #          * @param random	撤回消息用
    #          * @param req		撤回消息用
    #          */
    #         public static void sendPrivateMessagesJson(long selfQQ,long fromQQ,String msg,long random,int req){
    #             JSONObject json = new JSONObject();
    #             json.put("type", 102);
    #             json.put("selfQQ", selfQQ);
    #             json.put("fromQQ", fromQQ);
    #             json.put("msg", msg);
    #             json.put("random", random);
    #             json.put("req", req);
    #             Main.clientTest.sendMsg(json.toJSONString());
    #         }
    #     """
    #     data = {
    #         "type": 102,
    #         "selfQQ": self.self_qq,
    #         "fromQQ": fromQQ,
    #         "msg": msg,
    #         "random": 1832647307,
    #         "req": 2047,
    #     }
    #     self.conn.send(str(data).encode('gbk'))
    # #
    # # def send_pm_pic_msg(self):
    # #     """
    # #             /**
    # #          * 发送私聊图文消息
    # #          * @param selfQQ
    # #          * @param fromQQ
    # #          * @param msg
    # #          * @param random
    # #          * @param req
    # #          */
    # #         public static void sendPrivateMessagesPicText(long selfQQ,long fromQQ,String msg,long random,long req){
    # #             JSONObject json = new JSONObject();
    # #             json.put("type", 103);
    # #             json.put("selfQQ", selfQQ);
    # #             json.put("fromQQ", fromQQ);
    # #             json.put("msg", msg);
    # #             json.put("random", random);
    # #             json.put("req", req);
    # #             Main.clientTest.sendMsg(json.toJSONString());
    # #         }
    # #     """
    # #     pass
    # #
    # # def process_verify(self):
    # #     """
    # #           /**
    # #            * 处理好友验证事件
    # #            * @param selfQQ	框架QQ
    # #            * @param fromQQ	好友QQ
    # #            * @param seq		请求附带的seq
    # #            * @param status	是否同意 1同意 2拒绝
    # #            */
    # #           public static void handlePrivateEvent(long selfQQ,long fromQQ,long seq,int status){
    # #               JSONObject json = new JSONObject();
    # #               json.put("type", 104);
    # #               json.put("selfQQ", selfQQ);
    # #               json.put("fromQQ", fromQQ);
    # #               json.put("seq", seq);
    # #               json.put("status", status);
    # #               Main.clientTest.sendMsg(json.toJSONString());
    # #           }
    # #       """
    # #     pass
    # #
    # # def qq_card_like(self):
    # #     """/**
    # #      * QQ点赞
    # #      * @param selfQQ	框架QQ
    # #      * @param fromQQ	好友QQ
    # #      */
    # #     public static void callpPraise(long selfQQ,long fromQQ,long number){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 105);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("number", number);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #     """
    # #     pass
    # #
    # #
    # # def send_friend_red_packet(self):
    # #     """
    # #         /**
    # #      * 发送好友红包
    # #      * @param selfQQ	框架QQ
    # #      * @param fromQQ	对方QQ
    # #      * @param number	红包数量
    # #      * @param balance	红包金额 分
    # #      * @param msg		祝福语
    # #      * @param payPwd	支付密码
    # #      */
    # #     public static void pushRedPacket(long selfQQ,long fromQQ,long number,long balance,String msg,String payPwd){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 106);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("number", number);
    # #         json.put("balance", balance);
    # #         json.put("payPwd", payPwd);
    # #         json.put("msg", msg);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #     """
    # #     pass
    # #
    # # def get_friends_list(self):
    # #     """
    # #         /**
    # #      * 获取好友列表
    # #      * @param selfQQ
    # #      */
    # #     public static void friendsList(long selfQQ){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 107);
    # #         json.put("selfQQ", selfQQ);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #
    # #         :return:
    # #     """
    # #     pass
    # #
    # # def revert_pm(self):
    # #     """
    # #             /**
    # #      * 撤回私聊消息
    # #      * @param selfQQ
    # #      * @param fromQQ
    # #      * @param random
    # #      * @param req
    # #      * @param time
    # #      */
    # #     public static void withdrawPrivateMessages(long selfQQ,long fromQQ,long random,long req,long time){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 108);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("random", random);
    # #         json.put("req", req);
    # #         json.put("time", time);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def query_friends_info(self):
    # #     """
    # #     /**
    # #      * 查询好友信息
    # #      * @param selfQQ
    # #      * @param fromQQ
    # #      */
    # #     public static void selectFriendsInfo(long selfQQ,long fromQQ){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 109);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromQQ", fromQQ);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def send_group_anymous(self):
    # #     """
    # #      /**
    # #      * 发送群聊消息
    # #      * @param selfQQ	框架QQ
    # #      * @param fromGroup	群号
    # #      * @param msg		发送的内容
    # #      * @param anonymous	是否匿名 0否 1是
    # #      */
    # #     public static void sendGroupMessages(long selfQQ,long fromGroup,String msg,int anonymous){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 201);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("msg", msg);
    # #         json.put("anonymous", anonymous);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def send_group_pic_text(self):
    # #     """
    # #     	/**
    # #      * 发送群图文消息
    # #      * @param selfQQ
    # #      * @param fromGroup
    # #      * @param msg
    # #      * @param anonymous
    # #      */
    # #     public static void sendGroupMessagesPicText(long selfQQ,long fromGroup,String msg,int anonymous){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 203);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("msg", msg);
    # #         json.put("anonymous", anonymous);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def process_group_verify(self):
    # #     """
    # #     /**
    # #      * 处理群验证事件
    # #      * @param selfQQ	框架QQ
    # #      * @param fromGroup	群号
    # #      * @param fromQQ	申请人QQ
    # #      * @param seq		请求附带的seq
    # #      * @param status	11同意 12拒绝  14忽略
    # #      * @param fromType	3某人申请加群 1我被邀请加入群
    # #      */
    # #     public static void handleGroupEvent(long selfQQ,long fromGroup,long fromQQ,long seq,int status,int fromType){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 204);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("seq", seq);
    # #         json.put("status", status);
    # #         json.put("fromType", fromType);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def set_group_cardname(self):
    # #     """
    # #
    # #         /**
    # #          * 处理群验证事件
    # #          * @param selfQQ	框架QQ
    # #          * @param fromGroup	群号
    # #          * @param fromQQ	申请人QQ
    # #          * @param seq		请求附带的seq
    # #          * @param status	11同意 12拒绝  14忽略
    # #          * @param fromType	3某人申请加群 1我被邀请加入群
    # #          */
    # #         public static void handleGroupEvent(long selfQQ,long fromGroup,long fromQQ,long seq,int status,int fromType){
    # #             JSONObject json = new JSONObject();
    # #             json.put("type", 204);
    # #             json.put("selfQQ", selfQQ);
    # #             json.put("fromGroup", fromGroup);
    # #             json.put("fromQQ", fromQQ);
    # #             json.put("seq", seq);
    # #             json.put("status", status);
    # #             json.put("fromType", fromType);
    # #             Main.clientTest.sendMsg(json.toJSONString());
    # #         }
    # #
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def kick_group_member(self):
    # #     """
    # #     /**
    # #      * 删除群成员
    # #      * @param selfQQ	框架QQ
    # #      * @param fromGroup	群号
    # #      * @param fromQQ	对方QQ
    # #      * @param refuse	拒绝加群申请 0否 1是
    # #      */
    # #     public static void delGroupMember(long selfQQ,long fromGroup,long fromQQ,int refuse){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 206);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("refuse", refuse);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def group_shutup(self):
    # #     """
    # #      /**
    # #      * 群禁言
    # #      * @param selfQQ	框架QQ
    # #      * @param fromGroup	群号
    # #      * @param fromQQ	对方QQ
    # #      * @param second	时间 秒
    # #      */
    # #     public static void prohibitSpeak(long selfQQ,long fromGroup,long fromQQ,int second){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 207);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("fromQQ", fromQQ);
    # #         json.put("second", second);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass
    # #
    # # def withdraw_group_msg(self):
    # #     """
    # #     /**
    # #      * 撤回群消息
    # #      * @param selfQQ	框架QQ
    # #      * @param fromGroup	群号
    # #      * @param random	消息附带的random
    # #      * @param req		消息附带的req
    # #      */
    # #     public static void withdrawGroupMessages(long selfQQ,long fromGroup,long random,long req){
    # #         JSONObject json = new JSONObject();
    # #         json.put("type", 208);
    # #         json.put("selfQQ", selfQQ);
    # #         json.put("fromGroup", fromGroup);
    # #         json.put("random", random);
    # #         json.put("req", req);
    # #         Main.clientTest.sendMsg(json.toJSONString());
    # #     }
    # #
    # #     :return:
    # #     """
    # #     pass

    #
    # def send_group_red_packet(self):
    #     """
    #      /**
    #      * 发送群聊红包
    #      * @param selfQQ	框架QQ
    #      * @param fromGroup	群号
    #      * @param number	红包数量
    #      * @param balance	红包金额  分
    #      * @param msg		祝福语
    #      * @param payPwd	支付密码
    #      */
    #     public static void pushRedPacketGroup(long selfQQ,long fromGroup,long number,long balance,String msg,String payPwd){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 210);
    #         json.put("selfQQ", selfQQ);
    #         json.put("fromGroup", fromGroup);
    #         json.put("number", number);
    #         json.put("balance", balance);
    #         json.put("payPwd", payPwd);
    #         json.put("msg", msg);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #
    #     :return:
    #     """
    #     pass
    #
    # def group_all_member_shutup(self):
    #     """
    #      /**
    #      * 全员禁言
    #      * @param selfQQ
    #      * @param fromGroup
    #      * @param isOpen 0关闭 1开启
    #      */
    #     public static void prohibitSpeakAll(long selfQQ,long fromGroup,long isOpen){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 211);
    #         json.put("selfQQ", selfQQ);
    #         json.put("fromGroup", fromGroup);
    #         json.put("isOpen", isOpen);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #
    #     :return:
    #     """
    #     pass
    #
    # def get_group_list(self, msg):
    #
    #
    #     """
    #     /**
    #      * 获取群列表
    #      * @param selfQQ
    #      */
    #     public static void groupList(long selfQQ){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 212);
    #         json.put("selfQQ", selfQQ);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #     :return:
    #     """
    #     data = {
    #         "msg": msg,
    #         # "fromQQ":1274667113,
    #         "type":212,
    #         "selfQQ": self.self_qq,
    #
    #     }
    #
    #     self.conn.send(str(data).encode('gbk'))
    #     print(self.listen())
    #
    # def query_group_info(self):
    #     """
    #      /**
    #      * 查询群信息
    #      * @param selfQQ
    #      * @param fromGroup
    #      */
    #     public static void selectGroupInfo(long selfQQ,long fromGroup){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 213);
    #         json.put("selfQQ", selfQQ);
    #         json.put("fromGroup", fromGroup);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #
    #     :return:
    #     """
    #     pass
    #
    # def unknow_output_log(self):
    #     """
    #     /**
    #      * 输出日志
    #      * @param msg		日志内容
    #      * @param fontColor	字体颜色
    #      * @param bgColor	背景颜色
    #      */
    #     public static void outputLog(String log,int fontColor,int bgColor){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 301);
    #         json.put("log", log);
    #         json.put("fontColor", fontColor);
    #         json.put("bgColor", bgColor);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #
    #     :return:
    #     """
    #     pass
    #
    # def unknow_query_plugin_data_log(self):
    #     """
    #     /**
    #      * 查询插件数据目录
    #      */
    #     public static void selectPluginPath(){
    #         JSONObject json = new JSONObject();
    #         json.put("type", 302);
    #         Main.clientTest.sendMsg(json.toJSONString());
    #     }
    #
    #
    #     :return:
    #     """

    def listen(self):
        recv_data = self.conn.recv(1024)  # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了
        try:
            url_code = recv_data.decode()  # decode GBK
            receive_dict = json.loads(parse.unquote(url_code))
        except Exception as E:
            print('LISTEN-###json.loads###出问题了\n\t', E)
            print('###url_code###', url_code)
            print('##parse.unquote(url_code)##:\n', parse.unquote(url_code))

            receive_dict = None
        if recv_data:
            return receive_dict
        else:
            print("对方已离线。。")

    def run(self):
        print('###进入交互发送模式,Ctrl+C退出:')
        while True:
            try:
                input_text = '2/群聊消息/1106878273'  # input('输入选择和内容, 用/ 分割:')
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


    def filter(self, dict):
        keys = dict.keys()
        print('')
        try:
            print(f"群:{dict['fromGroupName']}({dict['fromGroup']})中 {dict['fromQQName']}({dict['fromQQ']}"
                  f"triggerQQ{dict['triggerQQ']} triggerQQName:{dict['triggerQQName']}|"
                  f"type:{dict['type']}-msgType:{dict['msgType']}-msgType2:{dict['msgType']}")
        except:
            try:
                if 'fromQQ' in keys:  # TODO: 这里改成特定条件触发回复
                    if result['type'] == 1:  # 如果type 为1 进行私发回复
                        print(f"来自{result['fromQQ']:>12}的1私聊：{result['msg']:<30}")
                        new_msg = f"爸爸，我收到了一条私聊消息: \n有个傻子*{result['fromQQ']}*说：{result['msg']}"
                        # s.private_msg(new_msg, result['fromQQ'])
                    elif result['type'] == 2:  # 如果type 为2 进行群聊回复
                        print(f"来自:{result['fromQQ']:>12}的2群聊 群昵称：{result['fromQQCardName']:>12} |：{result['msg']:<30}")
                        new_msg = f"爸爸，我收到了一条群聊消息: \n有个傻子*{result['fromQQCardName']}*说：{result['msg'][:60]}"
                        # s.group_msg(new_msg, result['fromGroup'])
                else:
                    print('无from字段')

            except:
                print('不符合过滤规则 详见s.filter')
                pass


from pprint import pprint
if __name__ == '__main__':
    s = Interactive("172.16.66.170", 8404, 2154024779)
    s.crte_conn()
    # while True:
    #     try:
    #         result = s.listen()
    #         pprint(result)
    #         print('-'*40)
    #         s.filter(result)
    #         print('='*40)
    #     except Exception as E:
    #         s.close()
    #         raise
    # s.run()
    # s.private_msg('To 127', 1274667113)
    # s.json_msg("233", 1274667113)
    # s.get_group_list('None')
    time.sleep(0.3)
    s.send_group_temporary_msg("临时会话type", 1050382999, 2934289319)
    # for i in range(70,1000):
    #     s.send_group_temporary_msg("临时会话type" + str(i), 1050382999, 2934289319, i)
    #
    #     time.sleep(1)
    # s.group_msg('[@605658506] 我可以发消息找你玩儿', 1050382999)
    # time.sleep(2)
    # s.group_msg('我现在可以重置了哦，重置功能已更新，私聊我即可重置', 470385171)
    # time.sleep(2)
    # s.group_msg('我现在可以重置了哦，重置功能已更新，私聊我即可重置', 931250969)
    # time.sleep(2)
    # s.group_msg('我现在可以重置了哦，重置功能已更新，私聊我即可重置', 1102236132)
    # time.sleep(2)
    # s.group_msg('我现在可以重置了哦，重置功能已更新，私聊我即可重置', 300509597)
    # time.sleep(2)
    s.close()

# requests.get(host + '/sendgroupmsg'.format('函数'))
