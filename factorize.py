def factorize(n:int) -> tuple[int, int]:
    k:int = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return (k, n)


if __name__ == '__main__':
    n = 48
    k, r = factorize(n)
    print(f'2^k*r = 2^{k}*{r} = {n}')
