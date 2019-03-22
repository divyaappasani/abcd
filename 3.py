# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:34:25 2019

@author: online
"""

def q3():
    string = input("enter the string")
    set = int(input("enter your slice size:"))
    c = 0
    while (c<len(string)):
        print(string[c:c+set])
        c+=set
q3()