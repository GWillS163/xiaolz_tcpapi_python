import requests
import re
import time

def find_url(str):
    result = re.findall(r"((?:http|ftp|https):\/\/[\w\-_]+(?:\.[\w\-_]+)+(?:[\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)", str)
    print(result)
    return result
def get_web_link(url, encode='utf-8',):
    global file_format
    res = requests.get(url)
    res.encoding = encode
    # print(res.text[:800])
    body = res.text
    # body = re.findall(r'<div id="main">[\s\S]*</div>', res.text)[0]
    # pprint(body)
    title = re.findall(r"<title>([\s\S]*)</title>", body)[0]
    all_link = re.findall(
        r"((?:http|ftp|https):\/\/[\w\-_]+(?:\.[\w\-_]+)+(?:[\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)", body)

    print('文章标题:', title)
    print('检测到所有链接，共', len(all_link))
    # pprint(all_link)

    output_lst = []
    un_output_lst = []
    for img in all_link:
        if img[-4:] in file_format:
            # print('检测',format,'==?', img)
            # print('匹配成功了', format, '==', img[-4:])
            output_lst.append(img)   # 添加符合规则的链接
            print('合规链接：', img)
        else:
            # 添加不符合规则的链接
            un_output_lst.append(img)

    output_lst = set(output_lst)
    un_output_lst = set(un_output_lst)
    print('func####解析完毕')
    return (url, title, output_lst, un_output_lst)


def write_to_txt(url, title, output_lst, un_output_lst):
    with open('img_link.txt', 'a+', encoding='utf-8')as f:
        f.write('=' * 20)
        f.write(time.strftime('%Y%m%d_%H:%M', time.localtime()))
        f.write('=' * 20)
        f.write('\n')
        f.write(title)
        f.write(url)
        f.write('\n--------合规链接--------\n')
        f.write(str(len(output_lst)))
        f.write('\n')
        for img in output_lst:
            f.write(img)
            f.write('\n')
        f.write('\n-------不合规链接--------\n')
        f.write(str(len(un_output_lst)))
        f.write('\n')
        for i in un_output_lst:
            f.write(i)
            f.write('\n')
        f.write('\n')
        f.write('\n' * 2)
        print('####文件写入完毕')


def down_file(url, filepath):
    r = requests.get(url)
    file_name = filepath + url.split('/')[-1]
    with open(file_name, "wb") as f:
        f.write(r.content)
    print(file_name, 'OK')

file_format = ['.jpg', '.gif', '.png']

if __name__ == '__main__':

    print('\n\n欢迎使用本解析程序 输入网址，将会查找所有链接，并保存到本目录下的txt中')
    while True:
        n = 1
        try:
            print('===========进入首次运行 配置页=============')


            print('请输入要筛选的url后缀：便于下载,如http://0a.d/a0bl0ck.jpg\n'
                  '>>>默认有', file_format, '回车使用默认配置')
            file_format_input = input('或自行输入以覆盖默认配置使用/分割>>>').split('/')
            if file_format_input:
                file_format = file_format_input

            encode = input('输入浏览器解码方式: utf-8/gbk/ascii >>>')
            filepath = input('输入下载文件存盘路径>>>')

            while True:
                print('\n','='*20)
                print(f'第{n}次运行')
                url = input('输入网址>>>')
                url, title, output_lst, un_output_lst = get_web_link(url, encode)
                write_to_txt(url, title, output_lst, un_output_lst)
                # if n == 1:
                #     print('首次执行完毕，文件格式与编码方式已被记录\n',
                #           file_format, encode, filepath,
                #           '如需修改请按ctrl c')
                print('正在下载')
                for img_link in output_lst:
                    print(img_link, end='>>')
                    down_file(img_link, filepath)
                n += 1
        except KeyboardInterrupt:
            try:
                print('')
                input('Enter回到配置页, Ctrl C 退出')
            except KeyboardInterrupt:
                raise
        except Exception as E:
            print('出现了异常！', E)
