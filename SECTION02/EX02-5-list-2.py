'''
파일명: EX02-5-list-2.py

리스트 주요 메소드
    -append(): 끝에 항목 추가
    -insert(): 지정 위치에 항목 추가
    -remove(): 항목 제거
    -pop(): 마지막 또는 지정위치 제거하고 반환
    -clear(): 리스트 비우기
'''
from platform import release

# 1. 리스트 기본 메소드
starter_poketmon = ['피카츄', '파이리', '꼬부기']
starter_poketmon.append('이상해씨') #끝에 추가
print('스타터 포켓몬:', starter_poketmon)
starter_poketmon.insert(1,'잠만보') #중간 삽입(삽입하는 인덱스 위치에 넣고 원래 있던 것은 뒤로 밀림)
print('삽입된 포켓몬', starter_poketmon)

# 2. 리스트 제거 메소드
legendary_poketmon = ['그라돈', '가이오가', '레쿠자', '히드런']
print('전설의 포켓몬:', legendary_poketmon)

legendary_poketmon.remove('히드런') #제거하고 싶은 값 입력
print('방출 후:', legendary_poketmon)

release = legendary_poketmon.pop(1)  #인덱스로 제거 / 인덱스 번호를 안쓰면 끝에서부터 제거함
print('현재 남은 포켓몬:', legendary_poketmon)
print('방출된 포켓몬:', release)

# 3. 리스트 확장과 초기화
a_team = ['나무지기','가디안']
b_team = ['불꽃송이','팽도리']
c_team = a_team+ b_team
print('연합팀1:', c_team)

a_team.extend(b_team) #a팀에 b팀을 추가한다고 생각하면 됨
print('연합팀2:',a_team)

a_team.clear() #리스트 비우기
print('리셋된 팀:', a_team) #안에 있는 요소들이 삭제된 거지 리스트는 남아 있음

del a_team # 리스트라는 객체 자체를 삭제(del은 함수라기보단 파이썬에서 정해준 기본 명령어임, print는 내장함수! / del은 값만 없애주는 것이 아니라 메모리에서 객체자체를 없애줌)
