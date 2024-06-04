def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def pollard_algorithm(n:int):

    res:int = 2
    gcd_res:int = gcd((res-1)%n, n)
    B:int = 2

    while gcd_res == 1:
        res **= B
        res %= n
        gcd_res = gcd((res-1)%n, n)
        print(f'{B = } | 2^{B}! mod{n} = {res:<10}| gcd(2^{B}!-1 mod{n}) = {gcd_res})')
        if gcd_res != 1:
            print("--------------------------------")
            print(f'{gcd_res} is a prime factor of {n}.')
            print(f'And {n} = {gcd_res} X {n//gcd_res}')
            print("--------------------------------")
        B += 1
    


if __name__ == "__main__":
    pollard_algorithm(15707)