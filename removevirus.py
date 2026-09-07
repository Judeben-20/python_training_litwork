N=int(input())
a=list(map(int,input().split()))
n=int(input())
for i in a:
  x=i
  for j in range(n):
    x=x//2
  print(x,end=" ")