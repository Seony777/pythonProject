'''
파일명: EX02-1-circle.py

shift + tab:왼쪽으로 들여쓰기
tab: 오른쪽으로 들여쓰기

docstring
    파이썬 코드(모듈, 함수, 클래스, 등)의 첫 부분에 문자열("""...""")로 작성하는 문서화 주석입니다.
    함수 위에 커서를 살짝 올리면 docstring으로 설명한 내용이 나타남
    함수를 사용할 때 이해하기 편하기 위한 주석
    공식 함수들은 링크도 달려있어 안에서 설명도 자세히 볼 수 있음
'''

#1. math 모듈포함
import math

#2. 원의 넓이를 계산하는 함수 만들기
def get_area(radius):
    """
    원의 넓이를 계산하는 함수
    :param radius: 반지름
    :return: 원의 넓이
    """
    area = math.pi * math.pow(radius, 2)
    return area


#3. 함수 사용해보기
radius =1.5 # 반지름 값 저장
print('반지름:',radius)

area = get_area(radius)
print("원의 넓이:",area)

# 4. 함수 설명(docstring) 확인하기(
print('함수 설명서:', get_area.__doc__)

help(get_area)
