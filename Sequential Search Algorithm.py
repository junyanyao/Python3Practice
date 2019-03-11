#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:44:49 2019

@author: YaoJunyan
"""
def sequentialSearch(alist, item):
    pos= 0
    found =False
    while pos < len(alist):
        if alist[pos] ==item:
            found=True
        else:
            pos= pos+1
    return found
testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

def orderedSequentialSearch(alist, item):
    pos= 0
    found= False
    stop = False
    while pos<len(alist) and not found:
        if alist[pos] == item:
            found= True
        else:
            if alist[pos] > item:
                stop =True
            else:
                pos += 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))

def binarySearch(alist, item):
    first =0
    last = len(alist)-1
    found= False
    while first <= last and not found:
        midpoint= (first +last) //2
        if alist[midpoint]== item:
            found=True
        else:
            if item< alist[midpoint]:
                last= midpoint -1
            else:
                first = midpoint +1
    return found
print(binarySearch(testlist,3))



#recursive approach to write Binary search 
def binarysearch1(alist, item):
     if len(alist)==0:
         return False
     else:
         midpoint = len(alist)//2
         if alist[midpoint] ==item:
             return True
         else:
             if alist[midpoint] > item:
                 return binarysearch1(alist[:midpoint], item)
             else:
                 return binarysearch1(alist[midpoint+1:], item)




            