
n = int(input())
ng = []
for i in range(3):
    ng.append(int(input()))
count = 0
ans = "YES"
if n in ng:
    ans = "NO"
else:
    while n > 0 and count <= 100:
        if n - 3 >= 0 and n - 3 not in ng:
            count += 1
            n -= 3
        elif n - 2 >= 0 and n - 2 not in ng:
            count += 1
            n -= 2
        elif n - 1 >= 0 and n - 1 not in ng:
            count += 1
            n -= 1
        else:
            count += 100
    if count > 100:
        ans = "NO"
print(ans)
# import math
#
# n = int(input())
# ng = []
# temp = 0
# for i in range(3):
#     ng.append(int(input()))
# ng.sort(reverse=True)
#
# ans = "YES"
# if ng[0] - ng[2] < 3:
#     ans = "NO"
# else:
#     temp += math.ceil((n-ng[0])/3)
#     temp += math.ceil((ng[0] - ng[1]) / 3)
#     temp += math.ceil((ng[1] - ng[2]) / 3)
#     temp += math.ceil((ng[2] - 0) / 3)
#     if temp > 100:
#         ans = "NO"
# print(ans)
