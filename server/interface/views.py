from django.shortcuts import render
from django.http import HttpResponse
import hashlib

token='gaoruihao'
def wechat(request):
    if request.method == 'GET': #微信的接入验证是用GET方法发送到服务器的，而其他方法是用POST发送到服务器的，以此区分
        #从请求中提取关键字
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        #关键字拼装成list并进行排序
        keylist = [];
        keylist.append(token)
        keylist.append(timestamp)
        keylist.append(nonce)
        sortedlist = sorted(keylist, key = str.lower)
        #连接成字符串进行sha1加密
        keystring = sortedlist[0]+sortedlist[1]+sortedlist[2]
        sha1 = hashlib.sha1()
        sha1.update(keystring.encode('ascii'))
        mysignature = sha1.hexdigest()
        #校验加密结果判断是否是正确的服务器请求
        if mysignature == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse('Error')
