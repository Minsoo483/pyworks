#로또 번호 생성

import random as r

lotto = []

for x in range(6):
    n = r.randint(1,45)
    if n not in lotto:
        lotto.append(n)
    
           

#print(lotto)

lotto2 = []

while len(lotto2) <6:
    n = r.randint(1,45)   
    if n not in lotto2:
        lotto2.append(n)


print("이번주 로또 예측 : " ,lotto2)

t.mainloop()
