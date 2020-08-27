import time
from client_sender import Interactive
from pprint import pprint

if __name__ == '__main__':
    while True:
        try:
            print('尝试建立连接')
            s = Interactive("172.16.66.170", 8404, 2934289319)
            s.crte_conn()

            print('###进入监听发送模式,Ctrl+C退出:')
            while True:
                # try:
                result = s.listen()
                print("返回的消息为:")
                pprint(result)
                # print('-'*10)
                if result:
                    s.filter(result)
                print('='*20)
        except Exception as E:
            raise
        #             try:
        #                 pprint(result)  # quote2 url_code

        #             except Exception as E:
        #                 print('出现了问题:', E, time.strftime("%Y-%m-%d %H:%m:%s", time.localtime()))
        #                 raise
        #             print('=' * 80)
        #         except Exception as E:
        #             print('注意！出现了问题2！', E)
        #             raise
        #             # input('回车后继续')
        #         time.sleep(1)
        #         print('+1')
        #     s.close()
        #
        # except:
        #     time.sleep(5)
        #     pass
