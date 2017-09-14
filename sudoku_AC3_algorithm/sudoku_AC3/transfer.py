"""
-------------------------------------------------------
transfer.py
read file and change string to list
-------------------------------------------------------
Author:  lingchi chen   
Email:   jackchen4work@gmail.com
__updated__ = "2016-11-09"
-------------------------------------------------------
"""


def trans(f_name):
    """
    -------------------------------------------------------
    [function description]
    -------------------------------------------------------
    Preconditions:
        [parameter name - parameter description (parameter type and constraints)]
    Postconditions:
        [returns or prints]
        [return value name - return value description (return value type)] 
    -------------------------------------------------------
    """
    temp = [[0] * 9 for i in range(9)]
    list = []
    f = open(f_name, "r")
    with f as fp:
        for i in range(9):
            for line in fp:
                list = line.split(" ")
                for j in range(9):
                    temp[i][j] = list[0][j]
                    j += 1
                i += 1
    return temp
