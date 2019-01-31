# coding: utf-8
arr = input().split(' ')

length = int(arr[0])
from_num = int(arr[1])
to_num = int(arr[2])

for num in range(from_num, to_num + 1):
    fmt = f':0>{length}'
    print(f'{{{fmt}}}'.format(num))
    
