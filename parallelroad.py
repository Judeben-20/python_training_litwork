n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
c=list(set(a+b))
c.sort()
n=len(c)
if n%2==1:
  print(c[n//2])
else:
  print((c[n//2-1]+c[n//2])/2)