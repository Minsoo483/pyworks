import re


str = "Two is too"
f1 = re.findall("T[ow]o", str)
print(f1)

f2 = re.findall("T[ow]o", str, re.IGNORECASE)  # re.IGNORECASE는 대,소문자 구분하지 않음.
print(f2)

f3 = re.findall("t[^w]o", str, re.IGNORECASE)
print(f3)