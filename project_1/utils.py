def digital_root(n: int) -> int:
    """Ker(a) — цифровой корень"""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9


def fib_mod_sequence(count: int = 2000, mod: int = 100) -> list:
    fibs = [0, 1]
    for _ in range(2, count):
        fibs.append((fibs[-1] + fibs[-2]) % mod)
    return fibs