def gcd(num_1:int, num_2:int) -> int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def factorize(n:int) -> tuple[int, int]:
    k:int = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return (k, n)


def rabin_miler(n:int, a:int) -> int:
    k, r = factorize(n-1)

    print("---------------------------------")
    print(f'{a = }')
    print(f'n = {n}, k = {k}, r = {r}', end='\n\n')

    res:list = [(a**r) % n]
    print(f'b0 = {a}^{r} = {res[0]} mod {n}')
    for i in range(k-1):
        if res[-1] == 1 or res[-1] == n-1:
            break
        res.append((res[i]**2) % n)
        print(f'b{i+1} = {res[i]}^2 = {res[-1]} mod {n}')

    print("/////////////////////////////////")
    if res[-1] == 1:
        if len(res) == 1:
            print(f'{n} is probably prime')
        else:
            print(f'{res[-2]} is a witness for {n} being composite')
            return res[-2]
    elif res[-1] == n-1:
        if len(res) == 1:
            print(f'{n} is probably prime')
        else:
            print(f'{res[-2]} is not a witness for {n} being composite')
            return res[-2]
    else:
        print(f'{n} is composite')
        return res[-1]
    print("/////////////////////////////////")
    return 1


def composite(n:int, start:int, end:int) -> None:
    for i in range(start, end+1):
        result:int = rabin_miler(n, i)
        if result != 1:
            temp_gcd:int = gcd(n, result-1)
            print(f'gcd({n}, {result}) = {temp_gcd}')
            if temp_gcd != 1 and temp_gcd != n:
                print(f'and we found that the composite is {n} = {temp_gcd} * {n//temp_gcd}', end='\n/////////////////////////////////')
                break
            print("/////////////////////////////////")
        print()
        

if __name__ == "__main__":
    composite(n=47197, start=2, end=10)
