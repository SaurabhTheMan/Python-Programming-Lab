# Prime Number
def is_prime(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(4), is_prime(3))
