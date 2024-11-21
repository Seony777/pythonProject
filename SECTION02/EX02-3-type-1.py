#1. 문자열 타입
'''
파일명: EX02-3-type-1.py

기본 데이터 타입:
    -문자열(str): 문자열 저장
    -정수(int): 숫자를 저장
    -실수(float): 소수점 있는 숫자를 저장
    -불린(bool): 참/거짓(True/False) 저장

    단어 단위 커서 이동: ctrl+ 방향키
    줄 단위 커서 이동: ctrl+ shift+ 위아래 방향키

'''
text = 'Hello world'
print('문자열:', text)
print('문자열 타입:', type(text))

#2. 숫자 타입
integer = 20
float_number = 20.5
print('정수:',integer)
print('정수 타입:', type(integer))
print('실수:',float_number)
print('실수 타입:', type(float_number))

#3.불린 타입
bool_true = True
bool_false= False
print('불린1:', bool_true)
print('불린2 타입:', type(bool_true))
print('불린2:', bool_false)
print('불린2 타입:', type(bool_false))

text1 = '이선우'
text2 = '변영찬'
text3 = text1+text2
print(text3)