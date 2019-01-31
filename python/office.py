# coding: utf-8
times = int(input())

for i in range(times):
    pair = input().split(' ')
    if int(pair[1]) == 3:
        print(pair[0])

