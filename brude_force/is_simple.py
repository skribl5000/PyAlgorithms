#! /usr/bin/env python
# -*- coding: utf-8 -*-

def is_simple(x):
    """ Определяет, является ли число простым
        x - integer > 0
        Возвращает Boolean
    """
    if x == 1:
        return(True)
    for n in range(2,x-1):
        if x%n == 0:
            print(n)
            return(False)
    return(True)

print(is_simple(17))
print(is_simple(6))
print(is_simple(1))