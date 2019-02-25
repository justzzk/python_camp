#一行一行替换
#open 以w打开的文件不存在则创建，存在则清空
import os
with open('a.txt','r') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('mac','linux')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')