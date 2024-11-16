N=int(input())
arr=list(map(int, input().split()))
list=[]
for i in arr:
    if i not in list:
        list.append(i)
print(*list)
