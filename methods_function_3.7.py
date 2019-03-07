#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:54:36 2019

@author: YaoJunyan
"""

'''
Functions and Methods Homework
Complete the following questions:

Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as $$\frac{4}{3} πr^3$$'''
def vol(rad):
    return (4/3)*(rad**3)*math.pi

#check
vol(2)


#Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low, high):
        print('{} is in the rnage between {} and {}'.format(num, low, high))
# Check
ran_check(5,2,7)

def ran_bool(num,low,high):
    if num in range(low, high):
        return True
    else:
        return False
    
#check
ran_bool(5,2,7)

'''

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33

HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!'''

def up_low(s):
    l= list(s)
    up=[]
    low=[]
    for i in l:
        if i.isupper() ==True:
            up.append(i)
        elif i.islower() ==True:
            low.append(i)
    up_num= len(up)
    low_num= len(low)
    print('No. of Upper case character: {}'.format(up_num))
    print('No. of Lower case character: {}'.format(low_num))

'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''
           

def unique_list(lst):
    return list(dict.fromkeys(lst)) 
#check
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''
def multiply(numbers):  
    result = 1
    for i in numbers:
        result= result* i
    return result
        

'''

Write a Python function that checks whether a passed in string is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''
def palindrome(s):
    left_pos= 0
    right_pos= len(s)-1
    while right_pos >= left_pos:
        if not s[left_pos]== s[right_pos]:
            return False
        left_pos += 1
        right_pos -=1
    return True

#check


'''
Hard:
Write a Python function to check whether a string is pangram or not.

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: Look at the string module
'''


    