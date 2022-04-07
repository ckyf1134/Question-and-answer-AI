#制作人ckyf1134.
#做这个人工智能用时很长，自己导入和创造了很多语料库。 
#名字：Lemon，性别女
#训练不了，没服务器。
#也不准备引入训练。全引用语料库手动添加变量。
#ps（夹 带 私 货）：我知道柠檬有“酸”的意思，但是一开始纯粹觉得好听，“酸”根本没考虑......
print('正在启动，请稍后......')
print('启动成功，正在初始化')
#引用库
import re
import telnetlib
import requests
import datetime
import os
import sys
#进行天气的获取
r = requests.get('http://www.weather.com.cn/data/sk/101030100.html')
r.encoding = 'utf-8'
weatherdata=r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'],r.json()['weatherinfo']['AP']
weatherdata1=str(weatherdata) 
weatherdata1 = str(weatherdata1.replace("(","").replace(")","").replace("'",""))
def clear():os.system('cls')
print('正在尝试连接网络......')
def weather():
        r = requests.get('http://www.weather.com.cn/data/sk/101030100.html')
        r.encoding = 'utf-8'
        weatherdata=r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp'],r.json()['weatherinfo']['AP']
        weatherdata1=str(weatherdata) 
        weatherdata1 = str(weatherdata1.replace("(","").replace(")","").replace("'",""))
return1=os.system('ping www.baidu.com')
if return1 == 0:
    print('联网成功!天气正在初始化.......')
    print('天气初始化成功......')
    print('[ID:Y2t5ZjExMzQ=],[Type=Base64]')
    num1=1
else:
    print('尝试连接......') 
    print('联网失败，天气功能将使用受限')
    num1=2
if num1 ==1:
    print('联网成功！')
else:
    print('联网失败......天气功能将使用受限.......')
if num1 == 1:
    weather()
else:
    print('无网络，天气功能初始化失败......')
    weatherdata1=str('无数据')
clear()
print('你好，我是Lemon！')
while (1):
    time=datetime.datetime.now()
    speak=input('你:')
    weather1='天气'
    timesay='时间'
    exit='再见'
    me='你是谁'
    timesay2='几点'
    rewea='重载网络模块'
    sysmod='打开系统设置'
    resys='重启Lemon'
    sorry='对不起'
    thank='谢谢'
    nothing='没关系'
    huozhuo='焯'
    hello='你好'
    if weather1 in speak:
        print("Lemon:"+weatherdata1)
    elif timesay in speak:
        print("Lemon:"+'现在是'+str(time))
    elif exit in speak:
        print("Lemon:"+"再见。")
        print("Lemon正在关闭......")
        print('Lemon已关闭。')
        sys.exit(0)
    #这里是退出的意思！！！
    elif me in speak:
        print("Lemon:"+'我是Lemon,很高兴认识你!')
    elif hello in speak:
        print("Lemon:"+'你好！')
    elif sorry in speak:
        print("Lemon:"+'没关系。')
    elif nothing in speak:
        print("Lemon:"+'谢谢啦......')
    elif thank in speak:
        print("Lemon:"+'不用谢！')
    elif huozhuo in speak:
        print('哥谭噩梦：我好不容易心动一次，你却让我输的，这么彻底，哈哈哈哈哈哈哈，焯！')
    elif timesay2 in speak:
        print("Lemon:"+'现在是'+str(time))
    elif sysmod == speak:
        print('已进入调试模式，模式下所有指令采用严格模式。')
        print('严格模式下指令需要完全正确。')
        speak1=input("System:"+'请输入系统指令:')
        if rewea == speak1:
            weather()
            print("[@]System:"+'模块重载成功!')
        elif resys == speak1:
            weather()
        else:
             print('System:不是正确的系统指令，已返回正常模式......')
    else:
        print("Lemon:"+'我没有理解...我还不知道这么多呢...对不起...')
   
