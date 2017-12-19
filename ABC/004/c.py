n = int(input())%30
card = [1, 2, 3, 4, 5, 6]
for i in range(n):
    card[i%5], card[i%5+1] = card[i%5+1], card[i%5]
ans = str()
for i in card:
    ans += str(i)
print(ans)
