# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 21:37:53 2024

@author: USER
"""

#四則運算

import random


q = int(input(" 1 => + , 2 => - , 3 => *"))

a = (random.randint(1,100))

b = (random.randint(1,100))


if q == 1:
    print(a+b)
    
elif q == 2:
    print(a-b)
    
elif q == 3:
    print(a*b)
    
else:
    print("選項錯誤")