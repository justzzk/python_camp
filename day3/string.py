#!/usr/bin/env python
# -*- coding: utf-8 -*-
#对string操作的练习
ini_str='    vIctOrY    '

# 1)    移除两边的空格,并输出处理结果
print(ini_str.strip())
# 2)    判断是否以 "vI" 开头,并输出结果 
if  ini_str.strip().startswith('vI'):
    print('true')
else:
    print('false')
# 3)    判断是否以 "y" 结尾,并输出结果 
if  ini_str.endswith('y'):
    print('true')
else:
    print('false')
# 4)    将“t” 替换为 “b”,并输出结果
print(ini_str.replace('t','b'))
# 5)    将根据 “t” 分割,并输出结果。
print(ini_str.split("t"))
# 6)    变大写,并输出结果 
print(ini_str.upper())
# 7)    变小写,并输出结果
print(ini_str.lower())
# 8)    请输出第 6 个字符?
print(ini_str[5])
# 9)    请输出前 7个字符?
print(ini_str[:6])
# 10)    请输出后 2 个字符? 
print(ini_str[-6:])
# 11)    请输出 “r” 所在索引位置? 
print(ini_str.index('r'))#使用find也可以
# 12)    获取子序列,去掉最后一个字符，确定好范围即可。如: vIctOrY则获取vIctOr
print(ini_str[:-5])