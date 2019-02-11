# coding: utf-8
balance = int(input())
withdraw = int(input())
rslt = balance - withdraw
if rslt < 0:
    print("error")
else:
    print(rslt)
