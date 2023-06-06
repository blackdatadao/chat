# -*- coding: utf-8 -*-
# filename: media.py
from basic import Basic
import json
import requests,web
from datetime import datetime
from datetime import timedelta

def get_access_token_database():
    db = web.database(dbn='mysql', db='wechat', user='root',pw='12345678')
    results = db.query("SELECT * from wechat.token where id=1").cursor._rows
    exp_time_date=datetime.strptime(results[0][2],"%Y%m%d%H%M%S")
    # print(exp_time_date)
    if datetime.now()<exp_time_date-timedelta(0,20):
        accessToken=results[0][1]
        return accessToken
    else:
        accessToken,exp_in = Basic().get_access_token()
        exp_time_str=(datetime.now()+timedelta(0,exp_in)).strftime("%Y%m%d%H%M%S")
        db.query("UPDATE wechat.token SET token=$actoken,exptime=$exp_time_str where id=1",
            vars={'actoken':accessToken,'exp_time_str':exp_time_str})
        return accessToken

class Media(object):
    def __init__(self):
        pass
    
    # 上传图片
    def upload(self,filePath, mediaType):
        # t1=datetime.now()
        accessToken = get_access_token_database()
        # print('actoken',datetime.now()-t1)
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (
            accessToken, mediaType)
        myfile={'media':open(filePath,'rb')}
        post_hearders={'Content-Type': 'multipart/form-data; boundary=b73eac9914d348748d52cd9027b245e9', 'Content-Length': '542908'}
        x=requests.post(postUrl,files=myfile)
        # print('uploadpic',datetime.now()-t1)
        return eval(x.text)['media_id']
        
    def get(self, mediaId):
        accessToken = get_access_token_database()
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (
            accessToken, mediaId)
        
        urlResp = requests.get(postUrl)

        headers = urlResp.headers
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print (jsonDict)
        else:
            buffer = urlResp._content  # 素材的二进制
            mediaFile = open("test_media.jpg", "wb")
            mediaFile.write(buffer)
            print ("get successful")

        # req = urllib.request.Request(self.PATH_ATTACHMENTS, datagen, headers)
        #     res = requests.post(postUrl, headers={'Content-Type': encoderr.content_type}, data=encoderr)
        #     print (res.json())

# if __name__ == '__main__':
#     myMedia = Media()
#     path = 'c:/wechat/'
#     filename = '3.png'
#     filePath = path+filename  # 请按实际填写
#     mediaType = "image"
#     mediaId=myMedia.upload(filePath, mediaType)
#     print(mediaId)
#     c=1
#     # mediaId = "cYwZa4_O9U2YfkyHO-oNsBsHPcqEdZFr_mD0H7PufLuMTUMJU-ryIYv7nvKp7DPR"
#     # myMedia.get(accessToken, mediaId)
