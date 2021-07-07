import sys

args = sys.argv[1:] #리스트형 자료
# print(args)

sum = 0
for i in range(0, len(args)):
    sum += int(args[i])
print(sum)

sum1 = 0
for i in args:
    sum1 += int(i)
print(sum1)

