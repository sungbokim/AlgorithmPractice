# def add(a,b):
#     print("%d,%d의 합은 %d입니다."%(a,b,a+b))

# a = add(3,4)
# print(a)
#---------------------------------------------------
#함수 안에서 선언한 변수의 효력 범위
#vartest.py
# a=1
# def vartest(a):
#     a=a+1

# vartest(a)
# print(a)
#------------------------------------------------------
#한 줄에 결괏값 출력하기
# for i in range(10):
#     print(i,end="!")  #  end = "(넣고 싶은 거 넣으면 그대로 출력)""
#-------------------------------------------------------
#파일 생성하기
# f =open("새파일.txt",'w')
# f.close()
#-------------------------------------------------------
#파일을 쓰기 모드로 열어 출력값 적기
# f= open("ㅈ파일.txt",'w')     #C:/doit디렉토리에다가 새파일이라는 이름의 txt형식의 파일 생성
# for i in range(1,11):                 #1부터 10까지 i에 대입
#     data ="%d번째 줄입니다.\n"%i       # \n은 줄바꿈 문자, %d는 정수를 나타내는 서식 지정자
#     f.write(data) # data를 파일 객체 f에 써라
# f.close()
#---------------------------------------------------------
#readline 함수 사용하기
# f=open("새파일.txt",'r')
# line=f.readline()
# print(line)
# f.close()
#모든 줄을 읽어서 화면에 출력하고 싶을 때
# f=open("새파일.txt",'r')
# while True:
#     line=f.readlines()
#     if not line: break
#     print(line)
# f.close()                  #while True:무한 루프 안에서 f.readline()을 사용해 파일을 계속해서 한 줄씩 읽어 들인다. 만약 더 이상 읽을 줄이 없다면 break를 수행한다.
#--------------------------------------------------------
# #read함수 사용하기
# f=open("새파일.txt",'r')
# data=f.read()
# print(data)
# f.close()
#----------------------------------------------------------
#이미 존재하는 파일을 열고 원래의 값을 유지하면서 단지 새로운 값을 추가해야할때
#파일을 추가모드('a')로 열면 된다.
# add_data.py
# f = open("새파일.txt",'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()
#------------------------------------------------------------------------
#파일을 열면 항상 닫아주어야한다-----open과 close같이 사용
#파일을 열고 닫는 것을 자동으로 처리할 수 있게 해주는 것: with문
# file_with.py
# with open("새파일.txt", "w") as f:
#     f.write("Life is too short, you need python")   #with문을 사용하면 with문에 속해 있는 문장을 벗어나는 순간, 열린 파일 객체f가 자동으로 닫힌다.
#----------------------------------------------------------------------
#프로그램의 입출력
#type 바로 뒤에 적힌 파일 이름을 인수로 받아 해당 파일의 내용을 출력해 주는 명령어
#명령어 [인수1 인수2.......]
#----------------------------------------------------------------------------
#sys모듈을 사용하여 프로그램에 인수를 전달 가능. (사용할려면 import명령어를 사용해야함)
#sys모듈의 argv  프로그램 실행 시 전달된 인수
#-----------------------------------------------------------------------------------
# calculator.py
# result = 0

# def add(num):
#     global result
#     result += num  # 결괏값(result)에 입력값(num) 더하기
#     return result  # 결괏값 리턴

# print(add(3))
# print(add(4))
#한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까? 각 계산기는 각각의 결과값을 유지해야 함
# calculator2.py
# result1 = 0
# result2 = 0

# def add1(num):  # 계산기1
#     global result1
#     result1 += num
#     return result1

# def add2(num):  # 계산기2
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))
#-------------------------------------------------------
# calculator3.py
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
#-------------------------------------------------------
# #빼기기능 추가   calculator클래스에 다음 함수 추가
# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

#     def sub(self, num):
#         self.result -= num
#         return self.result
# #클래스와 객체
#05-01(클래스)
# calculator.py   더하기 기능을 구현한 파이썬 코드
# result = 0

# def add(num):
#     global result
#     result += num  # 결괏값(result)에 입력값(num) 더하기
#     return result  # 결괏값 리턴

# print(add(3))
# print(add(4))
#-----------------------------------------------------------------
# #calcurator2.py   2대의 더하기 기능을 가진 계산기 만들기(각각의 결괏값을 유지해야 한다.)
# result1=0
# result2=0

# def add1(num): #계산기 1
#     global result1
#     result1 +=num
#     return result1

# def add2(num): #계산기2
#     global result2
#     result2 += num
#     return result2
# #똑같은 일을 하는 add1과 add2함수를 만들고 각 함수에서 계산한 결괏값을 유지하면서 저장하는 전역 변수 result1과 result2를 정의
# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))
#------------------------------------------------------------------------------------------------
# #calcurator3.py   ------위에꺼를 클래스로 만들어 낸것    
# class Calcurator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self,num):
#         self.result +=num
#         return self.result
    
# cal1=Calcurator()
# cal2=Calcurator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))
#------------------------------------------------------------------------------------------------
#클래스(class): 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀)
#객체(object): 클래스로 만든 피조물
# 사칙 연산 클래스 만들기                   *제일 먼저 해야 할 일:객체를 만들수 있게 하는 것
# class FourCal:                            #현재 상태에서 FourCal 클래스는 아무 변수나 함수도 포함하지 않지만, 우리가 원하는 객체a를 만들 수 있는 기능은 가지고 있다.
#     pass                                  #pass는 아무것도 수행하지 않는 문법, 임시로 코드를 작성할 때 주로 사용
# a=FourCal()
# #아직까지는 생성된 객체 a는 아직 아무런 기능도 하지 못한다. 기능을 하는 객체를 만들어야 한다.
# a.setdata(4,2)    #기능을 수행할 대상을 객체에 지정할 수 있게 만들자
# class FourCal:
#     def setdata(self,first,second):      #메서드의 매개변수
#         self.first=first                 #메서드의 수행문
#         self.second=second               #메서드의 수행문
# #앞에서 만든 FourCal클래스에서 pass 문장을 삭제--->setdata함수를 정의     (클래스 안에 구현된 함수: 메서드method)        
# a=FourCal()
# a.setdata(4,2)
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second


# a = FourCal()
# a.setdata(4, 2)
# print(a.first)
#객체에 생성되는 객체만의 변수: 객체변수, 속성
#클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지
#더하기 기능 만들기
# class FourCal:
#     def setdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
# a=FourCal()
# # a.setdata(4,2)
# # print(a.add())
# #-------------------------------------------------------------------------------------------
# #곱하기,빼기,나누기 기능 추가
# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second= second
#     def add(self):
#         result=self.first+self.second
#         return result
#     def mul(self):
#         result=self.first*self.second
#         return result
#     def sub(self):
#         result=self.first-self.second
#         return result
#     def div(self):
#         result=self.first/self.second
#         return result

# a=FourCal()    
# b=FourCal()
# a.setdata(4,2)
# b.setdata(3,8)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(b.add())
# print(b.mul())
# print(b.sub())
# print(b.div())
#------------------------------------------------------------------------------
# #생성자: 객체가 생성될때 자동으로 호출되는 메서드  ---> _init_ 을 사용하면 메서드 생성됨
# class FourCal:
#     def __init__(self,first,second):    #메서드 이름을 _init_ : 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이가 있다!
#         self.first = first
#         self.second= second
#     def satdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
#     def mul(self):
#         result=self.first*self.second
#         return result
#     def sub(self):
#         result=self.first-self.second
#         return result
#     def div(self):
#         result=self.first/self.second
#         return result
# # a=FourCal()
# # a.setdata(4,2)
# # print(a.add())      위에 처럼 하면 안됨: 이유? a=FourCal()을 수행할 때 생성자 _init_가 호출되어 ..생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았다.

# a=FourCal(4,2)      #매개변수  self/first/second 에 ------> 생성되는 객체/4/2
# # a.first
# # print(a.first)    
# # print(a.second)
# print(a.add())
# print(a.div())    
#-------------------------------------------------------------------------------------
#클래스의 상속    : 어떤 클래스를 만들 때, 다른 클래스의 기능을 물려받을 수 있게 만드는 것
# class FourCal:
#     def __init__(self,first,second):    #메서드 이름을 _init_ : 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다는 차이가 있다!
#         self.first = first
#         self.second= second
#     def satdata(self,first,second):
#         self.first=first
#         self.second=second
#     def add(self):
#         result=self.first+self.second
#         return result
#     def mul(self):
#         result=self.first*self.second
#         return result
#     def sub(self):
#         result=self.first-self.second
#         return result
#     def div(self):
#         result=self.first/self.second
#         return result
#FourCal클래스를 상속하는 MoreFourCal 클래스 만들기  (a**b값을 구하는 기능 추가)
# class MoreFourCal(FourCal):             
#     class 클래스_이름 (상속할_클래스_이름)
# a=MoreFourCal(4,2)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())       #MoreFourCal 클래스는 FourCal클래스를 상속, 즉 FourCal기능을 모두 사용가능
#     def pow(self):                       
#         result=self.first**self.second          #a**b기능 추가
#         return result
# a=MoreFourCal(4,2)
# print(a.pow())
#------------------------------------------------------------------
# 메서드 오버라이딩    부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것(오버라이딩한 메서드가 호출)
# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:      #나누는 값이 0인 경우 0을 리턴하도록 수정
#             return 0
#         else:
#             return self.first / self.second
#-------------------------------------------------------------------
# #클래스 변수: 객체변수는 다른 객체들의 영향을 받지 않고 독립적으로 그 값을 유지한다는 점(객체변수와는 성격이 다름)
# class Family:
#     lastname="김"
# print(Family.lastname)     #클래스변수는   클래스_이름.클래스변수 로 사용가능
# Family.lastname="박"    
# a= Family()
# b= Family()                     #클래스 변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 점
# print(a.lastname)
# print(b.lastname)
#--------------------------------------------------------------------
#모듈 : 함수나 변수 또는 클래스를 모아 놓은 파일 / 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일
#daily_sub
# import daily_coding.mod as mod          #import는 이미 만들어진 파이썬 모듈을 사용할 수 있게 해 주는 명령어   사용방법: import (모듈_이름에서 .py확장자를 제거한 것)
# print (mod)       #from 모듈이름 import 모듈 함수 ----> 이렇게 하면 함수 하나만 사용가능
# mod1.py의 함수 두개를 모두 다 사용하고 싶을 때: 1.   from 모듈이름 import 모듈함수1, 모듈함수2   2.  from 모듈이름 import*   :해당 모듈의 모든 함수를 불러온다
# 모듈은 클래스,변수,함수 등을 포함할수도 있다.




















