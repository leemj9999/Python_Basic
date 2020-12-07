### Python 표준 입출력 ###

import sys

#sep은 사이사이에 넣는거
#end는 맨끝에 줄안바꾸고 넣기
print("파이썬",'씨플플', "자바",sep = 'vs',end = '??')

#file=sys.stdout은 표준출력시 print하라
print("파이썬",'씨플플', "자바",file=sys.stdout)

#file=sys.stderr는 표준에러시 print하라
print("파이썬",'씨플플', "자바",file=sys.stderr) # 에러에 대해 따로 로깅

# ljust(8)는 왼쪽정렬하는데 8자리를 만들어라
# rjust(4)는 오른쪽정렬하는데 4자리를 만들어라
scores = {'수학':0, '영어':50, '코딩':100 } #scores는 딕셔너리: Key와 Value로 이루어져있다.
for subject, score in scores.items(): #items는 key와 value를 쌍으로 튜플로 보내준다.
    print(subject.ljust(8),str(score).rjust(4),sep=":")


# <문자열.zfill(n)>
# 뜻 : zeros + fill : n크기만큼 공간을 확보하고 값이없는 부분은 0으로 채워라
# zfill(n) 앞에는 String !! 그리고 n은 integer형
# 은행 대기순번표
#001, 002, 003, ...
for num in range(1,21):
    print("대기번호" , str(num).zfill(3), sep=" : ")


# <표준입력>
# 숫자를 입력해도 잘 출력되네? -> 사용자 입력을 통해서 값을 받게 되면 항상 str형으로 저장이된다.
answer = input("아무값이나 입력하세요")
print(type(answer))
print("입력하신값은 " + answer + "입니다")
