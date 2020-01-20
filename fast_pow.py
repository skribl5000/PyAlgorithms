#! /usr/bin/env python
# -*- coding: utf-8 -*-

x = 2
n = 100
i = 0
def pow(x,n):
    global i
    if n == 0:
        i += 1
        return(1)
    elif n%2 == 0:
        i += 1
        return(pow(x*x,n/2)) # если степень четная
    else:
        i += 1
        return(pow(x,n-1)*x) # это происходит если степень нечетная
print(pow(x,n))
print('fast pow - ' + str(i) + "  итераций в алгоритме")

k=0
def pow_old(x,n):
    global k
    if n == 0:
        k += 1
        return(1)
    else:
        k += 1
        return(pow_old(x,n-1)*x)
print(pow_old(x,n))
print('just pow - ' + str(k) + '  итераций в алгоритме')