N,X,Y=map(int, input().split())
print('YES' if 0<=Y<=N*X and Y%X==0 else 'NO')
