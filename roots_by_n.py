def calc_p_q_root(p_q, b):
    temp_b = b
    print("----------")
    print(f"{temp_b = }")
    print("----------")
    print(f'so - {temp_b} = {temp_b%p_q} mod {p_q}.')
    temp_b = temp_b % p_q
    if temp_b == 0:
        print(f"{b} has only one root modulo {p_q} and it is 0.")
        return 0
    print(f'so - {temp_b} is root modulo {p_q} iff he is the root of: ->')
    print(f'{temp_b}^(({p_q}+1)/4) = {(temp_b**((p_q+1)//4))%p_q} mod {p_q}.')
    a = (temp_b**((p_q+1)//4)) % p_q
    print(f"We will check if {a}^2 = b mod {p_q} ->", end="\n\n")
    if (a**2) % p_q == temp_b:
        print(f"{a}^2 = {temp_b} mod {p_q}.")
        print(f"and that is why {temp_b} = -+({a})^2 mod {p_q}.")
        return a
    print(f"{a}^2 != {temp_b} mod {p_q}.")
    print(f"and that is why b = {temp_b} is not a root modulo {p_q}.")
    return None


def roots_by_n(n, p, q, b):
    print("//////////////////////////////////////////////")
    print("\n----------")
    print(f"{b = }")
    print("----------\n")
    print(f"number {b = } have roots modulo {n = } iff he have roots modulo {p = } and {q = }", end="\n\n")
    print("==============================================")
    print(f'by {p}:')
    a_1 = calc_p_q_root(p, b)
    print("\n==============================================")
    print(f'by {q}:')
    a_2 = calc_p_q_root(q, b)
    print("==============================================", end="\n\n")

    root_count = 0
    if a_1 == 0:
        root_count += 1
    elif a_1 is not None:
        root_count += 2
        
    if a_2 == 0:
        root_count += 1
    elif a_2 is not None:
        root_count += 2

    if root_count == 0:
        print(f"{b} has no roots modulo {n}.")
        return
    elif root_count == 1:
        print(f"{b} has {root_count} root modulo {n} and it is 0.")
        return
    else:
        print(f"{b} has {root_count} roots modulo {n} and they are: {a_1}, {a_2}.")

    roots = []
    if a_1 is not None:
        roots.append(a_1)
    else:
        roots.append(0)
    
    if a_2 is not None:
        roots.append(a_2)
    else:
        roots.append(0)
    
    print(f"Now we will use the Chinese Residue Theorem to find the number in Z_({p}X{q})")

    M_1 = q*(pow(q, -1, p))
    M_2 = p*(pow(p, -1, q))
    
    if root_count % 2 != 0:
        root_count -= 1
    if root_count > 1:
        i_1 = 1
        i_2 = 1
        for r in range(root_count):
            print("\n--------------------")
            if r%2 == 0:
                i_1 *= -1
            elif roots[1] == 0:
                i_1 *= -1
            i_2 *= -1
            print(f"({(roots[0]*i_1)%p}, {(roots[1]*i_2)%q}) ->")
            c = (M_1*(roots[0]*i_1) + M_2*(roots[1]*i_2)) % n
            print(f"{c = } mod {n}")
    print("//////////////////////////////////////////////")


if __name__ == "__main__":
    n = 56977
    p = 251
    q = 227
    
    # b=4524
    b=45423
    # b=4757

    roots_by_n(n, p, q, b)

    # roots_by_n(21733, 103, 211, 21424)

