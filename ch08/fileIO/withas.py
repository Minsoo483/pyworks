# with ~ as 구문은 f.close()를 생략
with open('data.txt', 'w') as f:
    f.write('안녕하세요\n')
    f.write('%d\n' % 150000)
    unit = '1 inch는 %.2fcm' % 2.54
    f.write(unit)

with open('data.txt', 'r') as f:
    data = f.read()
    print(data)

