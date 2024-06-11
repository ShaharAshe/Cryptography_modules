def chinese_residue_theorem(p, q, n, a, b):
    M_1 = p*(pow(p, -1, q))
    M_2 = q*(pow(q, -1, p))
    
    x_1 = a%q
    x_2 = a%p

    d_1 = b%(q-1)
    d_2 = b%(p-1)

    a_1 = x_1**d_1
    a_2 = x_2**d_2

    c = (M_1*a_1 + M_2*a_2) % n

    return c


if __name__ == "__main__":
    n = 143
    p = 11
    q = 13

    a = 15
    b = 103

    res_c = chinese_residue_theorem(p, q, n, a, b)

    print(f"Chinese Residue Theorem: {res_c} mod {n}.")
