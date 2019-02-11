# coding: utf-8
num = 0
arr = input().split(' ')
for item in arr:
  num += int(item)

print(num % 10)
