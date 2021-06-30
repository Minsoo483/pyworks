# 영어 타자 연습 프로그램
import random
import time

f = open('words.txt', 'r')
word = f.read().split()
print(word)
f.close()

n = 1 # 문제 번호
print("[타자 게임] 준비되면 엔터")
input()
start = time.time()

q = random.choice(word) # 문제 출제
while n <= 10:
    print("문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n = n + 1
        q = random.choice(word)
    else:
        print("오타! 다시 도전")

print('게임 종료 ')
end = time.time()
et = (end - start)
print("타자 시간 : %.2f초" %et)

