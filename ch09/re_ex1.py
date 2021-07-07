import re

# '*' 와 '+'의 차이 비교
pat1 = re.compile("ca*t") # '*' 앞 문자가 0개 이상 반복
m1 = re.findall(pat1, "caat")
m2 = re.findall(pat1, "ct")

pat2 = re.compile("ca+t") # '+' 앞 문자가 1개 이상 반복 (공집합 불가능)
n1 = re.findall(pat2, "caat")
n2 = re.findall(pat2, "ct")


print(m1)
print(m2)

print(n1)
print(n2)