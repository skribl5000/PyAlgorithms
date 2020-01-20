#! /usr/bin/env python
# -*- coding: utf-8 -*-

def factorize(x):
    """ Раскладывает число на множетели
        Печатает на экран
        х - натуральное
    """
    print(1)
    for n in range(2,x-1):
        if x%n == 0:
            print(n)
    print(x)

factorize(2**20)

#! /usr/bin/env python
# -*- coding: utf-8 -*-

def factorize_clever(x):
    devisor = 2
    while x > 1:
        if x%devisor == 0:
            print(devisor)
            x //= devisor
        else:
            devisor += 1

factorize_clever(2**20)