goods_exist={
      'apple':10,
      'tesla':100000,
      'mac':3000,
      'lenovo':30000,
      'chicken':10,
}
print('exist goods:%s'%goods_exist)
goods_want=[]

while True:
#for key,item in goods_exist.items():
    #print('name:{name} price:{price}'.format(name=key, price=item))
    choice=input('good you want: ').strip()
    if not choice or choice not in goods_exist:
        print('good not exist')
        continue
    count=input('how many:')
    while not count.isdigit():
        count=input('enter a number:')
    goods_want.append((choice,goods_exist[choice],count))
    print('goods you have choose:%s'%goods_want)
    if input('done?')=='y':
        break