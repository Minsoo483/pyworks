from urllib import request
from bs4 import BeautifulSoup


html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace') # 한글깨짐때문에 추가
contents = BeautifulSoup(code, "html.parser")
ul = contents.find('ul', {'class':'data_lst'})
lis = ul.find_all('li')

for li in lis:

    ex = li.find('span', {'class':'blind'})
    val = li.find('span', {'class':'value'})
    #print(ex.text)
    #print(val.text)

    print(ex.string.split(' ')[-1], ':', val.string)
