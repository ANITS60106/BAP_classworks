from math import sqrt

def read_int():
    return int(input())

def read_int_butmany():
    return map(int, input().split(' '))

t = read_int()
for case_num in range(t):
    d, k = read_int_butmany()
    h = int(d / sqrt(2) / k)
    if (h * h + (h + 1) * (h + 1)) * k * k > d * d:
        print('Utkarsh')
    else:
        print('Ashish')