# -*- coding: utf-8 -*-
import sys
import copy
import os
goods = {
    'apple': 10,
    'tesla': 100000,
    'macbook': 3000,
    'bike': 200,
}
with open('registers.txt', 'a+') as reg, open('blacklist.txt', 'a+') as black, \
        open('new_reg.txt','w') as newreg:
    reg.seek(0)
    line = reg.readline()
    flag = True
    while flag:
        flag = False
        move = input('register or login：').strip().lower()
        if move == 'register':
            reg.read()
            user = input('input your name:')
            exit_user = []
            reg.seek(0)
            line = reg.readline()
            while line:
                line = line.strip().split('|')
                exit_user.append(line[0])
                line = reg.readline()
            if user in exit_user:
                print('you name is already registered,login directly')
                flag = True
                continue
            else:
                pswd = input('input your password :')
                account = input('input your money :')
                pswd2 = input('input your password again:')
                while  pswd != pswd2:
                    pswd2 = input('wrong password!input again:')
                reg.write(user+'|'+pswd+'|'+account+'\n')
                flag = True
                print('register success,login please')
                continue
        elif move == 'login':
            user = input('input your name:')
            black.seek(0)
            blackusers = black.readline().split()
            if user not in blackusers:
                pswd = input('input your password :')
            else:
                print('you are in the blacklist now')
                sys.exit()

            exit_flag = False
            reg.seek(0)
            line = reg.readline()
            while line:
                line = line.strip().split('|')
                if user == line[0]:
                    for i in range(2):
                        if pswd == line[1]:
                            exit_flag = True
                            break
                        else:
                            pswd = input('wrong password!input again:').strip().lower()
                    if exit_flag:
                        break
                    print('you have inputted the password for three times,'
                          'welcome to the blacklist')
                    black.read()
                    black.write(user + ' ')
                    #sys.exit()
                    flag = True
                    break
                else:
                    line = reg.readline()
            if not exit_flag :
                print('you have not registered ,register please')
                flag = True
        else:
            print('wrong command!input again:').strip().lower()
            flag = True

    print('\nthe goods you can buy and their prices are as follows:\n' + str(goods))
    #buys = goods   强调用
    buys = copy.deepcopy(goods)
    for key in buys.keys():
        buys[key] = 0

    while True:
        thing = input('input the one  you want: ').strip().lower()
        if thing not in buys.keys():
            print('wrong name,input again:')
            continue
        num = int(input('input the number you want to buy: ').strip().lower())
        cost = num*goods[thing]
        if cost > int(line[2]):
            print('your money left is not enough:'+ line[2])
            answer = input('do you want to continue?y or n:').strip().lower()
            if answer == 'n':
                break
            else:
                continue
        else:
            line[2] = str(int(line[2]) - cost)
            buys[thing] = buys[thing] + num
        print('your money left is:' + line[2])
        answer = input('do you want to continue?y or n：').strip().lower()
        if answer == 'n':
            break
        else:
            continue
    print('the things you buy and the number are:\n' + str(buys)+'\n')
    print('your money left is ' + line[2])

    reg.seek(0)
    newreg.seek(0)
    for everyline in reg:
        newline = everyline.strip().split('|')
        if newline[0] == line[0]:
            newreg.write(line[0] + '|' + line[1] + '|'+ line[2]+'\n')
        else:
            newreg.write(everyline)
os.remove('registers.txt')
os.rename('new_reg.txt','registers.txt')

sys.exit()
