'''
파일명: EX02-5-list-1.py

리스트(list)
    -순서가 있는 데이터 집합
    -중복 허용, 수정 가능
    -다양한 자료형 포함 가능

'''

# 문자열 len()
print('문자열 길이:', len('Hello'))

# 1. 리스트 생성과 접근
poketmon_list = ['피카츄', '라이츄', '파이리']
print('리스트 전체:', poketmon_list)
print('첫번째 포켓몬:', poketmon_list[0])
print('리스트 길이:', len(poketmon_list)) #파이썬 제공 내장함수 len
print('첫번째 포켓몬 문자열 길이:', len(poketmon_list[0:2]))
print('테스트1:', len(poketmon_list[0:2][1]))
print('테스트2:', poketmon_list[0:2][1])
print(poketmon_list[0:2])
# 함수의 실행우선 순위가 따로 있는 건 아니고 안쪽부터 실행한다고 생각하면 됨

p2 = ['피카츄', '라이츄']
print(p2[1])

# 2. 리스트 슬라이싱
fruit_list = ['블루베리', '바나나', '사과', '자몽', '체리', '망고']
print(fruit_list[2:4])
print(fruit_list[1:])
print(fruit_list[-3:])
print(fruit_list[::-1])
print(fruit_list[5:2:-1])  #
print(fruit_list[:3])

print('스탭테스트 2:', fruit_list[0:6:2]) #세번째는 스탭이라고 하는 데 두칸씩 이동할 수 있게금 해줌
# 스탭테스트 2: ['블루베리', '사과', '체리']


# 3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1, 2, 3, 4, 5]
boolean_list = [True, False, True]
mixed_list = ['문자열', 100, True, 3.14] #리스트 안에서 타입이 다를 수 있음

# 4. 리스트 수정
poketmon_list = ['피카츄', '라이츄', '파이리']
poketmon_list[1] = '잠만보' #단일 항목 수정
print("수정된 리스트:", poketmon_list)
print(poketmon_list[1:2]) #1번 인덱스부터 2번 인덱스 앞까지

# 5. 범위 수정
evolution_list = ['피카츄', '라이츄', '파이리','리자드', '리자몽']
evolution_list[1:3] = ['라이츄킹', '메가파이리']
print("수정된 리스트:",evolution_list)