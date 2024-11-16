A,B,C,X = map(int, input().split())
if (A+B>=X) or (B+C>=X) or (C+A>=X):
    print("YES")
else:
    print("NO")
