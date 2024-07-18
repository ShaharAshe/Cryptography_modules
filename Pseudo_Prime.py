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
        for i in range(k):
            if res[-1] == 1 or res[-1] == n-1:
                if i == 0:
                    print(f'_______________________________')
                    print(f"[Miller Rabin] - {n} is a Strong pseudo prime to base {a}")
                    print(f'[Fermat] - {n} is a pseudo prime to base {a}')
                    print(f'_______________________________')
                    return
                else:
                    print(f'_______________________________')
                    print(f"[Miller Rabin] - {n} is a composite number to base {a}")
                    print(f'[Fermat] - {n} is a pseudo prime to base {a}')
                    print(f'_______________________________')
                    return
            res.append((res[i]**2) % n)
            print(f'b{i+1} = {res[i]}^2 = {res[-1]} mod {n}')
            if res[-1] == 1 or res[-1] == n-1:
                print(f'_______________________________')
                print(f"[Miller Rabin] - {n} is a composite number to base {a}")
                print(f'[Fermat] - {n} is a pseudo prime to base {a}')
                print(f'_______________________________')
                return
        
        print(f'_______________________________')
        print(f"[Miller Rabin] - {n} is a composite number to base {a}")
        print(f'[Fermat] - {n} is a composite number to base {a}')
        print(f'_______________________________')


if __name__ == "__main__":
    start=5
    end=7

    n=6601
    for i in range(start, end+1):
        pseudo_prime(i, n)
        print("/////////////////////////////////", end='\n\n')