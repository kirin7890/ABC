l = list(map(int, input().split()))
l.sort()
print(sum(l)-l[1]*2)