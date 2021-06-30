f = open('c:/pyfile/2021kbo.txt', 'w')
team = ['기아', '삼성', 'LG', 'NC', '한화', '키움', 'KT', 'SSG']

'''for i in team:
    f.write(i + " ")
f.close()'''

for i in range(len(team)):
    f.write(team[i] + " ")
f.close()

f = open('c:/pyfile/2021kbo.txt', 'r')
data = f.read()
print(data)