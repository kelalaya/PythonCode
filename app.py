# print("Hello World")
# print("       /|")
# print("      / |")
# print("     /  |")
# print("    /___|")

# 变量 variable
# name = "qwh"
# age = "20"
# print("my name is"+name+"haha")
# print("my age is"+age+"hhh")

# 计算数列1 4 7 10 13 16 19...前100项的和
# x1 = 1
# d = 3
# n = 100
# x100 = x1+(n-1)*d
# s = n*(x1+x100)/2
# print (s)
# # 计算数列1 2 4 8 16...前100项的和
# x1 = 1
# q = 2
# n = 100
# x100 = x1*q^(n-1)
# s = x1*(1-q^n)/(1-q)
# print(s)

# 数据类型 datatype
# string '' ""
# number
#booler
# name = "qwh"
# name1 = 'ylh'
# # name2 = abc
# age = 1000.55
# isMale = True
# print(name)
# print(name1)
# # print(name2)
# print(age)
# print(name[0])
# print(isMale)
# print(100<99)

#字符串
# mystr = "DLMU"
# print(mystr)
# str = 'DL\nMU'
# print(str)
# str1 = 'DL"MU"'
# print(str1)
# str2 = "\"DL\"MU"
# print(str2)
# s = 'Python was started in 1989 by\"Guido\".\nPython is free and easy to learn.'
# print (s*3)

# 函数funcation
# strfun = "dlmu"
# print(strfun.upper())
# print(strfun.upper().isupper())
# print(strfun[3])
# print(strfun.index('m'))
# # print(str.index("M"))
# print(strfun.replace("dl","DL"))
# print(strfun.isdigit())
# print(strfun.isalnum())
# print(strfun.isalpha())
# print(strfun.__len__())
# 数字类型 number
# print(-1.222)
# print(1.5e3)
# print(1.5e-3)
# print(2**5)
# print(2+3)
# print(2*3)
# print(2/3)
# print(2-3)

# 数字函数
# abs pow max min round    math
# mymum = -5
# print(abs(mymum))
# print(pow(2,4))
# print(2**4)
# print(max(5,8))
# print(min(3,6))
# print(round(4.611))
# from math import *
# print(floor(4.999))
# print(sqrt(5))

# x1 = 1
# d = 3
# n= 100
# x100  = x1 + (99 * d)/2
# Sn = n*(x1+x100)/2
# print(Sn)

# raw字符串与多行字符串
# print('''Line1
# line2
# line3'''
# 'Line1\nline2\nline3'
# r'''Python is created by"Guide".
# It is free and easy to learn.
# Let's start learn Python in imooc!''')

# # Unicode字符串
# print( '''中国''')
#
# # 整数与浮点数
# print(2.5+10/4)
# print(2.5+10%4)
# print(11/4)
# print(2+3)
# print(2.0+3.0)
#
# # 布尔类型
# a = 'Python'
# print('hello,',a or 'world')
# b = ''
# print('hello,',b or 'World')

# List和Tuple类型
# 创建List
# L = ['Adam',100, 'Lisa',150]
# print(L)
# # 按照索引访问List
# print(L[0])
# # 倒序访问List
# print(L[-1])
# # 添加新元素
# L.append('Kikko')
# print(L)
# L.insert(0,'Hao')
# print(L)
# 创建tuple
# t = (0,1,2,3,4,5,6)
# t = tuple(range(0,10))
# print(t)
# 创建单元素tuple
# t = ()
# print(t)
# t = (1,)
# print(t)
# t = (1,2,3)
# print(t)
# t = (1,2,3,)
# print(t)

# if语句
# score = 100
# if score >=90:
#     print('excellent')
# elif score >=80:
#     print('good')
# elif score >=60:
#     print('passed')
# else:
#     print('failed')
#
#
# # while循环   计算100以内奇数的和
# sum = 0
# x = 1
# while x < 100:
#     sum+=x
#     x += 2
#     print(sum)
#
# # for循环 计算平均成绩
# L = [75,92,59,68]
# sum = 0.0
# for score in L:
#  sum+=score
#  print(sum/4)
#
# # break退出循环
# sum = 0
# x = 1
# n = 1
# while n<20:
#     sum = sum+x
#     x = x*2
#     n = n+1
#     print(sum)
# while True:
#     sum = sum+x
#     x = x*2
#     n = n+1
#     if n>20:
#         break
#     print(sum)

# 多重循环
# 对100以内两位数，使用一个人两重循环，打印出所有十位数比个位数小的
# for x in [1,2,3,4,5,6,7,8,9] :
#     for y in [0,1,2,3,4,5,6,7,8,9]:
#         if x<y:
#             print(x*10+y)

# 访问dict
# d = {
#     'Adam':95,
#     'Lisa':100
# }
# print(d.get('Adam'))
# print(d['Lisa'])

# 根据分数查找名字
# d={
#     95:'Adam',
#     100:'Kikko'
# }
# print(d.get(100))
# # 更新dict
# d[72] = 'Paul'
# print(d)

# 遍历dict
# d ={
# 'Adam':95,
# 'Lisa':85,
# 'Bart':59
# }
# for key in d:
#     print(key + ':',d[key])

# set --什么是set
# s = set(['Kikko','LingHao'])
# s = set(['Kikko','LingHao','Kikko'])
# print(s)

# set --访问set
# s = (['Kikko','LingHao'])
# print('Kikko' in s)
# print('SHABI' in s )

# set --set的特点
# months = set(['Jan','Feb','Mar'])
# x1 = 'Jan'
# x2 = 'Sun'
# if x1 in months:
#     print('x1: ok')
# else:
#     print('x1:error')
# if x2 in months:
#     print('x2:ok')
# else:
#     print('x2:error')

# set --遍历set
# s = set([('Adam',95),('Kikko',100)])
# for x in s:
#     print(x[0]+':',x[1])

#set --更新set
# 针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
# s = set(['Kikko','AB','CD'])
# L = ['AB','CD','lINGHAO']
# for name in L:
#     if name in s:
#         s.remove(name)
#     else:
#         s.add(name)
# print(s)

# 函数 -- 调用函数
# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
# L = []
# i = 1
# while i <= 100:
#     L.append(i*i)
#     i = i + 1
# print (sum(L))
# L = []
# i = 1
# for i in  range(1,101):
#     L.append(i*i)
# print(sum(L))


# 函数 --编写函数
# 请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
# def square_of_sum(L):
#     sum = 0
#     for x in L:
#         sum = sum + x*x
#     return sum
# print(square_of_sum([1,2,3,4,5]))
# print(square_of_sum([-5,0,5,3,2]))

# # 函数之返回多值
# # 返回一元二次方程的两个解
# import math
# def qiujie(a,b,c):
#     t = math.sqrt(b*b-4*a*c)
#     return (-b-t)/(2*a),(-b+t)/(2*a)
# print(qiujie(2,3,0))
#
# # 递归函数
# # 汉诺塔 用函数move(n,a,b,c)将n个圆盘从a借助b移动到c
# def move(n, a, b, c):
# # 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
#     if n == 1:
#         print (a,'-->', c)
#         return
# # 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
#     move(n-1, a, c, b)
# # 输出最下面个盘子移从a移到c的路径
#     print(a,'-->',c)
# # 将b柱子上面的n-1个盘子移动到c柱子上面
#     move(n-1, b, a, c)
#
# move(4, 'A', 'B', 'C')

# Python定义默认参数
# 定义一个greet（）函数，包含一个默认参数，如果没有传入，打印‘Hello,World’如果传入，打印‘Hello,xxx.’
# def greet(name = 'World'):
#     print('Hello,'+name+'.')
# greet()   #对于这个函数，可以不输入参数，输出就是默认输出 即 hello world
# greet('Bart')  #输入一个参数，则输出就是hello [输入的参数]

# Python定义可变参数
# 编写接受可变参数的average()参数
# def average(*args):
#     sum = 0.0
#     l = len(args)
#     if l ==0:
#         return sum
#     for x in args:
#         sum+=x
#     return sum/l
# print(average())
# print(average(1,2))
# print(average(1,2,2,3,4))

# 对list进行切片
# t = range(1,101)  #range函数创建一个数列
# L = list(t) # list列表
# print(L[0:10])  # 取前十个数
# print(L[2::3]) # 取3的倍数
# print(L[5:50:6]) # 取50以内6的倍数

# 倒序切片
# L = list(range(1,101))
# print(L[-10:])   # 取最后10个数
# print(L[-10:-1])  # 取最后10个数 不包含第10个数 即取9个数
# print(L[4::5][-10:]) # 取最后10个5的倍数
# print(L[-46::5]) # 取最后10个5的倍数

# 对字符串进行切片
# def firstCharUpper(s):
#     return s[0].upper()+s[1:]
# print(firstCharUpper('hello'))
# print(firstCharUpper('sunday'))

# 迭代
# 用for 循环迭代数列1-100并打印出7的倍数
# for x in range(1,101)[6::7]:
#         print (x)

# for x in range(1,101):
#     if x%7==0:
#         print(x)

# 索引迭代
# List = ['aaa','bbb','ccc']
# for index,name in zip((range(1,len(List)+1)),List):
#     print (index,'-',name)

# 迭代dict的value
# d ={'aaa':95,'Lisa':85,'Bart':59}
# print (d.values())
# for x in d.values():
#     print(x)

# # print(d.itervalues())
# for x in d.itervalues():
#     print (x)

# 迭代dict的value
# 计算所有同学的平均分
# d = {'aaa':95,'bbb':85,'ccc':59,'ddd':74}
# sum=0.0
# for x in d.values():
#     sum +=x
#     print(sum/len(d) )

#迭代dict的key和value
# 打印出name:score,最后打印出平均分average:score
# d = {'aaa':95,'bbb':85,'ccc':59,'ddd':74}
# sum = 0.0
# for x,y in d.items():
#     sum +=y
#     print(x,':',y)
# print('average',':',sum/len

# 生成列表
# 用列表生成式生成列表[1*2,3*4,5*6,...,99*100]
# print([x*(x+1) for x in range(1,100,2)])

# 复杂表达式
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
# def generate_tr(name, score):
#     if score<60:
#         return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name,score)
#     return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
#
# tds = [generate_tr(name,score) for name, score in d.iteritems()]
# print( '<table border="1">')
# print( '<tr><th>Name</th><th>Score</th><tr>')
# print( '\n'.join(tds))
# print( '</table>')

# 条件过滤
# def toUppers(L):
#     return [x.upper() for x in L if isinstance(x,str)]
# print(toUppers(['Hello','World',101]))

# 多层表达式
# print([100*m+10*n+x for m in range(1,10) for n in range(10) for x in range(10) if m==x])

