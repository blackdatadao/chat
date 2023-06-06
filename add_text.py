# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2,math
from datetime import datetime
import time
# #设置字体，如果没有，也可以不设置
# font = ImageFont.truetype("arial.ttf",32,encoding="utf-8")
# font = ImageFont.truetype("simkai.ttf",62)
# font = ImageFont.truetype(font="msyhl.ttc",size=32)

# #打开底版图片
# imageFile = "1.png"
# tp=Image.open(imageFile)

# # 在图片上添加文字 1
# draw = ImageDraw.Draw(tp)
# text="测试"
# print(text.encode('latin-1'))
# draw.text((100, 100),text.encode('latin-1'),(255,255,0))

# # 保存
# name=datetime.now().strftime("%m%d%Y%H%M%S")

# tp.save(name+".png")


def cv2AddChineseText(img, text, position, fontpath, textColor=(0, 255, 0), textSize=60):

    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        fontpath, textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position,text,textColor,font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def get_font_size(img_fraction, photo, text, fontsize, font_path):
    """摘自Nachtalb的回答https://cloud.tencent.com/developer/ask/sof/87148
    获取给定图片比例下的最合适大小
    """
    font = ImageFont.truetype(font_path, fontsize)
    # 输入photo [height, width, channel]
    breakpoint = img_fraction * photo.shape[1]
    jumpsize = 10
    while True:
        # font.getsize() 可以获得当前文本所占图片大小，维度是[width, height]
        # 用二分查找的方式搜索在给定比例下的最合适的size
        if font.getsize(text)[0] < breakpoint and fontsize<18:
            fontsize += jumpsize
        else:
            jumpsize = jumpsize // 2
            fontsize -= jumpsize
        font = ImageFont.truetype(font_path, fontsize)
        if jumpsize <= 1:
            break
    return fontsize, font.getsize(text)


def get_rabbit(text,path,imagename):
    if len(text)>0:
        font_path = "C:\Windows\Fonts\simkai.TTF"
        # 注意用numpy生成空白图片时，类型必须为np.uint8
        imgwidth = 512
        imghight=512
        imgbotton=75
        imageFile = path+imagename+".png"
        img=cv2.imread(imageFile)
        # font从1开始
        fontsize, font_region = get_font_size(img_fraction=0.2, photo=img,
                                                text=text, fontsize=1,
                                                font_path=font_path)
        img2 = np.ones((100, 512, 3), dtype=np.uint8) * 255 #bottom
        img2 = cv2AddChineseText(img2, text, position=(round((imgwidth-font_region[0])/2),round((imgbotton-font_region[1])/2)), textColor=(0,0,0),
                                    textSize=fontsize, fontpath=font_path)
        #img=np.concatenate((img,img2))
        img = cv2AddChineseText(img, text, position=(round((imgwidth-font_region[0]-50)),460), textColor=(0,0,0),
                                    textSize=fontsize, fontpath=font_path)
    else:
        imageFile = path+imagename+".png"
        img=cv2.imread(imageFile)
    outFile=path+'add_'+imagename+".png"
    cv2.imwrite(outFile,img)
    # print("add text success")

# text = f'某111AI作品'
# path="c:/wechat/photo/"
# imagename='rabbit_1'
# get_rabbit(text,path,imagename)


