"""
-------------------------------------------------------
scan_row.py
[description of functions]
-------------------------------------------------------
Author:  lingchichen
ID:      your ID
__updated__ = "2016-11-09"
-------------------------------------------------------
"""
D = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def count_1(list):
    count = 0
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] == "-":
                count += 1
    return count


def scan(list, count):
    i = 0
    j = 0
    m = 0
    index = [[0] * 2 for i in range(count)]
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i][j] == "-":
                index[m][0] = i
                index[m][1] = j
                m += 1
            j += 1
        i += 1
    return index


def scan_row(index, temp,):
    """
    -------------------------------------------------------
    when - appear we want to know how many choices we can select by 
    scan row and column and unit where - is
    -------------------------------------------------------
    """
    count = 0
    r = index[0][0]
    for j in range(len(temp)):
        if list[r][j] != "-":
            count += 1

    exist = [0 * count]
    choice_r = []
    for n in range(count):
        for j in range(len(temp)):
            if temp[r][j] != "-":
                exist[n] = temp[r][j]
            j += 1
        n += 1
    print exist
    print exist[0:2]
    print D
    choice_r = D - exist
    return exist
