# coding: utf-8
text = input()
raw = ""
for i, ch in enumerate(text):
    if i % 2 == 0:
        raw += ch
print(raw)

