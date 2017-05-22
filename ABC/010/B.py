n = int(input())
a = map(int, input().split())
count = 0
for x in a:
    y = x
    while y % 2 == 0 or y % 3 == 2:
        count += 1
        y -= 1
print(count)
