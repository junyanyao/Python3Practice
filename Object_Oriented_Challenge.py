#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:00:23 2019

@author: YaoJunyan
"""

'''
Object Oriented Programming

Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
'''

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1= coor1
        self.coor2= coor2
        
    def distance(self):
        x1,y1= self.coor1
        x2,y2= self.coor2
        return ((y2-y1)**2 + (x2-x1)**2)**0.5
    
    def slope(self):
        x1,y1= self.coor1
        x2,y2= self.coor2
        return (y2-y1)/(x2-x1)

coor1 = (3,2)
coor2 = (8,10)

li = Line(coor1,coor2)
li.distance()
li.slope()

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height= height
        self.radius= radius
        self.pi= 3.14
        
    def volume(self):
        return self.pi * self.radius **2 *self.height
        
    
    def surface_area(self):
        return 2* self.pi * self.radius*self.height + 2*self.pi* self.radius**2
    
c = Cylinder(2,3)
c.volume()
c.surface_area()

'''
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
'''

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print("Account owner: {} Account balance: {}".format(self.owner, self.balance))
        
    def deposit(self,n):
        print('Deposit Accepted')
    
    def withdraw(self,n):
        if self.balance-n >0:
            print ('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
            
# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner


# 4. Show the account balance attribute
acct1.balance


# 5. Make a series of deposits and withdrawals
acct1.deposit(50)



acct1.withdraw(75)


# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)






















