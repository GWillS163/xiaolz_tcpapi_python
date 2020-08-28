import requests
import time

send_qwx_url = 'http://172.16.66.170:4000/send?t=1&tos=23&content={}'

fromqq = '2934289319'
togroup = '1106878273'

host = '172.16.66.170'
port = 10429
selfqq = 2154024779
host_port = 'http://' + host + ':' + str(port)


def group_msg(togroup, text, image=''):
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


def private_msg(toqq, text):
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

if __name__ == '__main__':
    group_msg(1106878273, 'http发送3')
    private_msg(1274667113, 'http发送4')