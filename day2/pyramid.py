#print默认打印完一次后换行，所以加end=‘’以使之以空格阶数
i=int(input('几层塔：'))
#print()
for level in range(1,i+1):
    for space in range(i-level):
        print(' ',end='')
    for star in range(2*level-1):
        print('*',end='')
    print()