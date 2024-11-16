s=input()
s1=""
c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        c+=1
    else:
        s1+=s[i-1]+str(c)
        c=1
s1+=s[-1]+str(c)
print(s1)
