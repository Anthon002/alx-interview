#!/usr/bin/python3
'''
This module contains the pascal triangle
'''


def pascal_triangle(n):
    '''
    This method is the implemetation
    '''
    greaterList = []
    if (n <= 0):
        return greaterList
    for i in range(n):
        pascalArray = [1]
        val = 1
        for j in range(i):
            val = val *(i-j)/(j+1)
            pascalArray.append(int(val))

        greaterList.append(pascalArray)

    return greaterList;
