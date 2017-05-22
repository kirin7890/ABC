n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = list(set(a))
a.sort(reverse=True)
print(a[1])