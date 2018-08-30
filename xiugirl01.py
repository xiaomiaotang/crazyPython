import re
import requests
import urllib
# 显示进度的包
from tqdm import tqdm
import os


g_url = 'http://www.xiugirls.com/girl/?p='
single_girl = 'http://www.xiugirls.com/girl/'
album_url = 'http://www.xiugirls.com/album/'
start_url = 'http://www.xiugirls.com/album/hd/?p='

headers ={'Host': 'www.xiugirls.com',
         'Referer': 'http://www.xiugirls.com/news/',
         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36'
                       ' (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}
# 保存地址
path = 'D:/home/xiu/'
err_list = []

# 1.获取所有页面的美女姓名和path，保存在列表中
girls_list = []
for i in range(1,10):
    url = g_url + str(i)
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    # print(text)
    pattern = re.compile('href="/girl/(\d+)"\s+?title="(.*?)"\s',re.S)
    list = re.findall(pattern,text)
    for i in list:
        girls_list.append(i)
# print(girls_list)
# 2.根据所有path组合成新的url，进入个人资料页面，获取个人资料，保存成文本。获取所有专辑path列表。
for u in girls_list:
    url = single_girl + u[0]
    # print(url)
    r = requests.get(url,headers=headers)
    t = r.content.decode('utf-8')
    girl_name = u[1]
    if os.path.exists(path + girl_name):
        print(girl_name,'已经存在，跳过')
        flag = 1
        continue
    else:
        os.mkdir(path+girl_name)
        print('创建%s文件夹' % girl_name)
        flag = 0
    if flag == 0 :
        os.chdir(path+ girl_name)
        # 1.获取个人资料并保存在TXT文本中
        # 个人资料
        info_pattern = re.compile("<li><span class='bas-title'>(.*?)</span><span class='bas-cont'>(.*?)</span></li>",
                                  re.S)
        info_list = re.findall(info_pattern,t)
        girls_info_txt = u[1]+'.txt'
        with open(girls_info_txt,'w',encoding='utf-8') as txt:
            for i in info_list:
                txt.write(i[0]+':'+i[1]+'\n')

        # 2.收集套图path
        set_parttern = re.compile('href="/album/(\d+)"\s+?title=".*?"\s',re.S)
        # 套图路径列表
        set_pic_list = re.findall(set_parttern,t)
        for u in set_pic_list:
            # 套图详情页url
            url = album_url + str(u)

            # 根据url进入套图详情页，获取title和图片url列表

            rs = requests.get(url,headers= headers)
            ct = rs.content.decode('utf-8')

            # 套图title
            titile_pattern = re.compile('<title>(.*?)</title>',re.S)
            set_title = re.sub('[/:*"<>|？\(女神私房照_秀色女神\)]','',re.findall(titile_pattern,ct)[0])
            # print(set_title)
            # 创建套图文件夹
            if os.path.exists(path + girl_name + "/" + set_title ):
                print(set_title,'已经存在')
                flags = 1
            else:
                os.mkdir(path + girl_name + "/" + set_title)
                flags = 0
                print('创建新的文件夹：',set_title)
            # 改变文件夹路径，准备写入图片
            os.chdir(path + girl_name + "/" + set_title)

            # 获取图片url列表
            pic_pattern = re.compile("src='(//img.*?)'", re.S)
            url_list = re.findall(pic_pattern,ct)

            for url in tqdm(url_list):
                pic_name = url.replace('/', '')[-17:]
                print('正在保存：' + url)
                urllib.request.urlretrieve('http:' + url, pic_name)

