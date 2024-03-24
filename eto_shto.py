def find_min_power(A, B):
    n = 0
    while B % A == 0:
        B //= A
        n += 1
    if B == 1:
        return n
    else:
        return -1

A, B = map(int, input().split())
result = find_min_power(A, B)
print(result)