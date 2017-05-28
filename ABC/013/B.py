a = int(input())
b = int(input())

print(min(min(a, b)+10 - max(a, b), max(a, b) - min(a, b)))