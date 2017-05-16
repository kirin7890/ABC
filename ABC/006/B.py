n = int(input())

a = [0, 0, 1]

if n <= 3:
    print (a[n-1])
else:
    for i in range(n):
        a.append((a[i-1+3] + a[i-2+3] + a[i-3+3])%10007)
    print (a[n-1])
