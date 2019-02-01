# coding: utf-8
import re

times = int(input())

result = ""

for i in range(times):
    str = input()

    findstr = ""
    found_pattern = ""
    for ch in str:
        findstr += ch
        if re.compile(rf"{findstr}$").search(result) is not None:
            found_pattern = rf"{findstr}$"
    if len(found_pattern) != 0:
        result = re.sub(found_pattern, str, result)
    else:
        result += str

print(result)
