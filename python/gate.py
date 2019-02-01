# coding: utf-8
arr = input().split(' ')
h = int(arr[0])
w = int(arr[1])
n = int(arr[2])

x = 0
y = 0

for i in range(n):
    d = input()
    if d == 'U':
        y += 1
    elif d == 'R':
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'D':
        y -= 1

if 0 <= y and y < h and 0 <= x and x < w:
    print("valid")
else:
    print("invalid")
