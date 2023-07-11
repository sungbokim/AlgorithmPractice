#조코딩의 파이썬 기초 강의 -점프투파이썬(파이썬 날개 달기)
#immutable(정수,실수,문자열,튜플)-:변하지 않는것         mutable(리스트,딕셔너리,집합):변할 수 있는것
#클래스: 반복되는 변수&메서드(함수)를 미리 정해놓은 틀(설계도)
# class FourCal:
#     def setdata(self,first,second):     #클래스 안에 있는 함수:메서드
#         self.first=first
#         self.second=second                    

#     def add(self):
#         result= self.first+self.second
#         return result
                                    
# a=FourCal()
# a.setdata(4,2)                          #객체 a가 self로 들어감, 4가 first로 들어감, 2가 second로 들어감
# print(a.add())
#------------------------------------------------------------------
#__init__ :클래스에서 처음으로 수행됨   (선언할 때 무조건 이것부터 실행됨)   생성자
# class FourCal:
#     def __init__(self,first,second):
#         self.first=first
#         self.second=second
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
    
# a=FourCal(1,2)
# print(a.add())
#------------------------------------------------------------------
#상속              
# class MoreFourCal(FourCal):
#     def pow(self):
#         result=self.first**self.second
#         return result

# a=MoreFourCal(4,2)
# print(a.pow())
#클래스 변수: 클래스에 미리 선언해둔 변수 (공통으로 써야 할때)     객체 변수:각각으로 써야 할때
#모듈? 미리 만들어 놓은 .py파일  (함수, 변수, 클래스)------> 파이썬 파일을 미리 만들어 놓고 가져다가 쓰겠다
# import mod1

# print(mod1.add(1,2))

#위에꺼를 다른 형식으로 사용하는 방법
# from mod1 import add         #mod1이라는 파일에서 add만 가져오겠다
# print(add(1,2))
#----------------------------
#if __name__ == "__main__":   을 사용하는 이유는 mod1에서 만약 print등 값을 출력하는 함수가 있다면 그것들까지 불러와서 그것을 방지하려고
#import를 할때 같은 경로에 있으면 괜찮다 But 다른 파일에 있으면 경로를 추가해줘야 한다
#--------------------------------------------------------------------
#패키지란? 모듈을 여러 개 모아 놓은 것
#예외처리: 오류가 발생했을 때 어떻게 할지 정하는 것
#         try:
#         오류가 발생할 수 있는 구문
#         except Exception as e:              Exception 모든 에러의 부모       else랑 비슷함
#         오류 발생
#         else:
#         오류 발생하지 않음
#         finally:
#         무조건 마지막에 실행

# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# print("성보 화이팅")

#내장함수: 파이썬에 기본적으로 포함하고 있는 함수 (이미 들어가 있는 함수)  ex) print(), type()
# abs -> 절대값
# all -> 모두 참인지 검사
#dir-> 자체적으로 가지고 있는 변수나 함수를 보여줌
# print(dir([1,2,3]))     # 리스트에서 뭘 쓸 수 있는지 보여줌
#divmod     ---->몫과 나머지를 튜플 형태로 돌려줌
#enumerate  -----> 열거하다
#filter     ----> 함수를 통과하여 참인 것만 돌려줌   *자주 쓰임
# def positive(x):
#     return x >0

# a=list(filter(positive,[1,-3,2,0,-5,6]))
# print(a)
#id ----> 주소 값 알아보기
#map ----> 각 요소가 수행한 결과를 돌려줌    *자주 쓰임
# def two_times(x): return x*2
# a=list(map(two_times,[1,2,3,4]))
# print(a)
#zip ---> 자료형을 묶어주는 역할

#외장함수: 라이브러리함수(라이브러리에서 가져다가 쓰는 함수), import해서 쓰는 것
#pickle
#time
#time.sleep
#random ----> 난수 생성
#webbrowser
#계속 생성되기 때문에 필요한게 있을 때 그것을 검색해서 사용하면 된다.
#==========================================================================================================
# 백준 알고리즘 특강 풀기
#10871  x보다 작은수
# N,X=map(int,input().split())
# k=list(map(int,input().split()))

# for i in k:
#     if i<X:
#         print(i)
#3052  나머지 
#1.10개의 숫자 입력받기
# s=set()
# for i in range(10):
#     s.add((int(input()))%42)
# print(len(s))
#2738번    행렬 덧셈
# N,M=map(int,input()split(' '))    #N,M입력 받기

# Mat1=[[0 for _ in range(M)] for _ in range(N)]
# Mat2=[[0 for _ in range(M)] for _ in range(N)]
# Mat3=[[0 for _ in range(M)] for _ in range(N)]      #N*M사이즈 Mat1,Mat2,Mat3 초기화

# N,M =map(int,input().split())
# mat1=[]
# mat2=[]
# mat3= [[0 for j in range(M)]for i in range(N)]

# #입력
# for row in range(N):                                #가로:row
#     col= list(map(int,input().split()))
#     mat1.append(col)
# for row in range(N):
#     col=list(map(int,input().split()))
#     mat2.append(col)
# #더하기
# for row in range(N):
#     for col in range(M):
#         mat3[row][col]= mat1[row][col]+mat2[row][col]
# #출력
# for row in range(N):
#     for col in range(M):
#         print(mat3[row][col], end=' ')
#     print( )

#-------------------------------------------------------------------
#2750번    수정렬하기
#selection sort 선택 정렬
#알고리즘
#1. 배열의 첫번째부터 마지막까지 탐색하여 가장 작은 수를 찾아 배열 첫번째 숫자와 자리를 바꾼다.
#2. 배열의 두번째부터 마지막까지 탐색하여 가장 작은 수를 찾아 배열 두번째 숫자와 자리를 바꾼다.
#3. 배열의 세번째부터 마지막까지 탐색하여 가장 작은 수를 찾아 배열 세번째 숫자와 자리를 바꾼다.
#4. 배열의 마지막번째 순서가 되면 종료한다.
#코드 흐름
#1. 전체에서 가장 작은 수를 찾아 1번째 수와 자리를 바꾼다.
#2. 2번째 수부터 마지막 수 중 가장 작은 수를 찾아 2번째 수와 자리를 바꾼다.
#3. n번째 수부터 마지막 수 중 가장 작은 수를 찾아 n번째 수와 자리를 바꾼다.
#4. n이 마지막 수와 같아질 때까지 반복한다.

# N= int(input())
# a=[]
# for i in range(N):
#     a.append(int(input()))

# a.sort()


# for j in range(N):
#     print(a[j])
#2.42로 나눈 나머지 구하기
#3.나머지로 나눈 값들 중 서로 다른 값 찾기
#----------------------------------------------------------------------------------------------------
#2798번 블랙잭
N,M=map(int,input().split())
a=list(map(int,input().split()))
b=[]

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if a[i]+a[j]+a[k]<=M:
                b.append(a[i]+a[j]+a[k])
                if b[-1]==M:
                    break
print(max(b))
           


