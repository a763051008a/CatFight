# -!- coding: utf-8 -!-
import json
from random import randint

io = 'baike_data.json'
f = open(io)
data = json.load(f)
def choose_que():
    a = randint(0,79)
    a = str(a)
    print('————————————————')
    print(data['title'][a],'\n',data['options'][a])
    answer = input('请输入您的答案(大写字母):\n')
    if answer == data['key'][a]:
        print('恭喜你回答正确')
        return '正确'
    else:
        print('很遗憾，回答错误，正确答案是：%s' % data['key'][a])
        return '错误'

