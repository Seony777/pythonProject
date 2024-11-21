'''
파일명: EX02-9-mutable-immutable.py

데이터 타입의 가변성
    mutable: 객체 생성 후 내용 변경 가능
        - 값 변경 시 메모리 주소 유지
        ex) list, set, dict
    immutable: 객체 생성 후 내용 변경 불가
        - 값 변경 시 메모리 주소 할당
        ex) int, str, tuple 등 (tuple 주의!)
'''

# 1. mutable 예제
poketmon = ['피카츄', '파이리', '꼬부기']
print(poketmon)
print('메모리 주소:', id(poketmon))

poketmon[1]= '잠만보'
print('변경 후:',poketmon)
print('메모리 주소:', id(poketmon))

print()

# 2. immutable 예제
level = 25
print('level', level)
print('메모리 주소:', id(level))

level = 26
print('메모리 주소:', id(level))

level = level + 1
print('level+1:', level)
print('메모리 주소:', id(level)) # level이라는 변수가 25를 가리키고 있다고 값을 바꾸면 26을 가르키게 됨

age =25
print('age:', age)
print('메모리 주소:', id(age))

'''
리터럴(Literal) - 소스코드에 고정된 값
ex)
25 : 정수 리터럴
3.14 : 실수 리터럴
'홍길동' : 문자열 리터럴
true  : 부울 리터럴

그냥 어떤 값을 리터럴이라 한다~~~
'''
print('25 메모리 주소', id(25)) # 값에 대한 메모리 주소가 각각 있는 것임! 변수에 대한 메모리 주소가 아님!

tuple1 = ('파이썬','자바','씨쁠쁠')
print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))

tuple1 = ('리스트', 'go', 'React')
print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))
