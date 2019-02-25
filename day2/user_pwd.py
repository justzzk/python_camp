user_password={'one':'1','two':'12','three':'123'}
flag=1
for i in range(3):
    user=input('user:')
    if user in user_password.keys():
        password = input('password:')
        if password==user_password[user]:
            print('welcome!')
            flag = 0
            break
        else:
            for k in range(2):
                print('wrong password！')
                password=input('input password again:')
                if password==user_password[user]:
                    print('welcome')
                    flag=0
                    break
            break
    else:
        print('No user called %s '%user)
if flag:
    print('wrong user or password for three times!')