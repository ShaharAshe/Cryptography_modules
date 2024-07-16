def gcd(num_1:int, num_2:int)->int:
    if num_1 == 0:
        return 0
    return num_1 if num_2 == 0 else gcd(num_2, num_1%num_2)


def square_root(num:int, p:int, q:int, n:int)->int:
    if (p-3)%4 != 0 or (q-3)%4 != 0:
        print("[ERROR] The number is not a square root of 3 mod 4")
        return
    gcd_num_n = gcd(num, n)
    num_of_squares = 0
    roots:list = []
    if gcd_num_n == 1:
        num_of_squares = 4
        print(f"The gcd({num},{n}) = 1, so the number of square roots is 4")
        print(f"The roots are:")

        print('-----------')
        num_1 = num%p
        num_1 = pow(num_1,(p+1)//4,p)
        print(f"{num} mod {p} = {num%p}")
        print(f" -->  ({num%p}^({(p+1)}//4))^2 = ({num_1}, {(-num_1)%p})^2 mod {p}")
        print('-----------')
        num_2 = num%q
        num_2 = pow(num_2,(q+1)//4,q)
        print(f"{num} mod {q} = {num%q}")
        print(f" -->  ({num%q}^({(q+1)}//4))^2 = ({num_2}, {(-num_2)%q})^2 mod {q}")
        print('-----------')

        roots.append(num_1)
        roots.append((-num_1)%p)
        roots.append(num_2)
        roots.append((-num_2)%q)

        print(f"The roots are: {roots}")

        print('\n-----------')
        print(f'check if {num%p} = {pow(num_1, 2, p)}')
        print(f'check if {num%q} = {pow(num_2, 2, q)}')
        print(f'If one of the above is False, then the number {num} has no square roots')
        print('-----------')

        return num_of_squares
    elif gcd_num_n == p or gcd_num_n == q:
        num_of_squares = 2

        if gcd_num_n == p:
            print(f"The gcd({num},{n}) = p = {p}, so the number of square roots is 2")
            print(f"The roots are:")

            print('-----------')
            num_2 = num%q
            num_2 = pow(num_2,(q+1)//4,q)
            print(f"{num} mod {q} = {num%q}")
            print(f" -->  ({num%q}^({(q+1)}//4))^2 = ({num_2}, {(-num_2)%q})^2 mod {q}")
            print('-----------')

            roots.append(num_2)
            roots.append((-num_2)%q)

            print(f"The roots are: {roots}")

            print('\n-----------')
            print(f'check if {num%p} = {pow(num_2, 2, q)}')
            print(f'If one of the above is False, then the number {num} has no square roots')
            print('-----------')
            
        else:
            print(f"The gcd({num},{n}) = q = {q}, so the number of square roots is 2")
            print(f"The roots are:")

            print('-----------')
            num_1 = num%p
            num_1 = pow(num_1,(p+1)//4,p)
            print(f"{num} mod {p} = {num%p}")
            print(f" -->  ({num%p}^({(p+1)}//4))^2 = ({num_1}, {(-num_1)%p})^2 mod {p}")
            print('-----------')

            roots.append(num_1)
            roots.append((-num_1)%p)

            print(f"The roots are: {roots}")

            print('\n-----------')
            print(f'check if {num%q} = {pow(num_1, 2, p)}')
            print(f'If one of the above is False, then the number {num} has no square roots')
            print('-----------')

        return num_of_squares
    
    if num == 0:
        print(f"The number is 0, so the number of square roots is 1")
        print(f"The root is 0")
        return 1
    
    print(f"The gcd({num},{n}) n = pq, so the number of square roots is 0")
    print(f"The are no square roots")
    return num_of_squares


if __name__ == '__main__':
    p = 31
    q = 71
    n = 2201

    num = 318

    print(square_root(num, p, q, n))