#-*-coding:utf8;-*-

import random

userlen = int(input('put length:'))

def number():
    l = [0]
    l[0] = str(random.randint(1,9))
    for i in range(1, userlen):
        l.append(str(random.randint(1,9)))
    return(l)

a = number()

def bull(unk_num):
    user = list(input('put your number:'))
    print user
    if len(user) != len(unk_num):
        print 'must be' + ' ' + str(len(unk_num)) + ' ' + 'digits!'
        bull(unk_num)

    res = []

    for i in range(0,userlen):
        if user[i] == unk_num[i]:
            res.append('bull')
        elif user[i] in unk_num:
            res.append('cow')

    if user == unk_num:
        return('You won!')

    while user != unk_num:
        print('-'.join(res))
        bull(unk_num)

    return '-'.join(res)
    
c = bull(a)
print(c)
    


