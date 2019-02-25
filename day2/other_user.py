count=0
user_password={'one':'1','two':'12','three':'123'}
lock={}
while len(lock)<3:
    username=input('user:')
    if username in lock.keys():
        print('user forbidden')
    elif username not in user_password.keys():
        print('user not exist')
    else:
        pwd=input('password:')
        if pwd==user_password[username]:
            print('welcome')
            count=0
        else:
            while count<2:
                pwd=input('wrong password,input again:')
                if pwd==user_password[username]:
                    print('welcome')
                    break
                count+=1
            else:
                lock[username]=username   #将用户名同时赋值key和value
                count=0
                print('user is forbidden,try another:')
else:
    print('all users forbidden!')
    print(lock)
