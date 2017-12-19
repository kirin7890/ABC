e = list(input())
ans = 'Yes'
for i in e:
    if e.count(i) % 2 != 0:
        ans = 'No'
print(ans)
