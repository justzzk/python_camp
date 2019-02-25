# -*- coding: utf-8 -*-
menu = {
    '北京': {
        '海淀': {
            '五道口': {},
            '中关村': {},
            '上地': {}
        },
        '昌平': {
            '沙河': {},
            '天通苑': {},
            '回龙观': {}
        },
        '朝阳': {},
        '东城': {}
    },
    '山东': {
        '济南': {
            '长清区': {},
            '章丘区': {},
            '历下区': {}
        },
        '青岛': {
            '市南区': {},
            '市北区': {},
            '莱西市': {}
        }
    },
    '中国大学': {
        '985': {
            '清华': {},
            '北大': {},
            '浙大': {}
        },
        '211': {
            '北邮': {},
            '西电': {}
        },
        '双非': {}
    },
    '语言': {}
}

print('''
返回上级请输入back；
退出程序请输入quit；
''')
flag1 = True
while flag1:
    first_layer = menu.keys()
    print('first_layer： ' + str(first_layer))

    input1=input('quit or one of the first_layer:').strip().lower()
    if input1 == 'quit':
        flag1 = False
        break
    elif input1 not in first_layer:
        print('wrong input')
        continue
    else:
        flag2 = True
        while flag2:
            sec_layer = menu[input1].keys()
            print('sec_layer: ' + str(sec_layer))
            if not sec_layer:
                print('no values with this key')
                break
            else:
                input2 = input('back or quit or one of the sec_layer:').strip().lower()
                if input2 == 'back':
                    break
                elif input2 == 'quit':
                    flag1 = False
                    break
                elif input2 not in sec_layer:
                    print('wrong input')
                    continue
                else:
                    flag3 = True
                    while flag3:
                        third_layer = menu[input1][input2].keys()
                        if not third_layer:
                            print('no values with this key')
                            break
                        else:
                            print('third_layer: '+ str(third_layer))
                            input3 = input('back or quit or one of the third_layer:')
                            if input3 == 'back':
                                break
                            elif input3 == 'quit':
                                flag1 = False
                                flag2 = False
                                break
                            elif input3 not in third_layer:
                                print('wrong input')
                                continue
                            else:
                                input4 = input('''
                                this is the last layer 
                                back or quit 
                                ''').strip().lower()
                                if input4 == 'back':
                                    break
                                else:
                                    flag1 = False
                                    flag2 = False
                                    flag3 = False
                                    break
