n = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


a, b = 1, 1
for i in range(n):
    a = b
    b = lcm(a, int(input()))
print(b)
