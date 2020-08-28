import requests
import time

# 2020年8月28日, 10点10分
# 注意,本代码通过httpapi与 QQ_bot 进行交互.
# !!!!!!!! 功能不完整!!!!!!!!!!!


send_qwx_url = 'http://172.16.66.170:4000/send?t=1&tos=23&content={}'
# send_msg_url
# send_pic_url

def group_msg(text, togroup, image=''):
    url = host_port + '/sendgroupmsg'
    data = {
            'fromqq': selfqq,  # 2154024779,
            'togroup': togroup, # 1106878273,
            'text': text,
            'fromtype': 2 if image else '',
            'path': image if image else '',
            'url': image if image else '',
    }

    try:
        s = requests.post(url, data)
        s = requests.get(host_port + '/send?t=1&tos=23&content={}'.format(text))
    except Exception as E:
        s = False
        print(E)
    time.sleep(1)
    return s


def private_msg(text, toqq):
    url = host_port + '/sendprivatemsg'
    data = {
            'fromqq': selfqq,  # 2154024779,
            'toqq': toqq,  # 1106878273,
            'text': text,
    }
    try:
        s = requests.post(url, data)
        # s = requests.get(host_port + '/send?t=1&tos=23&content={}'.format(text))
    except Exception as E:
        s = False
        print(E)
    time.sleep(1)
    return s


def group_temporary(text, toqq, togroup):
    """
    :param text:
    :param 给哪个 QQ:
    :param 你们在哪个组?:
    :return:
    """
    url = host_port + '/sendgrouptempmsg'
    data = {
            'fromqq': selfqq,  # 2154024779,
            'togroup': togroup,
            'toqq': toqq,  # 1106878273,
            'text': text,
    }
    try:
        s = requests.post(url, data)
    except Exception as E:
        s = False
        print(E)
    time.sleep(1)
    return s


def get_buffer():
    url = host_port + '/allocsession'
    try:
        s = requests.post(url, '')
        print(s)
    except Exception as E:
        print(E)


# def get_event2(toqq, text):
#     url = host_port + '/sendprivatemsg'
#     data = {
#             'fromqq': selfqq,  # 2154024779,
#             'toqq': toqq, # 1106878273,
#             'text': text,
#     }
#     try:
#         s = requests.post(url, data)
#         # s = requests.get(host_port + '/send?t=1&tos=23&content={}'.format(text))
#     except Exception as E:
#         s = False
#         print(E)
#     time.sleep(1)
#     return s

def auto_accept():
    url = host_port + '/setfriendaddrequest'

    HEADERS = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'fromqq': selfqq,  # 2154024779,
        'qq': '782659451',
        'seq': '',
        'op': 1,
    }
    try:
        s = requests.post(url, data)
        # s = requests.get(host_port + '/send?t=1&tos=23&content={}'.format(text))
    except Exception as E:
        s = False
        print(E)
    time.sleep(1)
    return s

if __name__ == '__main__':
    fromqq = 2934289319   # 发送至哪个QQ
    togroup = 1106878273  # 发送至哪个群

    host = '172.16.66.170'
    port = 10429
    selfqq = 2154024779
    host_port = 'http://' + host + ':' + str(port)

    group_msg(1106878273, 'http发送群聊!')
    private_msg(1274667113, 'http发送私聊')
    # get_buffer()
    group_temporary('群临时消息', fromqq, togroup)
    # while True:
    #     requests.get(get, )
    # auto_accept()
