n = int(input())
a = list(map(int, input().split()))
if sum(a) % n != 0:
    print(-1)
    quit()
ave = sum(a) // n
ans = 0
temp_sum = 0
temp_island = 0
for i in a:
    temp_sum += i
    temp_island += 1
    if temp_sum / temp_island != ave:
        ans += 1
    else:
        temp_sum = 0
        temp_island = 0
print(ans)
