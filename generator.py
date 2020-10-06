#!/bin/env python
""" Generators only return a value when called
Without Generators:
 - Time: 0.6450381278991699 seconds
 - Size: 81528048

With Generators:
 - Time 1.9073486328125e-06 seconds
 - Size 112
 """
import sys
import time


def timeIt(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        print('Time:', endTime - startTime, 'seconds')

    return wrapper


# Normal function
@timeIt
def getList(limit):
    listVal = list()
    for i in range(limit):
        listVal.append(i)
    return listVal


# Generator function (no return, use yield)
@timeIt
def genList(limit):
    for i in range(limit):
        yield i


if __name__ == "__main__":
    numLimit = 10000000

    print('\nWithout Generators:')
    numList = getList(numLimit)

    print('\nWith Generators:')
    numGenerator = genList(numLimit)