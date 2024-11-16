n=int(input())
sign=-1 if n<=0 else 1
n=abs(n)
num=int(str(n)[::-1])*sign
if -2**31<=num<=2**31+1:
    print(num)
else:
    print('0')
