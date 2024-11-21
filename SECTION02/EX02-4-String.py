'''
파일명:EX02-4-String.py

문자열(String, str)
    -문자듷의 순서가 있는 나열
    -작은따옴표(') 또는 큰따옴표(")로 표현
    -문자열은 변경불가능(immutable) / 변수값 변경은 가능, 메모리안에서 값의 변경이 불가능한거임
'''

#1. 문자열 생성 방법
str1 = 'Hello Python'    #작은 따옴표
str2 = "Hello Python"    #큰 따옴표
# 여러줄 문자열 작은 따옴표
str3 = '''Hello 
Python
'''
# 여러줄 문자열 큰 따옴표
str4 = """Hello
Python
"""

# 줄복사 단축키 Ctrl + d
# 줄삭제 단축키 Ctrl + y
print(str1)
print(str2)
print(str3)
print(str4)

# 2.문자열 인덱싱
'''
         /h/e/l/l/o/
index     0/1/2/3/4/
역순번호  -5/-4/-3/-2/-1   (거의 파이썬에만 있다고 보면 됨)
문자의 리스트와 비슷하다고 생각하면 됨
방번호를 인덱스 번호라고 함
'''

str = 'hello'
print('1번째 문자:', str[0])
print('마지막 문자:', str[4])
print('-1번째 문자:', str[-1])
print('-2번째 문자:', str[-2])
print('-3번째 문자:', str[-3])

# 3. 문자열 슬라이싱
str = 'Python Programming'
print('처음부터 4글자:', str[0:4]) #0번부터 4글자인거임, 범위 설정
print('처음부터 4글자:', str[:4]) #생략하면 알아서 0번부터 반환
print('7번째문자부터 4글자:', str[7:]) #생략하면 알아서 끝까지 문자를 반환해줌
print('마지막 5글자:', str[-5:])

# 4. 주요 문자열 메소드(문자열이 가지고 있는 함수)
str = '   P y t h o n    '
print('공백제거:', str.strip()) #앞뒤 공백만 제거, 글자 사이 공백은 제거 못함
print('원본:', str)
print('모두 대문자:', str.upper())
print('모두 소문자:', str.lower())
print('문자 교체:', str.replace('P', 'J')) #글자 사이의 공백을 제거하고 싶으면 replace 사용하기
print('문자 사이까지 공백제거:', str.replace(' ', ''))

print('   가나다라   '.strip())

