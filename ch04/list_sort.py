# 리스트의 최대값과 최솟값, 정렬

#최댓값
score = [70, 80, 50, 60, 90, 40]
n = len(score)


max = score[0]
for i in range(0, n):
    if score[i] > max:
        max = score[i]

print("최고 점수 %d" %max)


# 오름차순 정렬

for i in range(0,n):
    for j in range(0,n-1):
        if score[j] > score[j+1]:
            score[j], score[j+1] = score[j+1], score[j]
#버블 정렬이랑 같음. 인접한 두개 원소끼리 비교해서 -> 맨 뒤에 제일 큰 값부터 정렬
            
'''for i in score:
    print(i, end=' ')'''


for i in range(0,n):
    for j in range(i, n):
        if score[i] > score[j]:
            score[i], score[j] = score[j], score[i]
#선택 정렬이랑 같음. 맨 앞에서 부터 차례대로 비교해서 -> 맨 앞에 제일 작은 값부터 정렬
            
print(score)
