#10871
# N,x=map(int,input().split())
# line=list(map(int,input().split(' ')))
# print(line)

# for value in  line:
#     if value < X:
#         print(value,end='')

#-------------------
# n,m=map(int,input.split(' '))

# mat1=[]#: 1번째 입력 받는 매트릭스
# mat2=[]#: 2번째 입력 받는 매트릭스
# mat3=[]#출력 받는 매트릭스

# for row in range(n):
#     cpl = input(int.split(' '))
#     col = list(map(int,input().split()))
#     mat1.append(col)
#----------------------------------------------------
# n=int(input())

# arr=list(map(int,input().split()))
# print('input:',arr)

# for i in range(n-1):
#     min_idx= i
#     for j in range(i+1,n):
#         if arr[min_idx] > arr[j]:
#             min_idx=j
#         print(i+1, "번째 작은 수:", arr[min_idx],"------>",sep='',end='')
#         #swap
#         arr[i],arr[min_idx] = arr[min_idx],arr[i]
#         print(arr)

# print("output:",arr)
#----------------------------------------
# n, m = map(int, input().split(' '))
# mat1 = []
# mat2 = []
# mat3 = [[0 for j in range(m)] for i in range(n)]
# # 입력
# for row in range(n):
#     col = list(map(int, input().split()))
#     mat1.append(col)
# for row in range(n):
#     col = list(map(int, input().split()))
#     mat2.append(col)
# # 더하기
# for row in range(n):
#     for col in range(m):
#         mat3[row][col] = mat1[row][col] + mat2[row][col]
# # 출력
# for row in range(n):
#     for col in range(m):
#         print(mat3[row][col], end=' ')
#     print()
#---------------------------------------------
# n=int(input())

# arr=list(map(int,input().split()))

# def swap(lst,a,b):
#     tmp=lst[a]
#     lst[a]=lst[b]
#     lst[b]=tmp
#     return 1

# swap(arr,0,3) # arr의 0번째와 3번째를 바꿔볼게

# print()
# print(arr)
#--------------------------------------------

# N=int(input())
# arr = []

# for i in range(N) :
#     arr.append(int(input()))

# for i in range(N-1):
#     min_idx= i
#     for j in range(i+1,N):
#         if arr[min_idx] > arr[j]:
#             min_idx=j

#         arr[i],arr[min_idx] = arr[min_idx],arr[i]
        

# print(*arr)

#------------------------------
# password=2134
# for password_ in range(0,10000):
#     if password ==password_:
#         print("정답은:",password_)
#         break
#---------------------------------------------------
height_sum=0
heigth_list=[]

for i in range(9):
    height=int(input())
    height_sum=height_sum+ height
    htight_list.append(height)
height_list.sort()

for first in range(9):
    for second in range(9):
        if first==second:
            continue
        height_total=height_sum - heigth_list[first] - height_list[second]
        if height_sum==100:
            heigth_list.remove(height_list(first))
            heigth_list.remove(height_list(second))
            is_ok= True
            break
    if is_ok:
        break
print(heigth_list)