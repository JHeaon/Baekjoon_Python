a,b,c = map(int, input().split())

b = max(b, a - b)
c = max(c, a - c)
print(b * c * 4)