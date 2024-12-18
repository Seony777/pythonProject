'''
파일명: EX02-0-summary

변수 - 값을 담을수 있는 메모리 저장 공간
    변수명 = 값 형식으로 저장

변수타입(값 종류)
    기본형
        1. 부울(BOOL) - True, False
            부울변수1 = True
            부울변수2 = False
        2. 정수형(int) - 메모리 허용 음수, 0, 양수
            num = 1
            num2 = 2
        3. 실수형(float) - 소수점 포함 숫자
            fnum = 3,14
            fnum2 = 2.7
        4. 문자열(str) - 문자 저장 쌍따옴표(") 또는 작은 따옴표(') (문자는 한글자를 뜻하고 단어이상은 문자열이라 한다)
            str1 = 'Hello'
            str2 = " 안녕하세요"
    컬렉션형(자료구조형)
        1. list - 순서가 있는 데이터 집합(리스트 안에 들어갈 수 있는 데이터들은 기본형들과 컬렉션형도 가능)
            list = ['값1', '값2', '값3']
            list2 = ['값1', 10, 3.14, True]
        2. Tuple - list와 비슷하지만 수정 불가능
            tuple1 = ('값1', '값2', '값3')
            tuple2 = ('값1', 10 , 3.14)
        3. Set - 순서가 없고, 중복허용 하지 않는 데이터 집합
            set1 = {'값1', '값2', '값3'}
            set2 = {'값1', 10, 3.14}

변수명.메소드()
파이썬은 변수라 해도 전부 다 객체이다.
ex) str1 = '안녕하세요'
변수명: str1
변수 타입: str
값: '안녕하세요'

str이라는 타입에는 이미 여러 기능들이 만들어져 있다
strip()
upper()
lower()
replace()
.....

따라서 str1.upper()을 했을 때
값의 소문자를 대문자로 변경하는 기능을 사용하는 것이다.

타입마다 기능들이 조금씩 다르다
타입마다의 기능을 보고 싶다면 파이참에서 커서를 올려보면 기능들을 설명하는 url이 뜰 것이다.(구글링이나 챗gpt 사용하는 것을 추천)

값 자체가 하나의 타입이라 값을 작성하는 순간 값이 메모리 어딘가에 올라가게 된다. 변수는 그 값의 주소값이라고 생각하면 편함
값.strip() 이렇게 사용해도 가능



'''