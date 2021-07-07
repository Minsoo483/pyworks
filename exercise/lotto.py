import random

lotto = []
while True:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n) #  중복 숫자 방지
    if len(lotto) == 6:
        break
print(lotto)

'''
lotto = []
for i in range(6):
    n = random.randint(1,45)
    if n not in lotto: 
print(lotto)'''