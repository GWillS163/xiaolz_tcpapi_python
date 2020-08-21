import time
from client_sender import Interactive
from pprint import pprint

if __name__ == '__main__':
    s = Interactive("172.16.66.170", 8404, 2934289319)
    s.crte_conn()

    print('###进入监听发送模式,Ctrl+C退出:')
    while True:
        try:
            result = s.listen()
            print("返回的消息为:")
            pprint(result)  # quote2 url_code

            if 'fromQQ' in result.keys():  # TODO: 这里改成特定条件触发回复
                if result['type'] == 1:     # 如果type 为1 进行私发回复
                    print(f"来自{result['fromQQ']:>12}的1私聊：{result['msg']:<30}")
                    new_msg = f"爸爸，我收到了一条私聊消息: \n有个傻子*{result['fromQQ']}*说：{result['msg']}"
                    s.private_msg(new_msg, result['fromQQ'])
                elif result['type'] == 2:  # 如果type 为2 进行群聊回复
                    print(f"来自:{result['fromQQ']:>12}的2群聊 群昵称：{result['fromQQCardName']:>12} |：{result['msg']:<30}")
                    new_msg = f"爸爸，我收到了一条群聊消息: \n有个傻子*{result['fromQQCardName']}*说：{result['msg']}"
                    s.group_msg(new_msg, result['fromGroup'])
            else:
                print('无from字段')
            print('=' * 80)
        except KeyboardInterrupt:
            try:
                input('用户中断: Ctrl+C终止/Enter继续')
            except KeyboardInterrupt:
                break
        except Exception as E:
            print('注意！输入出现了问题！', E)
            input('回车后继续')
        time.sleep(1)
        print('次数-1')
    s.close()
