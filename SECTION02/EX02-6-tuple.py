'''
파일명: EX02-6-tuple.py

튜플(Tuple)
    -읽기 전용 리스트
    -수정 불가능, 순서가 있는 자료구조
    -소괄호 () 사용
'''

# 1. 튜플 생성과 기본 조작
game_starter = ('파이리', '이상해씨', '꼬부기')
print('스타터 포켓몬:', game_starter)
print('첫번째 스타터:', game_starter[0])
print('마지막 스타터:', game_starter[-1])
print('전체 스타터:', len(game_starter))

# 2. 튜플 슬라이싱
legendary_birds = ('프리저', '썬더', '파이어', '루기아')
print('전설의 새:', legendary_birds[1:3])

# 3. 튜플 수정 불가 테스트
evolve_chain = ('치코타', '베이리프', '메가니옴')
# evolve_chain[1] = '아마겟돈'
# print('튜플 수정 테스트:', evolve_chain)
# 튜플수정 에러 메시지: TypeError: 'tuple' object does not support item assignment
print('evolve_chain 주소값1:', id(evolve_chain)) #변수가 가지고 있는 값의 주소값을 알 수 있음

#임시 리스트 변환하여 수정
temp_list = list(evolve_chain) #원본이 바뀐 건 아님 그저 리스트로 똑같이 하나 만든거임
temp_list[1] = '아마겟돈'
evolve_chain = tuple(temp_list) #여기서도 튜플로 바뀌는 것이 아니라 또 새로 튜플을 하나 만든것임 그 후 evolve_chain이라는 변수에 새로 넣은 것!
print('전환후:', evolve_chain)

print('evolve_chain 주소값2:', id(evolve_chain)) # 주소값이 다르게 나오는 걸 통해서 튜플이 수정되는 것이 아니었음을 알 수 있음

# 4. 튜플 언패킹
gym_leader = ('지우', '웅', '로이', '로사')
(leader1, leader2, leader3, leader4) = gym_leader #각각의 값들이 변수에 매칭이 되어 들어감
print('체육관 1번관장:', leader1)
print('체육관 2번관장:', leader2)
print('체육관 3번관장:', leader3)
print('체육관 4번관장:', leader4)

# 5. 튜플 결합(튜플은 수정이 안되기 때문에 리스트와 같이 한팀에 추가가 되는 것이 아니라 합쳐진 새로운 튜플 생성)
a_team = ('이상해씨', '파이리')
b_team = ('치코리타', '보케인')
c_team = a_team + b_team #리스트도 + 연산자 사용가능
print('연합팁:', c_team)
