# -*- coding: utf-8 -*-
# filename: handle.py
import hashlib
import reply
import receive,time
import web,random
from media import Media
from add_text import get_rabbit
from multiprocessing import Process
from threading import Thread
import time,requests,json
from datetime import datetime


def async_thread(f):    
    def wrapper(*args, **kwargs):       
        t = Thread(target=f, args=args, kwargs=kwargs)        
        t.start()
    return wrapper

@async_thread
def send_theme(user,theme,maxtoken):
    url='http://42.192.17.155/back'
    body = {"touser": user, "theme":theme,"time":datetime.now().strftime("%Y%m%d%H%M%S"),"maxtoken":maxtoken}
    data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
    requests.post(url, data=data)

@async_thread
def send_free_chat(user,theme,maxtoken,temperature):
    url='http://42.192.17.155/chat'
    body = {"touser": user, "theme":theme,"time":datetime.now().strftime("%Y%m%d%H%M%S"),"maxtoken":maxtoken,"temperature":temperature}
    data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
    requests.post(url, data=data)

@async_thread
def update_newyear(db,name,pic_id):
    db.query("UPDATE wechat.app_newyear SET used=used+1,picid=CONCAT(picid,',',$pic_id) where gf_id=$name",
    vars={'name':name,'pic_id':pic_id})

@async_thread
def update_newyear_request(db,name):
    db.query("UPDATE wechat.app_newyear SET request=request+1 where gf_id=$name",
    vars={'name':name})

# run python main.py 42.192.17.155:80

class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print ("Handle Post webdata is ", webData)   #后台打日志
            recMsg = receive.parse_xml(webData)
            print(recMsg)
            print(datetime.now().strftime("%Y%m%d%H%M%S"))
            print(1111)
            # t1=datetime.now()
            if isinstance(recMsg, receive.Msg):
                print(2222)
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                # db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')
                # name=toUser
                print(22)
                if recMsg.MsgType == 'text':
                    content='c:\windows\甄科学>AI...\n欢迎进入AI实验室\n\n微信号: Jiavc009,欢迎聊技术、聊创业\n\n灵感和窗花测试已经过期。\n\n这是自动回复。静待人工。'
                    # content=recMsg.Content.decode("utf-8")
                    print(content)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                    #兔年窗花
                    # if content[0:4]=='$窗花$':
                    #     newyearlimit=4
                    #     imagelimit=200
                    #     #更新accounts数据库
                    #     user_record=db.query("SELECT * from wechat.app_newyear where gf_id=$name",vars={'name':name}).cursor._rows
                    #     if len(user_record)==0:
                    #         db.query("INSERT INTO `app_newyear` (`gf_id`, `request`, `used`, `limit`,`picid`,`status`) VALUES ($name,1,0,$newyearlimit,'0',0)",
                    #         vars={'name':name,'newyearlimit':newyearlimit})
                    #         user_used=1
                    #         status=0
                    #     else:
                    #         db.query("UPDATE wechat.app_newyear SET request=request+1 where gf_id=$name",
                    #         vars={'name':name})
                    #         # update_newyear_request(db,name)
                    #         user_used=user_record[0][3]
                    #         status=user_record[0][6]
                        
                    #     if user_used<newyearlimit and status==0:#在limit内，没有生产中图片，生产图片
                    #         db.query("UPDATE wechat.app_newyear SET status=1 where gf_id=$name",
                    #                 vars={'name':name})                            
                    #         add_text_lenth=len(content) if len(content)<=13 else 13 
                    #         add_text=content[4:add_text_lenth]
                    #         path="c:/wechat/photo/"
                    #         with open ("photo/next_id.json",'r') as outfile:
                    #             next_id=json.load(outfile)['next_id']
                    #         if next_id<=imagelimit:

                    #             imagename='r_'+str(next_id)
                    #             pic_id=str(next_id)
                    #             next_id=next_id+1
                    #             with open ("photo/next_id.json",'w') as outfile:
                    #                 json.dump({'next_id':next_id},outfile)
                    #             get_rabbit(add_text,path,imagename)
                    #             filePath = path+"add_"+imagename+".png" 
                    #             mediaType = "image"
                    #             mymedia=Media()
                    #             mediaId=mymedia.upload(filePath, mediaType)
                    #             replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    #             # update_newyear(db,name,pic_id)
                    #             db.query("UPDATE wechat.app_newyear SET used=used+1,picid=CONCAT(picid,',',$pic_id),status=0 where gf_id=$name",
                    #                 vars={'name':name,'pic_id':pic_id})
                    #             return replyMsg.send()
                    #         else:
                    #             reply_content=f'AI实验室>您来晚了，{imagelimit}张兔年AI窗花已经领完,敬请期待AI实验室更多活动。祝兔年快乐!'
                    #             replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #             return replyMsg.send()
                    #     else:#超出limit，回复结束
                    #         if status!=0 and user_used<newyearlimit: 
                    #             reply_content=f'AI实验室>窗花生成中，网络拥堵，请5秒后再提交新命令'
                    #             replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #             return replyMsg.send()
                    #         else:
                    #             if user_used>=newyearlimit:
                    #                 reply_content=f'AI实验室>您的{newyearlimit}次AI窗花领取机会已耗尽,祝兔年快乐!'
                    #                 replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #                 return replyMsg.send()
                    # elif content[0:4]=='$灵感$':
                    #     paper_limit=4
                    #     user_record=db.query("SELECT * from wechat.app_paper where gf_id=$name",vars={'name':name}).cursor._rows
                    #     if len(user_record)==0:
                    #         db.query("INSERT INTO `app_paper` (`gf_id`, `request`, `used`, `limit`, `status`) VALUES ($name,1,0,$paper_limit,0)",
                    #         vars={'name':name,'paper_limit':paper_limit})
                    #         user_used=1
                    #         status=0
                    #     else:
                    #         db.query("UPDATE wechat.app_paper SET request=request+1 where gf_id=$name",
                    #         vars={'name':name})
                    #         user_used=user_record[0][3]
                    #         status=user_record[0][5]
                    #     if user_used<paper_limit and status==0:#在limit内,没有生产中，产生提纲
                    #         db.query("UPDATE wechat.app_paper SET status=1 where gf_id=$name",
                    #                 vars={'name':name})                            
                    #         theme=content[4:]
                    #         send_theme(name,theme,600)
                    #         # if __name__=='__main__':
                    #         #     print(11111)
                    #         #     name=123333
                    #         #     p=Process(target=fuc,args=[name])
                    #         #     p.start()
                    #         reply_content=f'正在生成《{theme}》...\n\n请耐心等够约100秒后发送消息 $提纲$,以获得结果\n\n!!!在此过程中请勿重复发送$灵感$消息'
                    #         replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #             # db.query("UPDATE wechat.app_paper SET used=used+1 where gf_id=$name",
                    #             #     vars={'name':name})
                    #         return replyMsg.send()
                    #     else:#超出limit或生产中，回复等待或结束
                    #         if status!=0 and user_used<paper_limit: 
                    #             reply_content=f'AI实验室>别心急，上一个灵感正在计算中...\n请耐心等够约100秒，再发送消息 $提纲$，以获得结果。\n\n!!!在此过程中请勿发送新的$灵感$消息'
                    #             replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #             return replyMsg.send()
                    #         else:
                    #             if user_used>=paper_limit:
                    #                 reply_content=f'AI实验室>您的{paper_limit}次灵感提纲免费试用已用完，等我有钱买更多算力的时候，欢迎您再来'
                    #                 replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #                 return replyMsg.send()
                    # elif content[0:4]=='$提纲$':
                    #     paper_result=db.query("SELECT result from wechat.paper_result where gf_id=$name",vars={'name':name}).cursor._rows
                    #     if 1==0:#len(paper_result)==0:
                    #         # print('0')
                    #         reply_content='你没有提交灵感请求，请先发送消息:\n$灵感$你的研究主题'
                    #     else:
                    #         user_record=db.query("SELECT * from wechat.app_paper where gf_id=$name",vars={'name':name}).cursor._rows
                    #         if len(user_record)==0:
                    #             reply_content='你没有提交灵感请求，请先发送消息:\n$灵感$你的研究主题'
                    #         else:
                    #             status=user_record[0][5]
                    #             if status==0:
                    #                 paper_result=db.query("SELECT result from wechat.paper_result where gf_id=$name",vars={'name':name}).cursor._rows
                    #                 reply_content=paper_result[-1][0]#"\n\n    说明：本公众号试用仅为AI研究和fun，不含任何商业目的。由于每次计算都需要支付费用给算法公司，我没钱的时候，这个试用就停了'_*。欢迎资助和加入。"
                    #             if status==1:
                    #                 reply_content=f'还在生成中...\n\n请再耐心等候几秒后发送消息 $提纲$,以获得结果\n\n!!!在此过程中请勿重复发送$灵感$消息'

                    #     replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #     return replyMsg.send()                       
                    # elif content[0:4]=="/sp/":
                    #     theme=content[7:]
                    #     mt=int(content[4:7])
                    #     send_theme(name,theme,mt)
                    #     reply_content=f'正在生成《{theme}》...\n\n请耐心等够约x秒后发送消息 $提纲$,以获得结果\n\n!!!在此过程中请勿重复发送$灵感$消息'
                    #     replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #     return replyMsg.send()          
                    # elif content[0:4]=="/ct/":
                    #     theme=content[8:]
                    #     mt=int(content[4:7])
                    #     tt=round(int(content[7:8])/10,1)
                    #     send_free_chat(name,theme,mt,tt)
                    #     reply_content=f'正在生成回复...\n\n请耐心等够约x秒后发送消息 $提纲$,以获得结果\n\n!!!在此过程中请勿重复发送$灵感$消息'
                    #     replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #     return replyMsg.send()                    
                    # else:
                    #     reply_content = "c:\windows\甄科学>AI\n消息命令不精确，请检查是否输入了精确的以 $ 引导的消息命令\n\n如果是其他问题,请等待人工回复"
                    #     replyMsg = reply.TextMsg(toUser, fromUser, reply_content)
                    #     return replyMsg.send()
                if recMsg.MsgType == 'event':
                    if recMsg.Event=='subscribe':      
                       content='c:\windows\甄科学>AI...\n欢迎进入AI实验室\n\n微信号: Jiavc009,欢迎聊技术、聊创业\n\n灵感和窗花测试已经过期'
                       print(content)
                       replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                    return replyMsg.send()
                # else:
                #     return reply.Msg().send()
            else:
                print ("暂且不处理")
                return reply.Msg().send()
        except Exception as Argment:
            return Argment

# db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')

# content="$兔年$abdcedw我的weod"
# x=content[0:4]
# name='aaaaa'

# if content[0:4]=='$兔年$':
#     newyearlimit=400
#     if len(db.query("SELECT * from wechat.app_newyear where gf_id=$name",vars={'name':name}).cursor._rows)==0:
#         db.query("INSERT INTO `app_newyear` (`gf_id`, `request`, `used`, `limit`) VALUES ($name,0,0,$newyearlimit)",
#         vars={'name':name,'newyearlimit':newyearlimit})
#     else:
#         db.query("UPDATE wechat.app_newyear SET used = used+1,request=request+1 where gf_id=$name",
#         vars={'name':name})

# c=1