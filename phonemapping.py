s=input()
l1=['']
d={
    "2":['a','b','c'],
    "3":['d','e','f'],
    "4":['g','h','i'],
    "5":['j','k','l'],
    "6":['m','n','o'],
    "7":['p','q','r','s'],
    "8":['t','u','v'],
    "9":['w','x','y','z']
}
for i in s:
    l2=[]
    for j in l1:
        for k in d[i]:
            l2.append(j+k)
    l1=l2
print(l1)