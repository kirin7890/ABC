n = int(input())
a = list(map(int, input().split()))

a.sort()
color = []
other = 0
for i in a:
    if i < 400 * 1:
        color.append('1')
    elif i < 400 * 2:
        color.append('2')
    elif i < 400 * 3:
        color.append('3')
    elif i < 400 * 4:
        color.append('4')
    elif i < 400 * 5:
        color.append('5')
    elif i < 400 * 6:
        color.append('6')
    elif i < 400 * 7:
        color.append('7')
    elif i < 400 * 8:
        color.append('8')
    else:
        other += 1
max_ans = len(set(color)) + other
min_ans = len(set(color))
if min_ans == 0 and other != 0:
    min_ans = 1
print(min_ans, max_ans)
