import re

# 그룹핑된 문자열에 이름 붙이기
# ?P<그룹이름> , 반드시 대문자 P
p = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
s = p.search('jang 010-2122-4578')
print(s.group())
print(s.group("name"))
print(s.group("phone"))


