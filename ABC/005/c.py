t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
count = 0
for i in b:
    for j in range(len(a)):
        # print(j, a[0], t, i)
        temp = a.pop(0)
        if temp <= i <= temp + t:
            count += 1
            break
if count == m:
    print('yes')
else:
    print('no')
