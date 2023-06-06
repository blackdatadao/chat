# -*- coding: utf-8 -*-
# filename: handle.py

import web,json
from media import Media
from add_text import get_rabbit
from paper import get_paper,get_free_chat

# run python main.py 42.192.17.155:80

def add_record_to_json(json_path,question,answer):
    record={"ask":question,"answer":answer}
    with open(json_path,'r',encoding='utf-8') as f:
        data=json.load(f)
    data.append(record)
    with open(json_path,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=4)

class Back(object):
    def POST(self):
        # try:
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        gf_id=webData['touser']
        theme=webData['theme']
        time=webData['time']
        maxtoken=webData['maxtoken']
        db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')
        result=get_paper(theme,maxtoken)
        db.query("INSERT INTO `paper_result` (`gf_id`, `time`, `theme`, `result`) VALUES ($gf_id,$time,$theme,$result)",
                        vars={'gf_id':gf_id,'time':time,'theme':theme,'result':result})
        db.query("UPDATE wechat.app_paper SET status=0,used=used+1 where gf_id=$name",
                vars={'name':gf_id})  

class Back2(object):
    def POST(self):
        # try:
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        gf_id=webData['touser']
        theme=webData['theme']
        time=webData['time']
        maxtoken=webData['maxtoken']
        temperature=webData['temperature']
        db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')
        result=get_free_chat(theme,maxtoken,temperature)
        db.query("INSERT INTO `paper_result` (`gf_id`, `time`, `theme`, `result`) VALUES ($gf_id,$time,$theme,$result)",
                        vars={'gf_id':gf_id,'time':time,'theme':theme,'result':result})
        db.query("UPDATE wechat.app_paper SET status=0,used=used+1 where gf_id=$name",
                vars={'name':gf_id})

        
class Back2(object):
    def POST(self):
        # try:
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        gf_id=webData['touser']
        theme=webData['theme']
        time=webData['time']
        maxtoken=webData['maxtoken']
        temperature=webData['temperature']
        db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')
        result=get_free_chat(theme,maxtoken,temperature)
        db.query("INSERT INTO `paper_result` (`gf_id`, `time`, `theme`, `result`) VALUES ($gf_id,$time,$theme,$result)",
                        vars={'gf_id':gf_id,'time':time,'theme':theme,'result':result})
        db.query("UPDATE wechat.app_paper SET status=0,used=used+1 where gf_id=$name",
                vars={'name':gf_id})

class Back_chat_record_my(object):
    def POST(self):
        # try:
        
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        question=webData['question']
        answer=webData['answer']
        add_record_to_json('chat_record_timothy.json',question,answer)
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        with open ('chat_record_timothy.json','r',encoding='utf-8') as f:
            data=json.load(f)
        return json.dumps(data, ensure_ascii=False)
        
class Back_chat_record_liu(object):
    def POST(self):
        # try:
        web.header('Content-Type','application/json; charset=utf-8')
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        question=webData['question']
        answer=webData['answer']
        add_record_to_json('chat_record_liu.json',question,answer)
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        with open ('chat_record_liu.json','r',encoding='utf-8') as f:
            data=json.load(f)
        return bytes(json.dumps(data, ensure_ascii=False).encode('utf-8'))

class Back_nft_list(object):
    def POST(self):
        # try:
        web.header('Content-Type','application/json; charset=utf-8')
        webData = eval(web.data().decode("utf-8"))
        print ("Handle Post webdata is ", webData)   #后台打日志
        with open('nft_list.json','w',encoding='utf-8') as f:
            json.dump(webData,f,ensure_ascii=False,indent=4)
    def GET(self):
        web.header('Content-Type','application/json; charset=utf-8')
        with open ('nft_list.json','r',encoding='utf-8') as f:
            data=json.load(f)
        return bytes(json.dumps(data, ensure_ascii=False).encode('utf-8'))
         
# except Exception as Argment:
        #     return Argment

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