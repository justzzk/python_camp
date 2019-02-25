#修改文件
#1.将文件全部加载到内存中，修改完毕后覆盖硬盘旧文件
#2.将文件一行一行加载到内存，修改后覆盖原行
#此文件为方法1
#open 以w打开的文件不存在则创建，存在则清空
import os
with open('a.txt','r') as read_f,open('.a.txt.swap','w') as write_f:
    data=read_f.read()  #完全读入
    data=data.replace('mac','linux')

    write_f.write(data)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')
