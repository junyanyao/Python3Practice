#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:46:56 2019

@author: YaoJunyan
"""

'''
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
'''
def old_macdonald(name):
    return name[0].upper()+name[1:3]+name[3].upper()+name[4:]
    
#check
old_macdonald('macdonald')



'''
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
'''
def master_yoda(word):
    l= word.split()
    l= l[::-1]
    return ' '.join(l)

'''
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
'''
def almost_there(n):
    if (n>=90 and n<=110) or (n >=190 and n<=210):
        return True
    else:
        return False
'''
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
'''