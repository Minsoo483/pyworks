import re


p = re.compile('(\w+)\s+(\d+[-]\d+[-]\d+)')
s = p.search('jang 010-2122-4578')
print(s.group())
print(s.group(1))
print(s.group(2))


