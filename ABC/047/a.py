candy = list(map(int, input().split()))
candy.sort()
if candy[0] + candy[1] == candy[2]:
    print('Yes')
else:
    print('No')
