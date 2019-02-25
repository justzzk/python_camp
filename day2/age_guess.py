#!/usr/bin/env python
# -*- coding: utf-8 -*-

#本程序有两重循环
#外循环判断用户yes or no
#内循环猜三次
#首先定义年龄
age=18
yorn=True
while yorn:
    age_g = int(input('你看我今年多大'))
    for i in range(2):
        if age_g==age:
            print('bingo！')
            yorn=False
            break
        else:
            age_g=int(input('不对哟，再猜一次:'))
    if yorn==True:
        if input('要继续猜嘛？y/n')=='n':
            yorn=False









