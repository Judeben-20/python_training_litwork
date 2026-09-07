n = int(input())
b = bin(n)[2:]
b = b.replace('0', 'x')
b = b.replace('1', '0')
b = b.replace('x', '1')
print(int(b, 2))