#!user/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
    """fibonacci sequence with recursion"""
    if n < 2: # return 0 or 1 if 0 or 1
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
    """Find GCD of two numbers using Euclid’s GCD Algorithm"""
    if b > a:
        a, b = b, a # Avoid 0 division error if b is a greater number than a

    if a % b == 0:
        return b

    return gcd(b, a % b)

def compareTo(s1, s2):
    """Compares two strings to check if they are the same length and whether one is longer
        than the other"""
    move_slice1 = 0
    move_slice2 = 1
    if s1[move_slice1:move_slice2] == '' and s2[move_slice1:move_slice2] == '':
        return 0 # return 0 if same length
    elif s1[move_slice1:move_slice2] == '' and s2[move_slice1:move_slice2] != '':
        return len(s2) * -1 # return negative number if s2 > s1
    elif s1[move_slice1:move_slice2] != '' and s2[move_slice1:move_slice2] == '':
        return len(s1) # return positive number if s1 > s2
    else:
        move_slice1 += 1 # with each new call, the next object in the string is checked if empty or not
        move_slice2 += 1

    return compareTo(s1[1:], s2[1:])







