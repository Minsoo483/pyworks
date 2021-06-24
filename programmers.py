import random
import string

# 이름 만들기 (1~20글자 소문자로 이루어짐)
source = string.ascii_lowercase #소문자 추출   




name_len = int(random.randint(1,20)) # 이름 길이 설정

# 이름 추출
name = ''
for x in range(name_len):
    
    alpha = random.choice(source)
    name += alpha
    
print(name)

#참가자 만들기
for x in range(1,11):

    particaint = list(name)
