'''
파일명: EX02-8-dict.py

딕셔너리(dict)
    -key:valaue 쌍으로 이루어진 자료구조
    -key는 중복 불가
    -실제 데이터를 구조화 하는데 유용
'''

# 1. 딕셔너리 생성
poketmon = {
    'name':'피카츄',
    'type':'전기',
    'level':25,
    'skill': ['백만볼트', '전광석화']

}
print('포켓몬 정보:', poketmon)

# 접근
print('name:', poketmon['name']) # 대괄호 접근
print('type:',poketmon['type'])
print('level:',poketmon['level'])
print('skill:',poketmon['skill'])
print('skill:',poketmon.get('skill')) # get() 메서드 접근
print('skill:',poketmon['skill'][0])

# 2. 딕셔너리 수정
poketmon['level'] = 30 #값 수정
print('수정 후:', poketmon)
poketmon['speed'] = 5
print('항목 추가:', poketmon)
poketmon.update({'hp':200})
print('업데이트 후:',poketmon)

# 3. 딕셔너리 삭제 메서드
remove_value = poketmon.pop('speed') #pop은 값을 반환해서 변수로 받을 수가 있음
print('삭제된 정보:', remove_value)
print('삭제 후:', poketmon)

last_item = poketmon.popitem() # 마지막 항목 삭제
print('마지막 항목:',last_item)
print('마지막 항목 삭제 루:',poketmon)

# 4. 딕셔너리 메서드
print('모든 키:',poketmon.keys()) # 딕셔너리의 모든키를 알 수 있음
print('모든 값:',poketmon.values()) #딕셔너리으 모든 밸류값을 알 수 있음

print('키 요소1:', list(poketmon.keys())[0]) #list로 형변환후 인덱스를 통애 첫번재 키를 가져오는 법
print('값 요소1:', list(poketmon.values())[0])

print('모든 쌍:', poketmon.items())

print('요소1:', list(poketmon.items())[0][1])