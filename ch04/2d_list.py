# 2차원 리스트의 생성과 출력

li = [[10,20], [30,40], [50,60]]

print('li[0][0]', li[0][0])
print('li[0][1]', li[0][1])
print('li[1][0]', li[1][0])
print('li[1][1]', li[1][1])
print('li[2][0]', li[2][0])
print('li[2][1]', li[2][1])

print(len(li)) # len(li) = 행의 크

for x,y in li:
    print(x,y)


for i in range(len(li)):
    for j in range(len(li[i])):  # len(li[i]) = 열의 크기
        print(li[i][j], end=' ')
    print()
