# -*- coding: utf-8 -*-
def is369(n):
    '''어떤 수가 3이거나 6이거나 9인지 확인하는 함수'''
    return n==3 or n==6 or n==9

def count369(n):
    '''어떤 수에 있는 3,6,9의 개수 세는 함수'''
    if is369(n)==1: return 1
    elif n<10 and is369(n)==0: return 0
    return is369(n%10)+count369(n//10)

import os
os.getcwd()
with open('369.txt','w',encoding='utf-8') as f:
    for n in range(1,10001):
        if count369(n):
            f.write('*'*count369(n))
            f.write(' ')
        else:
            f.write(str(n))
            f.write(' ')
            
with open('369.txt','w',encoding='utf-8') as f:
    def count369_(n):
        if count369(n): return '*'*count369(n)
        return str(n)
    f.writelines(' '.join(count369_(n) for n in range(1,10001)))