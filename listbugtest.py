#!/usr/bin/env python3

def compute(base, value):
    if base != None:
        other = []
        other.append(value)
    result0 = sum(other)
    result = sum(base) + result0
    print(result)
     
if __name__ == '__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)
