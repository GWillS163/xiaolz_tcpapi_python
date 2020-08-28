import requests


# 给http://xxx.xxx.com/xxx/#IUhufhd.jpg 的链接和本地路径将下载
def down_file(url, filepath):
    r = requests.get(url)
    file_name = filepath + url.split('/')[-1]
    with open(file_name, "wb") as f:
        f.write(r.content)
    print(file_name, 'OK')
