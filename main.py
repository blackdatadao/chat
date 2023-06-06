# -*- coding: utf-8 -*-
# filename: main.py
#run python main.py 42.192.17.155:80
#run python main.py 18.178.47.106:80
#install pillow opencv-python
import web
from handle_2_0 import Handle
from back_2_0 import Back,Back2,Back_chat_record_my,Back_chat_record_liu,Back_nft_list

urls = (
    '/wx', 'Handle',
    '/back','Back',
    '/chat','Back2',
    '/chat_record_my','Back_chat_record_my',
    '/chat_record_liu','Back_chat_record_liu',
    '/nft_list','Back_nft_list',
    
)

class index:
    def GET(self):
        return "Hello, world!"
class Myapplication(web.application):
    def run (self,port=80,*middleware):
        func=self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func,('0.0.0.0',port))

if __name__ == "__main__":
    app = Myapplication(urls, globals())
    app.run(port=80)
    #web.httpserver.runsimple(app.wsgifunc(),("42.192.17.155",8080))
    #web.httpserver.runsimple(app.wsgifunc(),("localhost",8080))