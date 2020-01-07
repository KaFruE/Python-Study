# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:07:43 2020

@author: Owner

"""


N = input()
N = int(N)

while N != 0:
    num = input()
    num = int(num)
    
    N = N-1
    sum = 0
    for i in range(1,num+1):
        if i%2 == 1:
            sum = sum + i
    print(sum)
