# coding: utf-8
balance = int(input())
withdraw = int(input())
if withdraw > balance:
    print("error")
else:
    print(balance - withdraw)

