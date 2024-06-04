def factorize(n:int) -> tuple[int, int]:
    k:int = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return (k, n)


def pseudo_prime(a:int ,n:int):
    print("---------------------------------")
    print(f'{a = }', end='\n\n')

    if (a**n-1)%n == 1:
        print(f'{a}^{n-1} = 1 mod {n}')
        print(f"{n} is a pseudo prime number to base {a}")
    else:
        k, r = factorize(n-1)
        res:list = [(a**r) % n]
        print(f'b0 = {a}^{r} = {res[0]} mod {n}')
        if res[0] == 1 or res[0] == n-1:
            print(f"{n} is a Strong pseudoprime to base {a}")
            return
        else:
            for i in range(k-1):
                if res[-1] == 1 or res[-1] == n-1:
                    print(f"{n} is a Strong pseudoprime to base {a}")
                    return
                res.append((res[i]**2) % n)
                print(f'b{i+1} = {res[i]}^2 = {res[-1]} mod {n}')
        print(f"{n} is not a pseudoprime or a Strong pseudoprime to base {a}")


if __name__ == "__main__":
    for i in range(2, 11):
        pseudo_prime(i, 47197)
        print("/////////////////////////////////", end='\n\n')