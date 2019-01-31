# coding: utf-8
input()

success = 0
arr = input().split(" ")
for str in arr:
    if int(str) > 5:
        success += 1

print(success)
