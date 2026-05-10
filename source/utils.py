def digital_root(n):
    """Ker(a) — цифровой корень"""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def fib_mod_sequence(count=2000, mod = 100):
    fibs = [0, 1]
    for _ in range(2, count):
        fibs.append((fibs[-1] + fibs[-2]) % mod)
    return fibs