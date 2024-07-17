def chinese_residue_theorem(p, q, n, a, b):
    M_1 = p*(pow(p, -1, q))
    M_2 = q*(pow(q, -1, p))
    print(f"M_1 = p*(p^-1 mod q) = {p}*({p}({p}^-1 mod {q})) = {p}*({pow(p, -1, q)}) = {M_1}")
    print(f"M_2 = q*(q^-1 mod p) = {q}*({q}({q}^-1 mod {p})) = {q}*({pow(q, -1, p)}) = {M_2}")
    
    x_1 = a%q
    x_2 = a%p
    print(f"x_1 = {a} mod {q} = {x_1}")
    print(f"x_2 = {a} mod {p} = {x_2}")

    d_1 = b%(q-1)
    d_2 = b%(p-1)
    print(f"d_1 = {b} mod {q-1} = {d_1}")
    print(f"d_2 = {b} mod {p-1} = {d_2}")

    a_1 = (x_1**d_1)%q
    a_2 = (x_2**d_2)%p
    print(f"a_1 = {x_1}^{d_1} mod {q} = {a_1}")
    print(f"a_2 = {x_2}^{d_2} mod {p} = {a_2}")

    c = (M_1*a_1 + M_2*a_2) % n
    print(f"c = ({M_1}*{a_1} + {M_2}*{a_2}) mod {n} = {c}")
    # print(f'{M_1 = }, {M_2 = }, {a_1 = }, {a_2 = }, {n = }')

    return c


if __name__ == "__main__":
    # base^power mod n
    n = 16241
    p = 109
    q = 149

    base = 10997
    power = 3761

    res_c = chinese_residue_theorem(p, q, n, base, power)

    print(f"Chinese Residue Theorem: {res_c} mod {n}.")
