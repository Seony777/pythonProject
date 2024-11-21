'''
파일명:EX02-3-type-2.py

컬렉션 타입: 변수 하나에 여러개 값을 담을 수 있음
    -리스트(list): 여러 값을 순서대로 저장
    -튜플(tuple): 리스트와 비슷하지만 수정 불가능
    -딕셔너리(dict): 키와 값이 쌍으로 저장
    -세트(set): 중복없이 저장
'''

#1. 컬렉션 타입예제
poketmon_list = ['피카츄','라이츄','파이리']
poketmon_tuple = ('피카츄','라이츄','파이리')
poketmon_dict = {'name':'피카츄', '기술':'백만볼트'}
#키 값은 중복이 안됨/ 왼쪽이 키값 오른쪽이 밸류값
poketmon_set = {'피카츄','라이츄','파이리'}

print('리스트:', poketmon_list)
print('튜플:', poketmon_tuple)
print('딕셔너리:', poketmon_dict)
print('세트:', poketmon_set)

print('리스트 첫번째 값 불러오기:', poketmon_list[0])
print('튜플 첫번째 값 불러오기:', poketmon_tuple[0])
#리스트,튜플의 순서는 0부터 시작, 이 숫자를 인덱스 번호라고도 함
print('딕셔너리 name 값 불러오기:', poketmon_dict['name'])
#딕셔너리는 키값으로 변수를 불러옴
#세트는 순서도 없고 중복값도 없음


