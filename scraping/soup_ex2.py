from bs4 import BeautifulSoup

html_str = '''
    <html>
    <body>
        <ul class ='item'>
            <li>인공지능</li>
            <li>빅데이터</li>
            <li>로봇</li>
        </ul>
        <ul class ='lang'>
            <li>영어</li>
            <li>중국어</li>
            <li>한국어</li>
        </ul>
    </body>    
    </html>
'''
content = BeautifulSoup(html_str, 'html.parser')
ul = content.find('ul', {'class': 'lang'})
# print(ul)
'''li = ul.find('li')
print(li)  -> 맨위 li 만 검색'''

lis = ul.find_all('li') # find_all 은 list의 형태로 담김.
print(lis) # <li>태그 포함
print(lis[1].text) # text만 추출