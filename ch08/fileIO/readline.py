
with open('2021kbo.txt', 'w') as f:
    team = ['삼성', 'LG', '기아', '롯데']
    for i in team:
        f.write(i + '\n')

with open('2021kbo.txt', 'r') as f:
    # data = f.readlines() # 파일 읽기를 하면 list로 반환
    # print(data)

    # 2차원리스트 만들기

    d2 = []
    for i in range(4):
        data = f.readline().split()
        d2.append(data)

    print(d2)