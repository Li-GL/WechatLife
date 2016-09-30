# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import requests
import os
import urllib
import urllib2
import json
from lxml import etree
import cookielib
import re
import random


class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr = data.echostr
        #自己的token
        token="lglfa666" #
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析

        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text

        if msgType =="event":

            msg = xml.find('Event').text
            if msg =="subscribe":
                return self.render.reply_text(fromUser,toUser,int(time.time()), u"■ 发送全国各地城市县区的拼音返回当天前详细天气，香港请发HongKong\n\n■ 发送“香港”和“北京”可返回近五日天气；\n\n\
■ 发送“段子”随机返回一条糗百top50的段子;\n\n■ “音乐”随机返回一首精选的歌，点播放三角播放;\n\n■ 其他任何中文关键词可以和中文机器人聊天;\n\n■ 其他任何英文关键词可以和英文机器人聊天;\n\n\
■ “图片”+关键词返回图片，“图片猫”返回猫有关的图片链接")

        if msgType=="text":

            content = xml.find("Content").text  # 获得用户所输入的内容

            if(content == u"天气" or content == u"北京" or content == u"北京天气"):
                url = "http://m.ip138.com/10/tianqi/"
                headers = {
                    'Connection': 'Keep-Alive',
                    'Accept': 'text/html, application/xhtml+xml, */*',
                   'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
                req = urllib2.Request(url, headers = headers)
                opener = urllib2.urlopen(req)
                html = opener.read()
                opener.close()
                rex = r'(?<=/>).{1,40}(?=</div><div class="temperature">)'
                rexx = r'(?<=div class="temperature">).{5,15}(?=</div>)'
                rexxx = r'(?<=<div class="date">).{1,6}'
                n = re.findall(rex,html)
                m = re.findall(rexx,html)
                d = re.findall(rexxx,html)
                str_wether = ""
                for (l,i,j) in zip(m,n,d):
                    str_wether =str_wether+ j +" "+ i + "  " +l + "\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),"北京五日天气:\n"+str_wether)

            elif(content == u"香港" or content == u"HK" or content == u"香港天气"):
                url = "http://m.ip138.com/xianggang/tianqi/"
                headers = {
                    'Connection': 'Keep-Alive',
                    'Accept': 'text/html, application/xhtml+xml, */*',
                   'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
                req = urllib2.Request(url, headers = headers)
                opener = urllib2.urlopen(req)
                html = opener.read()
                opener.close()
                rex = r'(?<=/>).{1,40}(?=</div><div class="temperature">)'
                rexx = r'(?<=div class="temperature">).{5,15}(?=</div>)'
                rexxx = r'(?<=<div class="date">).{1,6}'
                n = re.findall(rex,html)
                m = re.findall(rexx,html)
                d = re.findall(rexxx,html)
                str_wether = ""
                for (l,i,j) in zip(m,n,d):
                    str_wether =str_wether+ j +" "+ i + "  " +l + "\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),"香港五日天气:\n"+str_wether)
            elif(content == u"曹县" or content == u"曹县天气" or content == u"CX"):
                url = "http://m.ip138.com/25/heze/caoxian/tianqi/"
                headers = {
                    'Connection': 'Keep-Alive',
                    'Accept': 'text/html, application/xhtml+xml, */*',
                   'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
                req = urllib2.Request(url, headers = headers)
                opener = urllib2.urlopen(req)
                html = opener.read()
                opener.close()
                rex = r'(?<=/>).{1,40}(?=</div><div class="temperature">)'
                rexx = r'(?<=div class="temperature">).{5,15}(?=</div>)'
                rexxx = r'(?<=<div class="date">).{1,6}'
                n = re.findall(rex,html)
                m = re.findall(rexx,html)
                d = re.findall(rexxx,html)
                str_wether = ""
                for (l,i,j) in zip(m,n,d):
                    str_wether =str_wether+ j +" "+ i + "  " +l + "\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),"曹县五日天气:\n"+str_wether)

            elif(content == u"不开心" or content == u"段子" or content == u"我不开心"):

                url_24 = "http://www.qiushibaike.com/hot/"
                url_2= "http://www.qiushibaike.com/hot/page/2/?s=4916900"
                headers = {
                    'Connection': 'Keep-Alive',
                    'Accept': 'text/html, application/xhtml+xml, */*',
                   'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}

                req_24 = urllib2.Request(url_24,headers = headers)

                opener_24 = urllib2.urlopen(req_24)

                html_24 = opener_24.read()

                opener_24.close()

                req_2 = urllib2.Request(url_2, headers=headers)
                opener_2 = urllib2.urlopen(req_2)
                html_2 = opener_2.read()
                opener_2.close()
                rex = r'<div class="content">\n*<span>(.{40,500})</span>\n*</div>\n</a>'
                m_2 = re.findall(rex, html_2, re.S)
                m_24 = re.findall(rex, html_24, re.S)
                m_total = m_2 + m_24
                random.shuffle(m_total)
                return self.render.reply_text(fromUser, toUser, int(time.time()), re.sub('<br/>', '', m_total[0]))

            elif(content[0:2] == u"快递"):
                keyword = content[2:]
                url = "http://www.kuaidi100.com/autonumber/autoComNum?text="+keyword
                cj = cookielib.CookieJar()
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
                opener.addheaders = [('User-agent','Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0')]
                urllib2.install_opener(opener)
                html = urllib2.urlopen(url).read()
                jo = json.loads(html)
                typ = jo["auto"][0]['comCode']
                if(typ is None):
                    return self.render.reply_text(fromUser,toUser,int(time.time()),u"请检查你的定单号！")
                urll = "http://www.kuaidi100.com/query?type="+typ+"&postid="+keyword
                html_end = urllib2.urlopen(urll).read()
                jo_end = json.loads(html_end)
                if(jo_end["status"] == "201"):
                    return self.render.reply_text(fromUser,toUser,int(time.time()),u"订单号输入有误，请重新输入！")
                text = jo_end["data"]
                string = u""
                for i in text:
                    string = string + i["time"] + i["context"] + "\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),string)
            elif(content == u"微博热点"):
                url = "http://weibo.cn/pub/?tf=5_005"
                headers = {
                            'Connection': 'Keep-Alive',
                            'Accept': 'text/html, application/xhtml+xml, */*',
                           'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
                req = urllib2.Request(url, headers = headers)
                opener = urllib2.urlopen(req)
                html = opener.read().decode("utf-8")
                rex = r'(?<=div class="c"><a href=").{60,79}(?=</a>)'
                ss = re.findall(rex,html)
                string = u""
                for i in ss:
                    string = string + i.replace('>','\n')+"\n"
                return self.render.reply_text(fromUser,toUser,int(time.time()),string.replace('"',''))

            elif(content[0:2]==u"图片"):
                content_t = content[2:]
                content_t = content_t.encode('utf8')
                url = "http://www.bing.com/images/search?q="+urllib2.quote(content_t)+"&FORM=HDRSC2"
                opener = urllib.urlopen(url)
                html = opener.read()
                reg = r'(?<=href=")(http.{20,200}.jpg)"(?= h="ID=images)'
                imgre = re.compile(reg)
                imglist = imgre.findall(html)
                randomInt = random.randint(1,10)
                imgurl = imglist[randomInt]
                return self.render.reply_text(fromUser,toUser,int(time.time()),imgurl)

            #####音乐
            elif (content == u"音乐" or content == u'Music' or content == u"music"):
                with open('music.txt', 'r') as f:
                    data = f.readlines()
                random.shuffle(data)
                music = data[1].split('\t')

                musictitle = music[0]
                musicdes = music[1]
                musicurl = music[2].rstrip('\n')

                return self.render.reply_music(fromUser, toUser, int(time.time()), musictitle,musicdes,musicurl)
                # with open('music.txt', 'r') as f:
                #     data = f.readlines()
                #
                # music = [i.split('\t') for i in data]
                # for i in music:
                #     musictitle = i[0]
                #     musicdes = i[1]
                #     musicurl = i[2].rstrip('\n')
                #     return self.render.reply_music(fromUser, toUser, int(time.time()), musictitle, musicdes, musicurl)




            elif(u"李国梁" in content):
                return self.render.reply_text(fromUser,toUser,int(time.time()),u"找全世界最帅的人干嘛？")
            elif(content==u"杨晓" or content==u"小羊" ):
                return self.render.reply_text(fromUser,toUser,int(time.time()), r"宝宝爱你哦")
            else:

                try:
                    url = "http://apis.baidu.com/apistore/weatherservice/weather?citypinyin="
                    city = content
                    # 完整api访问接口
                    url = url + city
                    req = urllib2.Request(url)
                    # 给定header
                    # 这里注意填写自己的apikey
                    req.add_header("apikey", "2c967fe4a5c591dcbd03acbf80f7f679")
                    resp = urllib2.urlopen(req)
                    readcontent = resp.read()

                    # 通过json的loads将获得数据内容转换成python对象
                    info = json.loads(readcontent);

                    weather_data = u"城市：" + info['retData']['city'] + '\n' + u"查询日期：" + info['retData']['date'] \
                               + '\n' + u"最新预报时间：" + info['retData']['time'] + '\n' + u"天气：" + info['retData'][
                                   'weather'] \
                               + '\n' + u"气温：" + info['retData']['l_tmp'] + u'℃' + u' ~ ' + info['retData'][
                                   'h_tmp'] + u'℃' + '\n' \
                               + u"风向：" + info['retData']['WD'] + '\n' + u"风力：" + info['retData']['WS'] + '\n' \
                               + u"日出时间：" + info['retData']['sunrise'] + '\n' + u"日落时间：" + info['retData']['sunset']+ '\n' + u"海拔：" + info['retData']['altitude'] +' m'
                    return self.render.reply_text(fromUser, toUser, int(time.time()), weather_data)
                except:
                    if content[0] >= u'\u4e00' and content[0] <= u'\u9fa5':

                        content = content.encode('utf8')
                        url = "http://www.xiaodoubi.com/simsimiapi.php?msg=" + content
                        opener_auto = urllib2.urlopen(url)

                        html_auto = opener_auto.read()
                        opener_auto.close()

                        return self.render.reply_text(fromUser, toUser, int(time.time()), html_auto)

                    elif ord(content[0]) < 127:

                        content = content.encode('utf8')
                        url = "http://lwons.com/aiml?req=" + urllib.quote(content)
                        opener_auto = urllib2.urlopen(url)

                        html_auto = opener_auto.read()
                        opener_auto.close()

                        return self.render.reply_text(fromUser, toUser, int(time.time()), str(html_auto))






 




