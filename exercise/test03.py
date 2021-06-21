#1번
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#2번
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

result = 0
i = 1
while True:
    if i%3 == 0:
        result += i
    i += 1
    if i >1000:
        break
print(result)

#3번
i=0
while 1:
    i += 1
    if i > 5 :
        break
    print("*" * i)

for i in range(1,6):
    for j in range(0,i):
        print("*", end = "")
    print()

'''#4번
for i in range(1,101):
    print(i)'''

#5번
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)

#6번
numbers = [1,2,3,4,5]
result = []
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
print(result)
