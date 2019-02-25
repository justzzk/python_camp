import os
with open('ini.txt','r',encoding='utf-8') as read_f,\
        open('tmp.txt','w',encoding='utf-8') as write_f:
    s=set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)
    os.remove('ini.txt')
    os.rename('tmp.txt','res.txt')