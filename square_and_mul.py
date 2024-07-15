def square_and_mul(n, c, z, ts, c_ab):
        c_bit = []
        temp_c = c
        s_k = []
        r_k = []

        while temp_c != 0:
            if temp_c % 2 == 0:
                c_bit.insert(0, 0)
            else:
                c_bit.insert(0, 1)
            temp_c >>= 1
        print(f"{c} in binary is {c_bit}")

        k = 0
        z_new = 1
        for i in range(len(c_bit)):
            print("-----------------------------")
            print(f'{i = }')
            print(f'e_i = {c_bit[i]}')
            
            if k == 0:
                s_k.append(1)
                k += 2
                print(f'z^2 = 1 (mod {n})')
            else:
                z_new = (z_new**2)%n
                s_k.append(z_new)
                print(f'z^2 = {s_k[-2]}^2 = {s_k[-1]} (mod {n})')

            if c_bit[i] == 1:
                z_new = (z_new*z)%n
                r_k.append(z_new)
                print(f'z*{z} = {z_new}*{z} = {r_k[-1]} (mod {n})')
        print("-----------------------------")
        print(f'And we got that {c_ab}^{ts} = {z_new} (mod {n})')
        return z_new


if __name__ == "__main__":
    n = 16241
    # c = 2
    # z = 13910
    power = 17
    base = 2093

    square_and_mul(n, power, base, power, base)
