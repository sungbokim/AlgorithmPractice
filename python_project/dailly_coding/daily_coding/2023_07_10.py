#점프 투 파이썬   6장
#1. 입력과 출력을 생각하라
# def gugu(n):
#     result=[]
#     i=1
#     while i<10:
#         result.append(n*i)
#         i=i+1
#     return result
# print(gugu(2))
#---------------------------------------------------
#7장    문자 셋 표준: 아스키
#입출려과 인코딩
#1.입력으로 받은 바이트 문자열은 되도록 빨리 유니코드 문자열로 디코딩한다.
#2.함수나 클래스 등에서는 유니코드 문자열만 사용한다. 
#3.입력에 대한 결과를 전송하는 마지막 부분에서만 유니코드 문자열을 바이트 문자열로 인코딩해서 반환한다.
#클로저: 함수 안에 내부 함수를 구현하고 그 내부 함수를 리턴하는 함수
#점프 투 파이썬 -라이브러리 예제 편
# import textwrap
# long_text= 'Life is too short, you need python.'*10
# result=textwrap.wrap(long_text,width=30)
# print('\n'.join(result))
#정규표현식: 복잡한 문자열을 처리할 때 사용하는 기법(파이썬에서 이용할려면 re모듈을 사용)
# data='''
# 홍기동의 주민번호는 800905-1049118입니다. 
# 그리고 고길동의 주민번호는 700905입니다.
# 그렇다면 누가 형님일까요?
# '''

# result=[]
# for line in data.split("\n"):
#     word_result=[]
#     for word in line.split(""):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word = word[:6] + "-" + "*******"
#         word_result.append(word)
#     result.append(" ".join(word_result))
# print("\n".join(result))            과정을 구현한 코드
#re모듈을 사용하면 더욱 간단함
#1436번   영화감독 숌
# N=int(input())
# first=666
# while N != 0:
#     if '666' in str(first):
#         N=N-1
#     if N==0:
#         break
#     first=first+1
# print(first)
#2839     설탕배달
N=int(input())

a,b=N//5,N%5

if b ==0:
    print(a)
else:
    b
    if b%3==0:
        print(a+(b%3))
    else:
        print(-1)
        