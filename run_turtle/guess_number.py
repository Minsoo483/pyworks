#숫자 추측 게임

import random as r

com = r.randint(1,30)
while True:
    guess = int(input('맞혀보세요(1~30): '))

    if com > guess:
        print('너무 작아요!!')
    elif com < guess:
        print('너무 커요!')
    else:
        print('정답')
        break
t.mainloop()
