from __future__ import print_function

x = 1234
base = 10 

while x > 0:
    digit = x % base
    print(digit, end ='')
    x = x // base

# почему-то выводит наоборот