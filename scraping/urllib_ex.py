from urllib import request

url = "https://www.naver.com"
content = request.urlopen(url)
print(content.read())

