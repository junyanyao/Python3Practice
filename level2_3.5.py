#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:08:29 2019

@author: YaoJunyan
"""

'''

LEVEL 2 PROBLEMS
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
def has_33(nums):
    a= ''.join(map(str,nums))
    return '33' in a 

'''
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters¶
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

'''
def paper_doll(text):
    l = list(text)
    repeat= [i*3 for i in l]
    return ''.join(repeat)
    
'''
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19

'''

def blackjack(a,b,c):
    if (a+b+c)<= 21:
        return a+b+c
    elif a+b+c> 21 and (a==11 or b ==11 or c ==11):
        return a+b+c-10
    else:
        return 'BUST'
    
'''
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 
(every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
'''
def summer_69(arr):
    if 6 in arr and 9 in arr:
        
        ind1 = arr.index(6)
        ind2= arr.index(9)
        part1= arr[:ind1]
        part2= arr[ind2+1:]
        return sum(part1)+sum(part2)
    else:
        return sum(arr)
    
'''
Challenge Problem

SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

'''

def spy_game(nums):
    code =[0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code)==1


'''

COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25

By convention, 0 and 1 are not prime.'''

def count_primes(num):
    primes =[]

    for prime in range(2, num+1):
        #assume numner is prime until shown it's not
        isPrime=True
        for i in range(2,prime):
            if prime % i ==0:
                isPrime=False
        if isPrime:
            primes.append(prime)
            
    return len(primes)


#another approach with breaks could be more efficient
def count_primes(num):
    primes =[]
    for i in range(2, num+1):
        isPrime =True
        for j in range(2, i):
            if i % j ==0:
                isPrime =False
                break
        if isPrime:
            primes.append(i)
    return len(primes)


'''
Just for fun:¶
PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print_big('a')

out:   *  
      * *
     *****
     *   *
     *   *
HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns. 
For purposes of this exercise, it's ok if your dictionary stops at "E".
'''

