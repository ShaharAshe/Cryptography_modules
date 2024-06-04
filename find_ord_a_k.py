def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def ord_k(n, a, b):
    temp_a = a
    for k in range(2, n-1):
        print('-----------------------------------')
        print(f'{k = }')
        temp_a = (temp_a ** k) % n
        print(f'{a}^k = {a}^{k} = {temp_a}')

        gcd_val = gcd(k, (n-1))
        print(f'gcd(k, {n-1}) = {gcd_val}')
        ord_val = (n-1) // gcd_val
        print(f'ord({a}^k) = ord({a}^{k}) = {ord_val}')

        if ord_val == b:
            return (k, ord_val)


if __name__ == "__main__":
    n = 349
    a = 18
    # b = 348
    b = 29
    print(f'We are going to find the value of k such that ord({a}^k) = {b} (mod {n})')
    print('We are going to find that by the formula: ord(a^k) = |G|/gcd(k, |G|)', end='\n\n')
    k, ord_val = ord_k(n, a, b)
    
    print('-----------------------------------', end='\n\n')

    print('===================================')
    print(f'The value of k is: {k}, and the order of {a}^{k} is: {ord_val} (mod {n})')
    print('===================================')