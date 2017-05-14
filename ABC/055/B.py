n = int(input())
p = 1

for i in range(n):
    p = p*(i+1)
    p = p % (1000000000+7)
print (p)
