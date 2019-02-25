#（1）f.seek(p,0)  移动当文件第p个字节处，绝对位置
#（2）f.seek(p,1)  移动到相对于当前位置之后的p个字节
#（3）f.seek(p,2)  移动到相对文章尾之后的p个字节
#seek的第二个参数1和2只能在b模式下使用
#动态监控文件是否更新
import time
with open('tar.txt','rb') as f:
    f.seek(0,2)   #置光标与文件尾
    while True:
        line=f.readline()
        if line:
            print(line.decode('utf-8'))
        else:
            time.sleep(0.2)
