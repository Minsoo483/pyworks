from urllib import request
from bs4 import BeautifulSoup


html = request.urlopen("https://finance.naver.com/marketindex/")
code = html.read().decode('euc-kr', 'replace').encode('utf-8', 'replace') # 한글깨짐때문에 추가
contents = BeautifulSoup(code, "html.parser")
ul = contents.select_one("ul.data_lst")
lis = ul.select("li")


for li in lis:
    ex = li.select_one("span.blind")
    val = li.select_one("span.value")

    #print(ex.text)
    #print(val.text)

    print(ex.string.split(' ')[-1], ':', val.string)
