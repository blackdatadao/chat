# -*- coding: utf-8 -*-
import os
import openai,requests,json
from datetime import datetime
from sys import getsizeof

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def create_outline(theme,max_tokens):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="用中文写一个关于以下主题的论文提纲:"+theme+"，提纲包括四部分，每部分有三个小节,不超过300字。",
    temperature=0.3,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    outlines=response['choices'][0]['text']
    #print(response['usage'])
    return outlines

def free_chat(prompt,max_tokens,temperature):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    outlines=response['choices'][0]['text']
    #print(response['usage'])
    return outlines


def create_new_development(theme,max_tokens):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="用中文写一个关于以下主题的最新研究进展:"+theme+",包含三条",
    temperature=0.5,
    max_tokens=max_tokens,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    r=response['choices'][0]['text']
    #print(response['usage'])
    return r


def get_paper(theme,max_tokens):
    error_infor='恭喜你中彩票了，机器人碰到问题，原因可能是：\n\n1.你的研究主题中含标点、英文、中英文混排、特殊字符、表情，请检查后重新提交$灵感$你的主题\n\n 2.chatGPT网络问题，算力不够，请稍后再试。\n感谢支持'
    try:
        outlines=create_outline(theme,max_tokens)
    except:
        result=error_infor
        return result
    try:
        new_develoment=create_new_development(theme,max_tokens)
    except:
        result=error_infor
        return result    
    # outlines=create_outline(theme,max_tokens)
    # new_develoment=create_new_development(theme,max(10,max_tokens-100))
    result=theme+'\n\n提纲:'+outlines+'\n\n最新研究进展:'+new_develoment
    while getsizeof(result.encode('utf-8'))>1320:
        result=result[0:len(result)-5]
    return result


def get_free_chat(prompt,max_tokens,temperature):
    error_infor='恭喜你中彩票了，机器人碰到问题，可能chatGPT网络问题，算力不够，请稍后再试。\n感谢支持'
    try:
        r=free_chat(prompt,max_tokens,temperature)
    except:
        result=error_infor
        return result
    # try:
    #     new_develoment=create_new_development(theme,max_tokens)
    # except:
    #     result=error_infor
    #     return result    
    # outlines=create_outline(theme,max_tokens)
    # new_develoment=create_new_development(theme,max(10,max_tokens-100))
    result=r
    while getsizeof(result.encode('utf-8'))>1320:
        result=result[0:len(result)-5]
    return result

# def send_theme(user,theme):
#     url='http://42.192.17.155/back'
#     print(2)
#     body = {"touser": user, "theme":theme,"time":datetime.now().strftime("%Y%m%d%H%M%S")}
#     print(3)
#     data = bytes(json.dumps(body, ensure_ascii=False).encode('utf-8'))
#     print(1)
#     requests.post(url, data=data)

# send_theme('11','adfd')
# theme='中国医改历史和现有问题研究'
# max_tokens=200
# print(get_paper(theme,max_tokens))