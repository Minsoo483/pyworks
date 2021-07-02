import random
import string

# 이름 만들기 (1~20글자 소문자로 이루어짐)
source = string.ascii_lowercase #소문자 추출

#참가자 만들기
participant = ''
for x in range(3):
    #이름 만들기
    name_len = int(random.randint(1, 20))  # 이름 길이 설정
    name = ''
    for x in range(name_len):
        alpha = random.choice(source)
        name += alpha
    participant += name + ' '
# 만들어진 participant(str)을 list로 전환
participant = participant.split()
print('참가', participant)


#완주 못한 사람 만들기
# s : 참가자 중 완주 못한 사람의 리스트 인덱싱
s = random.randint(0, len(participant)-1)
# 완주 못한 사람 삭제
not_participant = participant[s]
print('완주x', not_participant)
participant.pop(s)
completion = participant
print('완주',completion)
