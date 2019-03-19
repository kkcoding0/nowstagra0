#-*-coding:utf-8-*-
import sys

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        a =int(input())
        l.append(a)
    # print(l)
    l = list(set(l))
    # print(l)
    l.sort()
    for i in l:
        print(i)