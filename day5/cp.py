#target_file
#open 以w打开的文件不存在则创建，存在则清空
#以a打开的文件不存在则创建且不清空
import sys
if len(sys.argv)!=3:
    print('usage:cp source_file target_file')
    sys.exit()

source_file,target_file=sys.argv[1],sys.argv[2]
with open(source_file,'rb') as read_f,open(target_file,'wb') as write_f:
    for line in read_f:
        write_f.write(line)