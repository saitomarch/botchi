# coding: utf-8
times = int(input())

left_wins = 0
right_wins = 0

for cnt in range(times):
    arr = input().split(' ')
    if arr[0] == arr[1]:
        continue
    elif arr[0] == 'g':
        if arr[1] == 'c':
            left_wins += 1
        elif arr[1] == 'p':
            right_wins += 1
    elif arr[0] == 'c':
        if arr[1] == 'p':
            left_wins += 1
        elif arr[1] == 'g':
            right_wins += 1
    elif arr[0] == 'p':
        if arr[1] == 'g':
            left_wins += 1
        elif arr[1] == 'c':
            right_wins += 1

print(left_wins)
print(right_wins)
