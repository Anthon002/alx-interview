#!/usr/bin/python3
'''
This module contains the pascal triangle
'''


def pascal_triangle(n):
    '''
    This is the pascal triangle implementation
    '''
    if (n <= 0):
        return []
    greaterList = []
    for i in range(n):
        pascalArray = []
        val = 1
        for j in range(i):
            val = val *(i-j)/(j+1)
            pascalArray.append(int(val))
        if (len(pascalArray) > 0):
            if (len(pascalArray) == 1):
                greaterList.append(pascalArray)
                greaterList.append([1,1])
            else:
                greaterList.append([1]+pascalArray)
            
    return greaterList;
