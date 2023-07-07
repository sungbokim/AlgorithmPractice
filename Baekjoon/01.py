#백준문제
# a=input()
# b=input()
# c=int(a)*int(b[2])
# d=int(a)*int(b[1])
# e=int(a)*int(b[0])
# f= c+d*10+e*100
#
# print(c)
# print(d)
# print(e)
# print(f)

#-------------------------------------
# a=0
# b=0
# c=0
#
# a,b,c= map(int, input().split())
#
# print(a+b+c)
#-------------------------------------
# a,b =map(int,input().split())
# if a>b:
#     print('>')
# elif a<b :
#     print('<')
# elif a==b :
#     print("==")
#--------------------------------------
# score=int(input())
# if score >= 90 and score <= 100:
#     print("A")
# elif score >= 80 and score <90:
#     print("B")
# elif score >= 70 and score < 80:
#     print("C")
# elif score >= 60 and score < 70:
#     print("D")
# elif score >= 0 and score <60:
#     print("F")
# else:
#     print("error")
#-----------------------------------------
# a= int(input())
# if a%4==0and (a%100!=0 or a%400==0):
#     print("1")
# else:
#     print("0")
#---------------------------------------------
# x=int(input())
# y=int(input())
# if x>=0 and y>=0:
#     print("1")
# elif x<0 and y>=0:
#     print("2")
# elif x>=0 and y<0:
#     print("4")
# elif x<0 and y<0:
#     print("3")
# else:
#     print("o")
#------------------------------------------------
# hour,minute =map(int,input().split())
# if minute<45 and hour ==0:
#     new_hour=23
#     new_minute=15+minute
# elif minute<45 and hour!=0:
#     new_hour = hour - 1
#     new_minute =15+minute
# else:
#     new_minute=minute-45
#     new_hour=hour
#
#
# print(new_hour,new_minute)
#-------------------------------------------------
# h,m =map(int,input().split())
# need=int(input())
# x = m+need
# H=h+(x//60)
# if H >= 24:
#     H=H-24
# M=(x%60)
# print(H,M)
#----------------------------------------------------
# x,y,z=map(int,input().split())
#
# if x == y == z :
#     print(10000+x*1000)
# elif y == z or x == y :
#     print(1000+100*y)
# elif x==z:
#     print(1000+100*x)
# else:
#     print(max(x,y,z)*100)
#-----------------------------------------------------
# N=int(input())
# for i in range(1,10):
#     print(N,"*" ,i ,"=" ,N * i )
#-----------------------------------------------------
# T=int(input())
# for T in range(1,T+1):
#     A,B=map(int,input().split())
#     print(A + B )
#----------------------------------------------------
# n=int(input())
# a=0
# for i in range(1,n+1):
#     a+= i
# print(a)
#-----------------------------------------------------
# X=int(input())
# N=int(input())
# s=0
# for i in range(1,N+1):
#     a,b=map(int,input().split())
#     s+=a*b
# if s ==X:
#     print("Yes")
# else:
#     print("No")
#----------------------------------------------------
# N=int(input())
#
# k=N//4
#
# print(k*"long "+"int")
#---------------------------------------------------
# import sys
# T=int(input())
#
# s=0
# for i in range(1,T+1):
#     A,B=map(int,sys.stdin.readline().split())
#     print(A+B)
#----------------------------------------------------
# T= int(input())
#
# for i in range(1,T+1):
#     A,B= map(int,input().split())
#     print("Case #"+str(i)+":",A+B)
#---------------------------------------------------
# T = int(input())
#
# for i in range(1, T + 1):
#     A, B = map(int, input().split())
#     print("Case #" + str(i) + ":",A, "+",B,"=", A + B)
#---------------------------------------------------
# N= int(input())
#
# for i in range(1,N+1):
#     print(i *"*")
#---------------------------------------------------
# N= int(input())
# for i in range(1,N+1):
#     print((N-i)*" "+i *"*")
# #---------------------------------------------------
# while True :
#     a =list(map(int,input().split()))
#
#     if sum(a)==0 :
#         break
#     print(sum(a))
#-----------------------------------------------------
# while True :
#     try:
#         a =list(map(int,input().split()))
#         print(sum(a))
#     except:
#         break
#---------------------------------------------------
# 첫째줄에 정수의 개수가:n , 둘째줄: 정수가 공백으로 구분
# N=int(input())
# k=list(map(int,input().split()))
# print(k.count(int(input())))
#--------------------------------------------------
# N,X=map(int,input().split())
# k=list(map(int,input().split()))
#
# a=list()
#
# for i in k:
#      if i<X:
#          print(i)
# #-------------------------------------------------
# lst = list(range(0,5))
# print(*lst)
#---------------------------------------------------
# N=int(input())
#
# k=list(map(int,input().split()))
# k.sort()
# print(k[0],k[-1])
#---------------------------------------------------
# x,y=list(map(int,input().split()))

# if x==1,3,5,7,8,10,12:
#------------------------------------------------
# import sys
# a=sys.stdin.readline()
# a=input()
# b=input()
# print(a,b, sep='')
#----------------------------
#입력이 세개가 들어왔을 때 처리방법
# import sys
# a,b,c,d= map(int,sys.stdin.readline().split())
# print(a,b,c,d)
#------------------------------
#리스트로 받아서 저장하겠다
# import sys
# res_list= list(map(int,sys.stdin.readline().split()))
#
#
# print(res_list)
#--------------------------------------
#리스트 안의 리스트(이중 리스트)
# import  sys
# list_in_list=list()
# n=int(input())
# for i in range(n):
#     list_in_list.append(list(map(int,sys.stdin.readline().split())))
# pr/.,../
#-------------------------------------------------------------
# print('hi')
# print()#\n
#
# print("hello","my","name","is")   #각 문자열 사이에 공백이 들어감
# print("hi", end="")#hi
# print("hello","my","name","is",sep="")# sep 는 문자사이에 공백을 줄거냐 안줄거냐
#
# print("hello","my","name","is",sep="\n")# 줄을 띄움
#-------------------------------------------------------------------------
# A,B= map(int,input().split())
# print(A+B)
#__________________________________________________________________________
# A,B= map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)
#-------------------------------------------------------------
# y=int(input())
# print(y-543)
#--------------------------------------------------------------------
# N=int(input())
# for i in range(9):
#     print("%d * %d= %d" %(N, i+1, N * (i+1)))
#---------------------------------------------------------
# n= int(input())
# a=0
# for i in range(1,n+1):
#     a+=i
# print(a)
#----------------------------------------------------------

# a=int(input())
#
# if 89<a<=100:
#     print("A")
# elif 79<a<=89:
#     print("B")
# elif 69<a<=79:
#     print("C")
# elif 59<a<=69:
#     print("D")
# else:
#     print("F")
#------------------------------------------------
#날짜 계산
# x,y=map(int,input().split())
#
# month=[[1,3,5,7,8,10,12],[4,6,9,11],[2]]
# day=[28,30,31]
# D=0
# if x in month[0]:
#     D=day[2]
# elif x in month[1]:
#     D=day[1]
# elif x in month[2]:
#     D=day[0]
#
#
#
#
# print(a)
#--------------------------------------------------------
# N=int(input())
# for i in range(9):
#     print("%d * %d = %d" %(N, i+1, N * (i+1)))
#-----------------------------------------------------
# A,B=map(int,input().split())
#
# if A>B:
#     print(">")
# elif A<B:
#     print("<")
# else:
#     print('==')
#=======================================================
# year=int(input())
# #
# # if year%4==0 and (year%100!=0 or year%400==0):
# #     print("1")
# # else:
# #     print("0")
#--------------------------------------------------------
# 별찍기 문제

# N=int(input())
#
# for i in range(1,N+1):
#     print((2*i-1)*'*')
#------------------------------------------------------
# import sys
# list_in_list=list()
# n=int(sys.stdin.readline())
# for i in range(n):
#     list_in_list.append(list(map(int,sys.stdin.readline().split())))
# print(list_in_list)
#_________________________________________________________
# fruits=["사과","배","오렌지"]
#
# for idx, value in enumerate(fruits):
#     print(idx)
#-----------------------------------------------------------
# for y in range(0,5):
#     print(f"y:{y}")
#------------------------------------------------------------
# c="i have {} apple".format(5)
# print(c)
#
# d=f'i have {5} apple'
# print(d)
#----------------------------------------------------------
# N=int(input())
#
# for i in range(1,N+1):
#     print(i*"*"+(i-1)*"")
# #----------------------------------------------------------------
# N=int(input())
#
# for i in range(N):
#     print(i*" "+(N-i)*"*")
# #--------------------------------------------------------------
# N=int(input())
#
# for y in range(N):
#     for x in range(2*N-1):
#         print(f'(y:{y},x:{x})',end=' ')
#     print()
#-----------------------------------------------------------
# N=int(input())
#
# for i in range(1,N+1):
#     print(((N-i)*" ")+((2*i)-1)*"*")
#------------------------------------------------------------
# N=int(input())
#
# for i in range(0,N):
#     print(" "*i+"*"*(2*(N-i-1)+1))
#-------------------------------------------------------------
# N=int(input())
#
# for i in range(1,N+1):
#     print(((N-i)*" ")+((2*i)-1)*"*")
# for i in range(N-1,0,-1):
#     print(((N-i)*" ")+((2*i)-1)*"*")
#-----------------------------------------------------------------
# N=int(input())
#
# for i in range(1,N+1):
#     print((i*"*")+2*(N-i)*" "+(i*"*"))
# for i in range(N-1,0,-1):
#     print((i * "*") + 2 * (N - i) * " " + (i * "*"))
# #------------------------------------------------------------------
# N=int(input())
#
# for i in range(0,N):
#     print((i*" ")+2*(N-i)*"*"+(i*" "))
# for i in range(N,0,-1):
#     print((i * " ") + 2 * (N - i) * "*" + (i * " "))
# N=int(input())
#
# for i in range(0,N):
#     print(" "*i+"*"*(2*(N-i-1)+1))
# for i in range(N-1,0,-1):
#     print(" "*(i-1) +"*"*(2*(N-i)+1))
#---------------------------------------------------------
# N=int(input())
#
# for i in range(1,N+1):
#     print((N-i)*" "+"*"*i)
# for i in range(N-1,0,-1):
#     print((N - i) * " " + "*" * i)
#------------------------------------------------------------
# x,y=map(int,input.split())
#
# month=[[1,5,7,8,10,12],[4,6,9,11],[2]]
# days=[[31],[30],[29]]
#
# month[0]=days[0]
# print(month[0])

# x,y=map(int,input().split())

# date=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# day=['SUN','MON','TUE','WED','THU','FRI','SAT']

# count=0
# for i in range(x):
#     count +=date[i]

# result= count+y
# results = day[result%7]
# print(results)

# s=set()
# for i in range(10):
#     s.add((int(input()))%42)
# print(len(s))

# N,M=map(int,input().split())

# basket = [i+1 for i in range(N)]

# for i in range(M):
#     a,b = map(int,input().split())
#     a= a-1; b= b-1
#     tomak1=basket[:a]
#     tomak2=basket[a:b+1]
#     tomak3=basket[b+1:]
#     tomak2.reverse()
#     basket = tomak1+tomak2+tomak3

# print(*basket)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end="")
#     print('')

# #----------------------------------------
# li=[]
# for _ in range(9):
# #     li.append(int(input()))


# # print(max(li))

# # print(li.index(max(li))+1)

# N,M=map(int,input().split())
# li=[0]*N

# for i in range(M):
#     a,b, c =map(int, input().split())
#     for j in range(a-1,b):
#         li[j]=c
# print(*li)
#-----------------------------------------
# N,M=map(int,input().split())

# bascket = [i+1 for i in range(N)]

# for i in range(M):
#     a,b = map(int,input().split())
#     a= a-1; b= b-1
#     bascket[a],bascket[b] = bascket[b], bascket[a]
# print(*bascket)
#---------------------------------------------------

# students= [i+1 for i in range(30)]

# for i in range(28):
#     students.remove(int(input()))
# print(*students)
#---------------------------------------------------

# s=set()
# for i in range(10):
#     set.add((input())%42)

# print(len(s))

    












